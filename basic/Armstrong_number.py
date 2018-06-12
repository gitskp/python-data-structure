def armstrong_number(n):
    temp = n
    sum=0
    while n>0:
        rem = n%10
        sum = sum+rem**3
        n = n//10
    if temp==sum:
        print("armstrong number")
    else:
        print("not armstrong number")

n =int(input())
armstrong_number(n)
