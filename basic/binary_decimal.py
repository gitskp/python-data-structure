def BinaryToDecimal(binary):
    decimal,i=0,0
    while binary!=0:
        dec = binary%10
        decimal = decimal+dec*pow(2,i)
        i+=1
        binary//=10
    print(decimal)

# Driver code
if __name__ == '__main__':
    BinaryToDecimal(1000)
