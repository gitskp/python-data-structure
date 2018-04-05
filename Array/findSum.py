def findSum(arr,n):
    arr.sort()
    sum =0
    for i in range(0, n):
        if arr[i] != arr[i+1]:
            sum = sum + arr[i]
    return sum
arr = [1, 2, 3, 1, 1, 4, 5, 6]
n = len(arr)
findSum(arr,n)

