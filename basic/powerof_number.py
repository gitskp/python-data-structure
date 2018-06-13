def powerof_number(num,pow1):
    sum=1
    i=1
    while i<=pow1:
        sum=sum*num
        i+=1
    return sum

if __name__=="__main__":
    num= int(input())
    pow1= int(input())
    print(powerof_number(num,pow1))
