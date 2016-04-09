# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
str = fh.read()
print str.upper()



# Program 2
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0.0
add = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count +1
    value = line.split(':')
    num = value[1]
    num1 = float(num)
    add = add + num1
avg = float(add/count)
print "Average spam confidence: %.12f" %avg
