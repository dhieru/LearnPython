page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
url1 = page[start_link : ]
first_quote = url.find('"')
url = url1[first_quote+1:-2]
print url


# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 4.69327159

#ENTER CODE BELOW HERE
x_str = str(x)
loc_decimal_point = x_str.find('.')
before_decimal_point = x_str[:loc_decimal_point]
next_digit = x_str[loc_decimal_point+1]
digit = int(next_digit)
rounded_number = int(before_decimal_point)
if( digit >= 5):
    rounded_number = rounded_number+1
print rounded_number


def get_next_target(page):
    start_link = page.find('<a href=')
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_link+1)
	url = page[start_quote +1:end_quote]
	return url, end_quote
	
	
	# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps( pence):
    # Your code here
    fivep = 0
    twop = 0
    onep = 0
    if( pence >= 5):
        fivep = pence / 5
        pence = pence % 5
    if(pence >= 2 and pence < 5):
        twop = pence / 2
        pence = pence % 2
    onep = pence
    return fivep,twop,onep
    
print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps

    














