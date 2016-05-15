import re

filename = raw_input("Enter the file name:")
try:
    fh = open(filename,'r')
except:
    print "File not found ",filename
count = 0
for lines in fh:
    words = lines.rstrip().split()
    word = list(words)
    str = ''.join(word)
    finder = re.findall('[a-z]+',str)
    count = count + 1
    print finder
print count