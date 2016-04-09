name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From:'):continue
    words = line.split()
    email = words[1]
    if email in d:
	    d[email] +=1
    else:
	    d[email] = 1
lst = d.values()
m = max(lst)
for addre in d :
    if d[addre] >= m:
	    print addre, d[addre]