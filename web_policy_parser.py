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
# start main function
def main():

	keywords = ["privacy"]

	url = input("url:  ")
	all_paragraphs = policy_grabber(url)

	relevant_sentences = []

	for paragraph in all_paragraphs:
		sentences = text_to_sentence(paragraph)

		for sentence in sentences:
			if text_is_relevant(sentence, keywords):
				relevant_sentences.append(sentence)


	print(len(relevant_sentences))
	print(relevant_sentences)





##########  End of main()  ####################################


###############################################################
# Various auxiliary functions:


def text_to_sentence(text):
	all_sentences = []
	sentence = []

	for ch in text:
		sentence.append(ch)

		if sentence[-1] == "." or sentence[-1] == "\n":
			sentence = "".join(sentence)
			all_sentences.append(sentence)
			sentence = []

	return all_sentences

def file_to_paragraph(file):
	all_paragraphs = []

	for line in file:
		all_paragraphs.append(line)

	return all_paragraphs


def text_is_relevant(text, keywords):

	for keyword in keywords:
		if keyword in text.lower():
			return True
	return False


while True:

	if __name__== "__main__":
		main()

