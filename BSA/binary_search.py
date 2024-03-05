target = 15
lst = [1, 2, 2, 2, 4, 5, 5, 6, 8, 9, 10, 10, 11, 12, 13, 13, 16, 17, 18, 19]

def find_num(lst, target):
    start, end = 0, len(lst) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return f"Founded num {target} at {mid} index"
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return "unfortunatly there are no such num"

print(find_num(lst, target))