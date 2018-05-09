## Install urllib3, certifi, and BeautifulSoup4 ##

import urllib3
import certifi
from bs4 import BeautifulSoup

def policy_grabber(url):
	http = urllib3.PoolManager(
	    cert_reqs='CERT_REQUIRED',
	    ca_certs=certifi.where())
	r = http.request('GET', url)
	soup = BeautifulSoup(r.data, "html5lib")

	paragraphs = soup.find_all('p')
	paragraphs = [p.get_text() for p in paragraphs]

	return paragraphs
