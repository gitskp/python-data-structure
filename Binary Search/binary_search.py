def binray_search(arr,n,x):
	low = 0
	high = n-1
	while(low<=high):
		mid = low+(high-low)//2
		if x==arr[mid]:
			return mid
		elif x<arr[mid]:
			high=mid-1
		else:
			low = mid+1
	return -1


arr = [1,2,4,8,10,22,34,56,78]
x=34
n = len(arr)
print(binray_search(arr,n,x))