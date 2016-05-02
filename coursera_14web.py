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