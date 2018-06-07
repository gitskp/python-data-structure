# RETURN TRUE IF THERE IS UNIQUE CHARACTER IN STRING
# Approach 1:

'def uniqueChar(str1):
    return len(set(str1)) == len(str1)
str1 = "abcde"
print(uniqueChar(str1))



# Approach 2
def uniqueChar(str1):
    chars = set()
    for letter in str1:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True


str1 = "aabcde"
print(uniqueChar(str1))
