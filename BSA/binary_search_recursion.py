from typing import List

def binary_search(arr: List[int], target: int, low: int, high: int) -> int:
    mid = (high + low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)
        
def main() -> None:
    arr = [1, 2, 5, 7, 10, 11]
    target = 10
    x = binary_search(arr, target, 0, len(arr) - 1)
    print(x)
    
if __name__ == "__main__":
    main()