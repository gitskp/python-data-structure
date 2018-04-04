def bubble_sort(list1):

   # outer loop n-1 times
    for i in range(0, len(list1)-1):

        # inner loop n-1-i times
        for j in range(0,len(list1)-1-i):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]

    return list1



list1 = [10,8,9,7,4,5,32,1]
print(bubble_sort(list1))
