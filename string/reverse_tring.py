# https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

s = "i like this program very much"
words = s.split(' ') 
string =[] 
for word in words: 
    string.insert(0, word) 
  
print("Reversed String:") 
print(" ".join(string)) 