import webbrowser
import requests
import os
from bs4 import BeautifulSoup
import urllib 
import urllib2
#webbrowser.open('http://www.ibiblio.org/xml/examples/shakespeare/')
#os.makedirs('Shakespeare', exist_ok=True)
baseurl = 'http://www.ibiblio.org/xml/examples/shakespeare/'
soup = BeautifulSoup(urllib2.urlopen(baseurl))
links=soup.findAll("a")
for link in links[0:]:
	print link.text
	print link['href'], link.string
	print link['href']
	urllib.urlretrieve(baseurl+link['href'], link.string)
print "End"
