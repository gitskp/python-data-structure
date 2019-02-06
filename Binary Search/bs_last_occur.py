# Find the last occurence of elememts in array using binray search
def BS_first_occur(arr,n,x):
	low =0
	high= n-1
	result = -1
	while(low<=high):
		mid = low+(high-low)//2
		if x ==arr[mid]:
			result=mid
			low= mid+1
		elif x<arr[mid]:
			high= mid-1
		else:
			low= mid+1

	return result



arr = [2,4,10,10,10,18,20]
n = len(arr)
x=10
print(BS_first_occur(arr,n,x))
