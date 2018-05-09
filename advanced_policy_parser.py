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
import textwrap
from gensim.models import KeyedVectors
import time
import sys


# start main function
def main():

	# Load pretrained Google word2vec model
	model = load_word2vec_model()

	###############################################################
	# Introduction:
	print(("\n=======================================================\n"
			"Hello There! Welcome to The Privacy Policy Memeifier.\n"
			"=======================================================\n"
			"Have you got a dense, opaque, unreadable pile of legal\n"
			"privacy jargon that you can't make heads or tails of?\n"
			"I can help with that! Just let me know where to look:\n"
			"(<filename.txt> OR <path-to-filename.txt>)"))


	##############################################################
	# get path to privacy policy text file
	while(True):

		path_to_policy = input()
		print()

		# check to make sure filename is valid
		if not os.path.isfile(path_to_policy):
			print("Invalid file or path. Please try again:")
			print("(<filename.txt> OR <path-to-filename.txt> OR \"quit\")")
		else:
			break


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
				keyword = input("What keyword should I search for?  ")
			else:
				keyword = input(
					"\n--------------------------------------------------------\n"
					"Would you like to try again? What keyword should I search\n"
					"for this time? (or \"quit\")   ")

			# quit if necessary
			if keyword == "quit":
				exit()

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
		print("Analyzing " + path_to_policy + "...")
		print()

		all_sentences = []
		relevant_sentences = []

		with open(path_to_policy, 'r') as file:

			all_sentences = file_to_sentence(file)

			for sentence in all_sentences:
				if text_is_relevant(sentence, all_keywords):
					relevant_sentences.append(sentence)


		#####################################
		# print findings
		if len(relevant_sentences) > 0:
			print("I found {} sentences related to the keyword {}. Would you like to see them?".format(len(relevant_sentences), keyword))
			response = input("(\"yes\" OR \"no\"):  ")

			if response == "yes":
				counter = 1
				for sentence in relevant_sentences:
					sentence = textwrap.wrap(sentence)
					print(str(counter) + ": " + sentence[0])
					if len(sentence) > 0:
						for piece in sentence[1:]:
							print("   " + piece)

					counter += 1
		else:
			print("I found {} sentences with the keyword {}.".format(len(relevant_sentences), keyword))



		input("Hit any key to continue.")


# returns list of words similiar to keyword
# len(list) is on the order of topn in size
def keyword_expander(keyword, topn, model):
	result = model.most_similar(positive=[keyword], topn=topn)
	result_lower = model.most_similar(positive=[keyword.lower()], topn=topn)
	result_title = model.most_similar(positive=[keyword.title()], topn=topn)

	result = result + result_lower + result_title
	result = [tple[0].lower().replace("_", " ") for tple in result]
	print(len(result))
	result = list(set(result))
	print(len(result))

	return result

def file_to_sentence(file):
	all_sentences = []
	sentence = []

	for line in file:
		for ch in line:
			sentence.append(ch)

			if sentence[-1] == "." or sentence[-1] == "\n":
				sentence = "".join(sentence)
				all_sentences.append(sentence)
				sentence = []

	return all_sentences


def load_word2vec_model():
	###############################################################
	# Load pretrained Google word2vec model
	print("Loading pretrained Google word2vec model...")
	print("expected time on the order of 60 sec")
	start_time = time.time()
	filename = 'GoogleNews-vectors-negative300.bin'
	model = KeyedVectors.load_word2vec_format(filename, binary=True)
	testing123 = model.most_similar(positive=["testing"], topn=20)
	print("Successfully loaded model ({} sec)".format(time.time() - start_time))
	return model

def text_is_relevant(text, keywords):

	for keyword in keywords:
		if keyword in text:
			return True
	return False



if __name__== "__main__":
  main()










