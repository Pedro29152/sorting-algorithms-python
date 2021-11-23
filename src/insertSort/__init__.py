
def insert_sort(arr: 'list', reverse: bool = False, inplace: bool = True):
    if not inplace:
        arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        if reverse:
            while j >=0 and key > arr[j] :
                    arr[j+1] = arr[j]
                    j -= 1
        else:
            while j >=0 and key < arr[j] :
                    arr[j+1] = arr[j]
                    j -= 1
        arr[j+1] = key

    if not inplace:
        return arr
