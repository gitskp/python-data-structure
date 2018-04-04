def selection_sort(list1):
    for i in range(0,len(list1)-1):
        minIndex = i
        for j in range(i+1,len(list1)):
            if list1[j] < list1[minIndex]:
                minIndex = j
        if minIndex != i:
            list1[i],list1[minIndex] = list1[minIndex],list1[i]
    return list1



list1 = [4,7,78,12,3,5,10,188]
print(selection_sort(list1))
