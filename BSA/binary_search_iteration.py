from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """Binary search on sorted array"""
    if not arr:
        return
    
    left: int = 0
    right: int = len(arr) - 1
    
    while left <= right:
        mid: int = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def main() -> None:
    """Main function"""
    target: int = 13
    lst: List[int] = [1, 2, 2, 2, 4, 5, 5, 6, 8, 9, 10, 10, 11, 12, 13, 13, 16, 17, 18, 19]
    print(binary_search(lst, target))
    
if __name__ == "__main__":
    main()
