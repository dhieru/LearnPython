import urllib
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = raw_input('Enter location: ')

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None
print len(js["results"])
i = 0;
while i < len(js["results"]):
    if(js["results"][i]["geometry"]["location_type"] == "GEOMETRIC_CENTER"):
        placeid = js["results"][i]["place_id"]
        print placeid
        break