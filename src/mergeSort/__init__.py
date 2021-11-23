from concurrent.futures import ThreadPoolExecutor, as_completed
import os

def merge(l: 'list', r: 'list'):
    ret = []
    if not l:
        return r
    elif not r:
        return l
    while(True):
        if l[0] > r[0]:
            ret.append(r.pop(0))
        else:
            ret.append(l.pop(0))
        
        if len(l) == 0:
            return ret + r
        elif len(r) == 0:
            return ret + l

def sort(arr: 'list'):
    size = len(arr)
    if size > 2:
        m = size//2
        l = sort(arr[0:m])
        r = sort(arr[m:])

        return merge(l, r)
    elif size == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
    return arr

def threaded_sort(arr: 'list'):
    nthreads = os.cpu_count()
    listSize = len(arr)

    if listSize < nthreads:
        return sort(arr)

    execList = []

    for i in range(nthreads):
        start = (i * (listSize // nthreads))
        end = start + (listSize // nthreads)
        execList.append(arr[start:end])
    if end < listSize:
        execList[-1] += arr[end:]

    with ThreadPoolExecutor(max_workers=nthreads) as threads:
        execs = []
        for l in execList:
            execs.append(threads.submit(sort, arr=l))
            
        ret = []
        for res in as_completed(execs):
            ret = merge(ret, res.result())
        return ret
