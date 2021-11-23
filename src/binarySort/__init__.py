from util import binary_search

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
