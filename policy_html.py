
from bs4 import BeautifulSoup

def generate_pdf(policy_url, collected_data, not_collected_data, third_party_data):
	
	fw1 = ""
	fw2 = ""
	fw3 = ""
	fw4 = ""
	fw5 = ""
	fw6 = ""
	fw7 = ""

	fw1b = ""
	fw2b= ""
	fw3b = ""
	fw4b= ""
	fw5b= ""
	fw6b = ""
	fw7b= ""

	fw1tp = ""
	fw2tp = ""
	fw3tp = ""
	fw4tp = ""
	fw5tp = ""
	fw6tp = ""
	fw7tp = ""

	if (len(collected_data) >= 1):
		fw1 = collected_data[0]
	else:
		fw2 = "Nothing"
	if (len(collected_data) >= 2):
		fw2 = collected_data[1]
	if (len(collected_data) >= 3):
		fw3 = collected_data[2]
	if (len(collected_data) >= 4):
		fw4 = collected_data[3]
	if (len(collected_data) >= 5):
		fw5 = collected_data[4]
	if (len(collected_data) >= 6):
		fw6 = collected_data[5]
	if (len(collected_data) >= 7):
		fw7 = "And even more... (see the command line for details)"

	if (len(not_collected_data) >= 1):
		fw1b = not_collected_data[0]
	else:
		fw2b = "Nothing"
	if (len(not_collected_data) >= 2):
		fw2b= not_collected_data[1]
	if (len(not_collected_data) >= 3):
		fw3b = not_collected_data[2]
	if (len(not_collected_data) >= 4):
		fw4b= not_collected_data[3]
	if (len(not_collected_data) >= 5):
		fw5b= not_collected_data[4]
	if (len(not_collected_data) >= 6):
		fw6b = not_collected_data[5]
	if (len(not_collected_data) >= 7):
		fw7b= "And even more... (see the command line for details)"

	if (len(third_party_data) >= 1):
		fw1tp = third_party_data[0]
	else:
		fw1tp = "Nothing"
	if (len(third_party_data) >= 2):
		fw2tp = third_party_data[1]
	if (len(third_party_data) >= 3):
		fw3tp = third_party_data[2]
	if (len(third_party_data) >= 4):
		fw4tp = third_party_data[3]
	if (len(third_party_data) >= 5):
		fw5tp = third_party_data[4]
	if (len(third_party_data) >= 6):
		fw6tp = third_party_data[5]
	if (len(third_party_data) >= 7):
		fw7tp = "And even more... (see the command line for details)"

	fw1btp = ""
	fw2btp = ""
	fw3btp  = ""
	fw4btp = ""
	fw5btp = ""
	fw6btp  = ""
	fw7btp = ""

	css = 'style.css'

	#load the HTML template
	with open ("in.html") as htmlin:
	    txt = htmlin.read()
	    soup = BeautifulSoup(txt, "html5lib")

	# Inserting the policy tag

	# p.one
	temp_soup = BeautifulSoup('<h2>Analyzing '+policy_url+'</h2>',"html5lib")
	h2_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, h2_tag)

	# Inserting the found words' tags

	# p.one
	temp_soup = BeautifulSoup('<p class="one">'+ fw1 + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.two
	temp_soup = BeautifulSoup('<p class="two">'+ fw2 + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.three
	temp_soup = BeautifulSoup('<p class="three">'+ fw3 + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.four
	temp_soup = BeautifulSoup('<p class="four">'+ fw4 + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.five
	temp_soup = BeautifulSoup('<p class="five">'+ fw5 + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.six
	temp_soup = BeautifulSoup('<p class="six">'+ fw6 + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.seven
	temp_soup = BeautifulSoup('<p class="seven">'+ fw7 + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.oneb
	temp_soup = BeautifulSoup('<p class="oneb">'+ fw1b + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.twob
	temp_soup = BeautifulSoup('<p class="twob">'+ fw2b + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.threeb
	temp_soup = BeautifulSoup('<p class="threeb">'+ fw3b + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.fourb
	temp_soup = BeautifulSoup('<p class="fourb">'+ fw4b + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.fiveb
	temp_soup = BeautifulSoup('<p class="fiveb">'+ fw5b + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.sixb
	temp_soup = BeautifulSoup('<p class="sixb">'+ fw6b + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.sevenb
	temp_soup = BeautifulSoup('<p class="sevenb">'+ fw7b + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)

	###### Make this work for TP as well ########

	# p.onetp
	temp_soup = BeautifulSoup('<p class="onetp">'+ fw1tp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.twotp
	temp_soup = BeautifulSoup('<p class="twotp">'+ fw2tp+ '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.threetp
	temp_soup = BeautifulSoup('<p class="threetp">'+ fw3tp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.fourtp
	temp_soup = BeautifulSoup('<p class="fourtp">'+ fw4tp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.fivetp
	temp_soup = BeautifulSoup('<p class="fivetp">'+ fw5tp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.sixtp
	temp_soup = BeautifulSoup('<p class="sixtp">'+ fw6tp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.seventp
	temp_soup = BeautifulSoup('<p class="seventp">'+ fw7tp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.onebtp
	temp_soup = BeautifulSoup('<p class="onebtp">'+ fw1btp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.twobtp
	temp_soup = BeautifulSoup('<p class="twobtp">'+ fw2btp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.threebtp
	temp_soup = BeautifulSoup('<p class="threebtp">'+ fw3btp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.fourbtp
	temp_soup = BeautifulSoup('<p class="fourbtp">'+ fw4btp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.fivebtp
	temp_soup = BeautifulSoup('<p class="fivebtp">'+ fw5btp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.sixbtp
	temp_soup = BeautifulSoup('<p class="sixbtp">'+ fw6btp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)
	# p.sevenbtp
	temp_soup = BeautifulSoup('<p class="sevenbtp">'+ fw7btp + '</p>',"html5lib")
	p_tag = temp_soup.html.body.contents[0]
	soup.body.insert(3, p_tag)


	##########


	# Code for partial image inclusion
	# if (collect):
	#     new_photo = soup.new_tag("img", src="collect.png")
	#     # insert it into the document
	#     soup.head.append(new_photo)
	# if (third_party):
	#     new_photo = soup.new_tag("img", src="third_party.png")
	#     # insert it into the document
	#     soup.head.append(new_photo)

	# save the file
	with open("report.html", "w") as htmlout:
	    htmlout.write(str(soup))