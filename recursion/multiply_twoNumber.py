def multiply(n,m):
    return product(n,m)
def product(n,m):
    i=0
    prod=0
    while i<n:
        prod = prod+m
        i+=1
    return prod


if __name__=="__main__":
    n= int(input())
    m= int(input())
    print(multiply(n,m))
