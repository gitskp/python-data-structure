# count occurence of  a number in a sorted array with duplicates using binray search
def count(arr, x, n): 
  
    # get the index of first 
    # occurrence of x  
    i = first(arr,x,n) 
   
    # # If x doesn't exist in  
    # # arr[] then return -1  
    # if i == -1: 
    #     return i 
      
    # # Else get the index of last occurrence 
    # # of x. Note that we are only looking 
    # # in the subarray after first occurrence    
    j = last(arr,x,n);      
      
    # return count  
    return j-i+1; 
def first(arr,x,n):
	low =0
	high= n-1
	result1 = -1
	while(low<=high):
		mid = low+(high-low)//2
		if x ==arr[mid]:
			result1=mid
			high= mid-1
		elif x<arr[mid]:
			high= mid-1
		else:
			low= mid+1

	return result1

def last(arr,x,n):
	low =0
	high= n-1
	result2 = -1
	while(low<=high):
		mid = low+(high-low)//2
		if x ==arr[mid]:
			result2=mid
			low= mid+1
		elif x<arr[mid]:
			high= mid-1
		else:
			low= mid+1

	return result2

arr = [1, 2, 2, 3, 3, 3, 3,5,5,5,5,5,5] 
x = 5  # Element to be counted in arr[] 
n = len(arr) 
c = count(arr, x, n) 
print ("%d occurs %d times "%(x, c)) 