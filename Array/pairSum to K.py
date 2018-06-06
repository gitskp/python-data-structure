# https://www.geeksforgeeks.org/count-pairs-with-given-sum/
# Approach 1
def pair_sum(arr,n,k):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == k:
                count+=1
    return count

t= int(input())

for _  in range(t):
    n,k=list(map(int,input().split()))
    arr = [int(x) for x in input().split()]
    print(pair_sum(arr,n,k))

# Time complexity: O(n*n)

#########################################################################

# Approach 2

def pair_sum(arr,k):
    if len(arr)<2:
        return
    # sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k-num

        if target not in seen:
            seen.add(num)
        else:
            output.add(min(num,target),max(num,target))
    return len(output)

    print(pair_sum([1,3,2,2]),4)

# Time complexity : O(n)
