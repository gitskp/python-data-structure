def palindrome_string(string):
    i=0
    n = len(string)
    while i<len(string):
        if string[i]==string[-1-i]:
            i+=1
            return True
        return False


string ="mama"
print(palindrome_string(string))
