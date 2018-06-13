def ncr(n,r):
    return (factorial(n)/(factorial(r)*factorial(n-r)))

def factorial(n):
    fact=1
    while n:
        fact=fact*n
        n=n-1
    return fact



if __name__=="__main__":
    n=int(input())
    r=int(input())
    print(ncr(n,r))
