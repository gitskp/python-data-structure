def strong_number(n):
    temp = n
    sum1=0
    while n:
        i=1
        f=1
        rem = n%10
        while(i<=rem):
            f = f*i
            i+=1
        sum1= sum1+f
        n=n//10
    if sum1==temp:
        print("it is strong  number")
    else:
        print("it is not strong number")





if __name__=="__main__":
    n = int(input())
    strong_number(n)
