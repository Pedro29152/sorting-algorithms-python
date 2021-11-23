from random import randint
import time, selectionSort, quickSort, insertSort, binarySort, mergeSort, util

if __name__ == '__main__':
    size = 500
    mult = 10

    list = [randint(0, size * mult) for i in range(size)]

    timers = []
    results = []
    
    # 1
    timers.append({})
    timers[len(timers) - 1]['start'] = time.time()
    results.append(selectionSort.select_sort(list.copy(), inplace=False))
    timers[len(timers) - 1]['stop'] = time.time()
    # 2
    timers.append({})
    timers[len(timers) - 1]['start'] = time.time()
    results.append(insertSort.insert_sort(list.copy(), inplace=False))
    timers[len(timers) - 1]['stop'] = time.time()
    # 3
    timers.append({})
    timers[len(timers) - 1]['start'] = time.time()
    results.append(binarySort.binary_sort(list.copy()))
    timers[len(timers) - 1]['stop'] = time.time()
    # 4
    timers.append({})
    timers[len(timers) - 1]['start'] = time.time()
    results.append(mergeSort.sort(list.copy()))
    timers[len(timers) - 1]['stop'] = time.time()
    # 5
    timers.append({})
    timers[len(timers) - 1]['start'] = time.time()
    results.append(mergeSort.threaded_sort(list.copy()))
    timers[len(timers) - 1]['stop'] = time.time()
    # 6
    timers.append({})
    timers[len(timers) - 1]['start'] = time.time()
    results.append(quickSort.quick_sort(list.copy(), inplace=False))
    timers[len(timers) - 1]['stop'] = time.time()

    for i, item in enumerate(results):
        if not util.check_sorted_list(item):
            raise ValueError(f'Somthing went wrong in the algorithm: {i + 1}')

    for i, item in enumerate(timers):
        print('algorithm ', i + 1)
        print(item['stop'] - item['start'])