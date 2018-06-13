def reverse_number(n):
    reverse=0
    while n:
        rem= n%10
        reverse= reverse*10+rem
        n//=10
    return reverse

if __name__ =="__main__":
    n = int(input())
    print(reverse_number(n))
