import json
import urllib

serviceurl = '  http://python-data.dr-chuck.net/comments_239603.json'

uh = urllib.urlopen(serviceurl)
data = uh.read()
print "retrieved data", len(data),"characters"
info = json.loads(str(data))
print json.dumps(info, indent=4)
sum = 0
for item in info["comments"]:
    sum = sum + item["count"]
    print item["count"]
print sum
	