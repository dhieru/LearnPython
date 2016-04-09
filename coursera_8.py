import re
filename = raw_input("Enter the file name to open : ")
fopen = open(filename)
stringread = fopen.read()
total = 0
nums = re.findall('[0-9]+',stringread)
for num in nums:
	num1 = int(num)
	total = total + num1
print total