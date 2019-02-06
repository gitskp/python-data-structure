def binray_search_recursive(arr,low,high,x):
	mid = low+(high-low)//2
	if low>high:
		return -1

	if x == arr[mid]:
		return mid
	elif x<arr[mid]:
		return binray_search_recursive(arr,low,high-1,x)
	else:
		return binray_search_recursive(arr,mid+1,high,x)
arr = [1,2,4,8,10,22,34,56,78]
x=100
n = len(arr)
low=0
high= n-1
print(binray_search_recursive(arr,low,high,x))