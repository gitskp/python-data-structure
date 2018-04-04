# A Python implementation to count quadruples from four sorted arrays
# whose sum is equal to a given value x

# function to count all quadruples from
# four sorted arrays whose sum is equal
# to a given value x
def countQuuadruples(arr1,arr2,arr3,arr4,n,x):
    count = 0

    #  generate all possible quadruples from
    # the four sorted arrays
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):

                    #  check whether elements of
                    #  quadruple sum up to x or not
                    if arr1[i]+arr2[j]+arr3[k]+arr4[l] == x:
                        count += 1
    # required count of quadruples
    return count


# Driver Program
arr1 = [1, 4, 5, 6]
arr2 = [2, 3, 7, 8]
arr3 = [1, 4, 6, 10]
arr4 = [2, 4, 7, 8 ]
n = len(arr1)
x = 30
print("Count=",countQuuadruples(arr1,arr2,arr3,arr4,n,x))
