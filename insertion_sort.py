def insertion_sort(array):
    for i in range(1,len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

if __name__ == "__main__":
    arr = [9,6,89,24,67]
    print(insertion_sort(arr))