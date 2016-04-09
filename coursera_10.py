fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	words = line.split()
    for word in words:
	    if word in lst: continue
	    else:
            lst.append(word)
 print sorted(lst)
 
 
 import urllib
 from BeautifulSoup import *
 
 url = raw_input('Enter - ')
 html = urllib.urlopen(url).read()
 soup = BeautifulSoup(html)
 tags = soup('a')
 for tag in tags:
     print tag.get('href',None)

