import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
total =0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    tag1 = str(tag)
    nums = re.findall('[0-9]+',tag1)
    print nums
    for num in nums:
	    num1 = int(num)
	    total = total + num1
print total