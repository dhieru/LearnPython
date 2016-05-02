import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = raw_input('Enter the count - ')
pos = raw_input('Enter the position - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

def getthelink(url, count):
    temppos = 0;
    while count < 4:
	    html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        # Retrieve all of the anchor tags
        tags = soup('a')
		for tag in tags:
		    if temppos == pos:
			    url = tag.get('href', None)
		        getthelink(url,count+1)
				break
			else :
			    temppos = temppos+1
		break

# Retrieve all of the anchor tags
tags = soup('a')
pos = int(pos)
count = int(count)
newurl=""
tempcount = 0;
i=0
while(i<count):
    for tag in tags:
        print tag.get('href', None)
        tempcount =  tempcount+1
        if (tempcount == pos):
	        newurl = tag.get('href', None)
            count = count+1
	        break
    html = urllib.urlopen(newurl).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
print "the loop ran " + str(tempcount)


import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
position=int(raw_input('Enter Position - '))

count=int(raw_input('Enter Count- '))

for _ in xrange(0,count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup.findAll('a')
    for tag in tags:
        url= tag.get('href')
        tags=soup.findAll('a')
        if not tags[position-1]:
            print "There is no link at that position."
        url = tags[position-1].get('href')
print url
	    
    
    