def text_is_relevant(text, keywords):

	for keyword in keywords:
		if keyword.lower() in text.lower():
			return True
	return False

def text_is_NOT_relevant(text, keywords):
	for keyword in keywords:
		if ("not" + keyword.lower() in text.lower()) or ("never" + keyword.lower() in text.lower()) or ("n't" + keyword.lower() in text.lower()):
			return True
	return False

data_types = ["gps", "location", "IP address", "email address", 
	"generic information", "personal information", "name", "cookies",
	"device", "log", "mailing address", "phone number", "contact preferences",
	"contacts", "credit card", "occupation", "language", "area code", "zip code",
	"unique device identifier", "referrer URL", "time zone", "customer activities",
	"search queries", "child", "metrics", "weight", "sleep", "heart rate", 
	"cell tower", "GPS", "browser", "operating system", "identifiers", 
	"referring web page", "voice", "payment data", "health data", "password",
	"transaction", "phone", "debit card", "contact details", "contributions", 
	"occupation", "employer", "information you provide directly", "postal address",
	"video", "audio", "messages", "analytical information", "diagnostic information",
	"vibration controls", "children"]

collect_keywords = [" use ", " provid", " collect"]
third_party_keywords = ["third parties", "third-parties", "third party", "third-party","3rd-party", "3rd party", "3rd parties", "3rd-parties"]
negation_terms = ["n't", "never", "not"]

data_types = list(set(data_types))

def collect_test(all_sentences):

	possible_data_collected = set()
	possible_NOT_data_collected = set()

	relevant_text = []
	relevant_NOT_text = []

	for sentence in all_sentences:
		if text_is_NOT_relevant(sentence, collect_keywords):
			relevant_NOT_text.append(sentence)
		elif text_is_relevant(sentence, collect_keywords):
			relevant_text.append(sentence)

	for sentence in relevant_text:
		for data_type in data_types:
			if data_type.lower() in sentence.lower():
				possible_data_collected.add(data_type)

	for sentence in relevant_NOT_text:
		for data_type in data_types:
			if data_type.lower() in sentence.lower():
				possible_NOT_data_collected.add(data_type)

	print("data that is possibly collected:")
	possible_data_collected = list(possible_data_collected)
	for i in range(len(possible_data_collected)):
		print('    ',i+1, possible_data_collected[i])
	print()

	print("data that is possibly NOT collected:")
	possible_NOT_data_collected = list(possible_NOT_data_collected)
	for i in range(len(possible_NOT_data_collected)):
		print('    ',i+1, possible_NOT_data_collected[i])
	print()

	return


def third_party_test(all_sentences):

	possible_data_collected = set()

	relevant_text = []

	for sentence in all_sentences:
		if text_is_relevant(sentence, third_party_keywords):
			relevant_text.append(sentence)

	for sentence in relevant_text:
		for data_type in data_types:
			if data_type.lower() in sentence.lower():
				possible_data_collected.add(data_type)

	print("data that is possibly transfered to or shared with third parties:")
	possible_data_collected = list(possible_data_collected)
	for i in range(len(possible_data_collected)):
		print('    ', i+1, possible_data_collected[i])
	print()

	return


