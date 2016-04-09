import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = raw_input('Enter count:')
position = raw_input('Enter position:')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a')
index = 0
while(index < count)
    # Look at the parts of a tag
    print 'TAG:',tag