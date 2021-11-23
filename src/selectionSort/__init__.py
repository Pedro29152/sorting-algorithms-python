from util import get_high_low

def select_sort(arr: 'list', reverse: bool = False, inplace: bool = True):
    if not inplace:
        arr = arr.copy()
    
    for i in range(len(arr)):
        aux = arr[i]
        list = arr[i:]
        info = get_high_low(list)
        if reverse:
            arr[i] = info['high']
            arr[info['highPos'] + i] = aux
        else:
            arr[i] = info['low']
            arr[info['lowPos'] + i] = aux
    
    if not inplace:
        return arr
