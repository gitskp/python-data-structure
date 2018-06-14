def lcm(a,b):
    if a==0 or b==0:
        return 0
    if a>b:
        temp = a
    else:
        temp =b

    while True:
        if temp%a==0 and temp%b==0:
            break
        temp=temp+1
    return temp

if __name__=="__main__":
    a =int(input())
    b =int(input())
    print(lcm(b,a))
