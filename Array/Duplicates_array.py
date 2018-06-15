def remove_duplicate(list1):
    new_list=[]
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    return new_list

if __name__=="__main__":
    list1=[5,3,5,2,10,23,10,14,16]
    print(remove_duplicate(list1))
