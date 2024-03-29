from typing import List

def interpolation_search(arr: List[int], key: int) -> int:
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        pos = low + ((high - low) * (key - arr[low])) // (arr[high] - arr[low])
        if arr[pos] == key:
            return pos
        elif arr[pos] > key:
            high = pos - 1
        else:
            low = pos + 1
            
    return -1

def main() -> None:
    x = [1, 2, 3, 4 , 5, 6, 9, 11, 22, 100, 2503]
    y = interpolation_search(x, 22)
    print(y)
    
if __name__ == "__main__":
    main()