
def pivot(arr: 'list', low: 'int', high: 'int'):
    m = low
    for i in range(low, high):
        if arr[i] < arr[high]:
            arr[m], arr[i] = arr[i], arr[m]
            m += 1
    arr[m], arr[high] = arr[high], arr[m]
    return m

def quick_sort(arr: 'list', low: 'int' = 0, high: 'int' = None, inplace: bool = True):
    if not inplace:
        arr = arr.copy()

    if high == None:
        high = len(arr) - 1
    
    if len(arr) <= 1:
        return arr
    if low < high:
        piv = pivot(arr, low, high)

        quick_sort(arr, low, piv-1)
        quick_sort(arr, piv+1, high)

    if not inplace:
        return arr
