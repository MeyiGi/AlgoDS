from typing import List

def interpolation_search(arr: List[int], key: int, low: int, high: int) -> int:
    if low > high:
        return -1
    
    pos = low + ((high - low) * (key - arr[low])) // (arr[high] - arr[low])
    if arr[pos] == key:
        return pos
    elif arr[pos] > key:
        high = pos - 1
    else:
        low = pos + 1
        
    return interpolation_search(arr, key, low, high)

def main() -> None:
    x = [1, 2, 3, 4 , 5, 6, 9, 11, 22, 100, 2503]
    y = interpolation_search(x, 22, 0, len(x) - 1)
    print(y)
    
if __name__ == "__main__":
    main()