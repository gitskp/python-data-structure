def number_sum(n):
    sum=0
    while n>0:
        rem=n%10
        sum= sum+rem
        n//=10
    return sum
    

if __name__=="__main__":
    n= int(input())
    print(number_sum(n))
