def check_prime(n):
	if n>1:
		for i in range(2,n):
			if n%i==0:
				print("Number is not prime")
				break;
		else:
			print("Number is prime")

check_prime(35)