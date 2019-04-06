import sys

def second_largest(arr,n):
	max1 = -sys.maxsize
	max2 = -sys.maxsize

	for i in range(0,n):
		if arr[i]>max1:
			max2 = max1
			max1 = arr[i]
		elif arr[i]>max2 and arr[i]<max1:
			max2 = arr[i]
	print(max2)

	

arr = [1,2,0,-1,20,30,-2,100]
n = len(arr)
second_largest(arr,n)