def modexp(x,y,n):
	"""returns the result of x^y mod n"""
	if y == 0: return 1

	partial = modexp(x, y/2, n)

	if y%2 == 0: return (partial**2) % n
	else: return (x*partial**2) % n

def last_digits(x,y,n):
	"""returns the n last digits of x^y as a string"""
	r = modexp(x,y, 10**n)

	#post processing to make sure we didn't cut off a leading 0
	return str(r).zfill(n)




if __name__ == "__main__":
	#test cases
	print(modexp(2,10,100000) == 1024)
	print(last_digits(2,10,2) == "24")
	print(last_digits(2,10,3) == "024")
	print(last_digits(3,123456789,500))