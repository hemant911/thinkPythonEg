def gcd(a,b):
	if b == 0:
		return a
	else:
		r = a % b 
		return gcd(b,r)

print "GREATEST COMMON DIVISOR IS :",gcd(1071,462)	