'''
The Privacy Policy Memeifier
Analyzes privacy policies you might encounter during your everyday
internet browsing. Analyzes those policies and helps you understand
what they might be saying.
''' 

import os 


# Introduction:
print(("\n=======================================================\n"
		"Hello There! Welcome to The Privacy Policy Memeifier.\n"
		"=======================================================\n"
		"Have you got a dense, opaque, unreadable pile of legal\n"
		"privacy jargon that you can't make heads or tails of?\n"
		"I can help with that! Just let me know where to look:\n"
		"(<filename.txt> OR <path-to-filename.txt>)"))



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


keyword = ""
first_time = True

while(True):

	# get keyword to search for
	if first_time:
		first_time = False
		keyword = input("What keyword should I search for?  ")
	else:
		keyword = input(
			"--------------------------------------------------------\n"
			"Would you like to try again? What keyword should I search\n"
			"for this time? (or \"quit\")   ")
	print()

	# quit if necessary
	if keyword.lower() == "quit":
		exit()


	# analyze text file
	print()
	print("Analyzing " + path_to_policy + "...")
	print()

	relevant_sentences = []

	with open(path_to_policy, 'r') as file:

		for line in file:
			if keyword in line.lower():
				relevant_sentences.append(line)


	# print findings
	print("This is what I found:")
	counter = 1

	for sentence in relevant_sentences:
		print(counter, sentence)
		counter += 1


	input("Hit any key to continue.")












