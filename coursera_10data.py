name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):continue
    words = line.split()
    time = words[5]
    timeinhr = time.split(':')
    hr = timeinhr[0]
    if hr in d:
        d[hr] += 1
    else:
	    d[hr] = 1

lst = list()
for k,v in d.items():
    lst.append((k,v))
lst.sort()
for k,v in lst:
    print k,v
