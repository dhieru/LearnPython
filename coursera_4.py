def computepay(h,r):
	grosspay = 0.0
	if h > 40:
		hourextra = h-40
		grosspay = 40*r + (1.5*hourextra*r)
	else :
		grosspay = h*r
	return grosspay

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate of pay:")
r = float(rate)
p = computepay(h,r)
print p