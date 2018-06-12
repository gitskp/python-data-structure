def palindrome_number(n):
    temp =n
    sum=0
    while n:
        rem= n%10
        sum = rem+sum*10
        n=n//10
    if sum==temp:
        print("palindrome")
    else:
        print("not palidrome")



if __name__=="__main__":
    n = int(input())
    palindrome_number(n)
