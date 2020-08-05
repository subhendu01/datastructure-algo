def bubble_sort(list_val):
    l = len(list_val)
    for i in range(l-1):
        flag =0;
        for j in range(l-1):
            if list_val[j] > list_val[j+1]:
                temp = list_val[j]
                list_val[j] = list_val[j+1]
                list_val[j+1] = temp
                flag = 1
        if flag == 0:
            break
    return list_val
if __name__=='__main__':
    lst = [99,198,23,56,77,7]
    print(bubble_sort(lst))
