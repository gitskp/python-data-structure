# time complexity : O(nlogn)

# Approach 1
def missing_value(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for num1,num2 in zip(arr1,arr2):
        if num1!=num2:
            return num1
    return arr[-1]


arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(missing_value(arr1,arr2))



# Approach 2

# Time complexity :O(n)
import collections

def missing_value(arr1,arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num]+=1
    for num in arr1:
        if d[num]==0:
            return num
        else:
            d[num] -=1
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(missing_value(arr1,arr2))

# Apporach 3 use XOR
def missing_value(arr1,arr2):
    result=0
    for num in arr1+arr2:
        result^=num
    return result
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(missing_value(arr1,arr2))
