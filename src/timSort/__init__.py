from binarySort import binary_sort

def tim_sort(arr: 'list', reverse: bool=False):
    ret = None
    if len(arr) <= 64:
        ret = binary_sort(arr, reverse=reverse)
    else:
        pass

    return ret
