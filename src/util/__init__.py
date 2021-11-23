
def check_sorted_list(arr: 'list', reverse: bool = False):
    for i in range(1, len(arr)):
        if reverse:
            if arr[i-1] < arr[i]:
                return False
        else:
            if arr[i-1] > arr[i]:
                return False
    return True

def get_high_low(arr):
    low = None
    high = None
    highPos = None
    lowPos = None

    for i, v in enumerate(arr):
        atual = v
        if low == None:
            low = atual
            lowPos = i
        if high == None:
            high = atual
            highPos = i

        if atual < low:
            low = atual
            lowPos = i

        if atual > high:
            high = atual
            highPos = i
    
    return {'high': high, 'low': low, 'highPos': highPos, 'lowPos': lowPos}

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
