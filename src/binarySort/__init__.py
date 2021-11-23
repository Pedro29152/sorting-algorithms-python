def binary_sort(arr: 'list', reverse: bool=False):
    ret = [arr[0]] if arr else arr

    for i in range(1, len(arr)):
        ins = i
        if ret[i-1] > arr[i]:
            ins = binary_search(ret, arr[i], len(ret) - 1)
        ret = ret[0:ins] + [arr[i]] + ret[ins:]
    
    if reverse:
        ret.reverse()
    return ret

def binary_search(arr: 'list', element: int, end: int, start: int = 0):
    if end <= start:
        return start + 1 if element > arr[start] else start
    
    mid = (end + start) // 2

    if (element == arr[mid]):
        return mid + 1

    if (element > arr[mid]):
        return binary_search(
            arr, element,
            start=mid + 1, end=end
        )
    return binary_search(
        arr, element,
        start=start, end=mid - 1
    )
