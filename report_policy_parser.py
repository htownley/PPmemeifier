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
import requests

from policy_grabber import policy_grabber
from policy_tests import *



###############################################################
# start main function
def main(model):

	# Introduction:
	introduction()

	# figure out whether the privacy policy text is online or in a file
	url_bool, file_bool = url_or_text()

	# load privacy policy into paragraphs list
	all_sentences, policy_location = policy_collecter(url_bool, file_bool)

	# analyze text file
	print()
	print("Analyzing " + policy_location + "...")
	print()

	collect_test(all_sentences)
	third_party_test(all_sentences)

	return


##########  End of main()  ####################################


###############################################################
# Various auxiliary functions:
def introduction():
	print(("\n=======================================================\n"
			"Hello There! Welcome to The Privacy Policy Memeifier.\n"
			"=======================================================\n"
			"Have you got a dense, opaque, unreadable pile of legal\n"
			"privacy jargon that you can't make heads or tails of?\n"
			"I can help with that! Just let me know where to look.\n"))
	return

def url_or_text():

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

	return url_bool, file_bool

# prompts user for exact policy location and loads text into list
def policy_collecter(url_bool, file_bool):
	all_paragraphs = []
	all_sentences = []

	if url_bool:
		print("\nPlease enter the full URL:")
		print("(<URL>)")

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
					all_sentences = string_to_sentence(all_paragraphs)
					break
			except Exception as err:
				print()
				print(err)
				print("Please try again:")
				print("(<URL>)")

	elif file_bool:
		print("\nPlease enter the file or filename:")
		print("(<filename.txt> OR <path-to-filename.txt>)")

		while(True):
			user_input = input()
			if user_input == "done":
				return

			# check to see if filename is valid
			if os.path.isfile(user_input):
				with open(user_input, 'r') as file:
					all_sentences = file.readlines()
					all_sentences = "".join(all_sentences)
					all_sentences = string_to_sentence(all_sentences)

				break
			else:
				print("\nInvalid filename. Please try again:")
				print("(<filename.txt> OR <path-to-filename.txt>)")

	return all_sentences, user_input


# returns list of words similiar to keyword
# len(list) is on the order of topn in size
def keyword_expander(keyword, topn, model):
	result = model.most_similar(positive=[keyword], topn=topn)
	result_lower = model.most_similar(positive=[keyword.lower()], topn=topn)
	result_title = model.most_similar(positive=[keyword.title()], topn=topn)

	result = result + result_lower + result_title
	result = [tple[0].lower().replace("_", " ") for tple in result]
	result.append(keyword)

	print(len(result))
	result = list(set(result))
	print(len(result))

	return result

def string_to_sentence(text):
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




if __name__== "__main__":
	main(model)










