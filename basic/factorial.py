def factorial(n):
    i=1
    f=1
    while i<=n:
        f= f*i
        i+=1
    return f

if __name__ == "__main__":
    n= int(input())
    print(factorial(n))
