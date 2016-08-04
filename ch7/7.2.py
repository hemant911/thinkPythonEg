def square_root(a):
	a = float(a)
	x = 5
	i=0
	while  i < 10:
		y=(x +a/x)/2
		print y
		x = y 
		i+= 1 
	return x

a = int(raw_input("Plaese enter number to check square root :"))
print "An estimate of the square root of a :",square_root(a)