import math

def all_prime_factors(n):
	while n%2==0:
		print(2,end=' ')
		n=n/2
	for i in range(3,int(math.sqrt(n))+1,2):
		while n%i==0:
			print(i,end=' ')
			n= n/i
	if n>2:
		return n


n = 36
all_prime_factors(n)
