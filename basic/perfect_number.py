def perfect_number(n):
    sum1=0
    for i in range(1,n):
        if n%i==0:
            sum1 =sum1+i
    if sum1==n:
        print("is perfect number")
    else:
        print("is not perfect number")


if __name__ =="__main__":
    n=int(input())
    perfect_number(n)
