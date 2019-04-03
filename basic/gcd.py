def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)
a = 15
b = 20
print(gcd(a,b))