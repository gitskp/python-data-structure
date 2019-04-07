def traingle_possible_count(arr,n):
	count =0
	for i in range(n):
		for j in range(i+1,n):
			for k in range(j+1,n):
				if arr[i]+arr[j]>arr[k]:
					count +=1
	return count
#arr = [10, 21, 22, 100, 101, 200, 300]
arr = [4, 6, 3, 7]

n = len(arr)
print(traingle_possible_count(arr,n))