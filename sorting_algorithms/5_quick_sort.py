import numpy as np
from typing import List

def quick_sort(arr: List[int], left: int, right: int) -> None:
    if left < right:
        partision_pos = partition(arr, left, right)
        quick_sort(arr, left, partision_pos - 1)
        quick_sort(arr, partision_pos + 1, right)
    
def partition(arr: List[int], left: int, right: int) -> None: 
    i = left
    j = right - 1
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
            
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        
    return i
        
        

lst = np.random.permutation(np.arange(1, 20))
print("unsorted list: ", lst)
quick_sort(lst, 0, len(lst) - 1)
