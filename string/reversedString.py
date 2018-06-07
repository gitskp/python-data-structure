# Revere the string

# Approach 1

def reverse_string(str1):
    return " ".join(reversed(str1.split()))

str1 = "hello how are you"
print(reverse_string(str1))

# Approach 2
def reverse_string(str1):
    return " ".join(str1.split()[::-1])

str1 = "hello how are you"
print(reverse_string(str1))


# Approach 3
def reverse_string(str1):
    words = []
    l = len(str1)
    spaces = [' ']
    i=0
    while i <l:
        if str1[i] not in spaces:
            word_start =i
            while i <l and str1[i] not in spaces:
                i+=1
            words.append(str1[word_start:i])
        i+=1
    return " ".join(reversed(words))


str1 = "hello how are you"
print(reverse_string(str1))
