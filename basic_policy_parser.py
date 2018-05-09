'''
The Privacy Policy Memeifier
Analyzes privacy policies you might encounter during your everyday
internet browsing. Analyzes those policies and helps you understand
what they might be saying.
''' 

import os
import textwrap

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
	keyword = keyword.lower()

	# quit if necessary
	if keyword == "quit":
		exit()

	#####################################
	# analyze text file
	print()
	print("Analyzing " + path_to_policy + "...")
	print()

	all_sentences = []
	relevant_sentences = []

	with open(path_to_policy, 'r') as file:

		sentence = []

		for line in file:
			for ch in line:
				sentence.append(ch)

				if sentence[-1] == "." or sentence[-1] == "\n":
					sentence = "".join(sentence)
					all_sentences.append(sentence)
					sentence = []

		for sentence in all_sentences:
			if keyword in sentence:
				relevant_sentences.append(sentence)


	#####################################
	# print findings
	if len(relevant_sentences) > 0:
		print("I found {} sentences with the keyword {}. Would you like to see them?".format(len(relevant_sentences), keyword))
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












