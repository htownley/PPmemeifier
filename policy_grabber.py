## Install urllib3, certifi, and BeautifulSoup4 ##

import urllib3
import certifi
from bs4 import BeautifulSoup


url = input("Please paste your URL in quotes: ")
url = url[1:-1]
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())
r = http.request('GET', url)
soup = BeautifulSoup(r.data, "html5lib")

paragraphs = soup.find_all('p')

for p in paragraphs:
    print(p.text)
    print("\n")
