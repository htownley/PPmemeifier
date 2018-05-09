'''
The Privacy Policy Memeifier
Analyzes privacy policies you might encounter during your everyday
internet browsing. Analyzes those policies and helps you understand
what they might be saying.

Installation:
	pip install --upgrade pip
	pip install gensim

Download:
	https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing
''' 

import os
import time
import sys

import textwrap
from gensim.models import KeyedVectors
import requests

from policy_grabber import policy_grabber


###############################################################
# Load pretrained Google word2vec model
def load_word2vec_model():
	print("Loading pretrained Google word2vec model...")
	print("expected time on the order of 60 sec")
	start_time = time.time()
	filename = 'GoogleNews-vectors-negative300.bin'
	model = KeyedVectors.load_word2vec_format(filename, binary=True)
	testing123 = model.most_similar(positive=["testing"], topn=20)
	print("Successfully loaded model ({} sec)".format(time.time() - start_time))
	return model

model = load_word2vec_model()

## for testing purposes:
# while True:
# 	test_keyword = input("keyword:")
# 	for word in keyword_expander(test_keyword, 10, model):


###############################################################
# start main function
def main(model):

	###############################################################
	# Introduction:
	print(("\n=======================================================\n"
			"Hello There! Welcome to The Privacy Policy Memeifier.\n"
			"=======================================================\n"
			"Have you got a dense, opaque, unreadable pile of legal\n"
			"privacy jargon that you can't make heads or tails of?\n"
			"I can help with that! Just let me know where to look.\n"))

	##############################################################
	# figure out where the privacy policy text is
	url_bool = False
	file_bool = False

	while True:
		print("Please type either \"url\" or \"file\" to indicate whether\n"
			"the privacy policy can be found online or in a local text file:")
		print("type \"quit\" to exit.")

		user_input = input()

		if user_input == "quit":
			exit()
		elif user_input == "url":
			url_bool = True
			break
		elif user_input == "file":
			file_bool = True
			break


	##############################################################
	# load privacy policy into paragraphs list
	all_paragraphs = []

	if url_bool:
		print("\nPlease enter the full URL:")
		print("(<URL> OR \"done\")")

		while(True):
			user_input = input()
			if user_input == "done":
				return

			# check to see if URL is valid
			try:
				request = requests.get(user_input)
				if request.status_code == 200:
					all_paragraphs = policy_grabber(user_input)
					all_paragraphs = "\n".join(all_paragraphs)
					all_paragraphs = file_to_sentence(all_paragraphs)
					break
			except Exception as err:
				print()
				print(err)
				print("Please try again:")
				print("(<URL> OR \"done\")")

	if file_bool:
		print("\nPlease enter the file or filename:")
		print("(<filename.txt> OR <path-to-filename.txt> OR \"done\")")

		while(True):
			user_input = input()
			if user_input == "done":
				return

			# check to see if filename is valid
			if os.path.isfile(user_input):
				with open(user_input, 'r') as file:
					all_paragraphs = file.readlines()
					all_paragraphs = "".join(all_paragraphs)
					all_paragraphs = file_to_sentence(all_paragraphs)

				break
			else:
				print("\nInvalid filename. Please try again:")
				print("(<filename.txt> OR <path-to-filename.txt> OR \"done\")")


	##############################################################
	# main loop:

	keyword = ""
	first_time = True

	while(True):

		all_keywords = []

		while True:
			#####################################
			# get keyword to search for
			if first_time:
				first_time = False
				keyword = input("\nWhat keyword should I search for?  ")
			else:
				keyword = input(
					"\n--------------------------------------------------------\n"
					"Would you like to try again? What keyword should I search\n"
					"for this time? (or \"done\")   ")

			# quit if necessary
			if keyword == "done":
				return

			#####################################
			# Find list of words related to keyword to search for in text file
			try:
				all_keywords = keyword_expander(keyword, 30, model)
				break
			except KeyError as err:
				print(err)
				print()

		#####################################
		# analyze text file
		print()
		print("Analyzing " + user_input + "...")
		print()

		relevant_text = []

		for paragraph in all_paragraphs:
			if text_is_relevant(paragraph, all_keywords):
				relevant_text.append(paragraph)


		#####################################
		# print findings
		if len(relevant_text) > 0:
			print("I found {} sentence(s) related to the keyword {}. Would you like to see them?".format(len(relevant_text), keyword))
			response = input("(\"yes\" OR \"no\"):  ")

			if response == "yes":
				counter = 1
				for text in relevant_text:
					text = textwrap.wrap(text)
					print(str(counter) + ": " + text[0])
					if len(text) > 0:
						for piece in text[1:]:
							print("   " + piece)

					counter += 1
		else:
			print("I found {} sentence(s) related to the keyword {}.".format(len(relevant_text), keyword))



		input("Hit any key to continue.")

##########  End of main()  ####################################


###############################################################
# Various auxiliary functions:


# returns list of words similiar to keyword
# len(list) is on the order of topn in size
def keyword_expander(keyword, topn, model):
	result = model.most_similar(positive=[keyword.title()], topn=topn)
	result_lower = model.most_similar(positive=[keyword.lower()], topn=topn)

	result = result + result_lower
	result = sorted(result, key=lambda thing: thing[1])
	result = result[0:30]

	print("set of {} most similiar words which will also be searched\nfor in the document:".format(topn))
	for thing in result:
		print(thing)

	result = [tple[0].lower().replace("_", " ") for tple in result]
	result = [keyword] + result

	result = list(set(result))

	return result

def file_to_sentence(text):
	all_sentences = []
	sentence = []

	for ch in text:
		sentence.append(ch)

		if sentence[-1] == '.' or sentence[-1] == '\n':
			sentence = "".join(sentence)
			all_sentences.append(sentence)
			sentence = []

	if len(sentence) > 0:
		all_sentences.append("".join(sentence))
		sentence = []

	return all_sentences

def file_to_paragraph(file):
	all_paragraphs = []

	for line in file:
		all_paragraphs.append(line)

	return all_paragraphs


def text_is_relevant(text, keywords):

	for keyword in keywords:
		if keyword.lower() in text.lower():
			return True
	return False


while True:

	if __name__== "__main__":
		main(model)










