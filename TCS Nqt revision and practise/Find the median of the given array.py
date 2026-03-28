# Find the median of the given array

def find_median(arr):
    n = len(arr)
    
    if n == 0:
        return None

    arr.sort()  # Step 1: Sort

    mid = n // 2 

    # Odd length
    if n % 2 != 0:
        return arr[mid]
    
    # Even length
    else:
        return (arr[mid - 1] + arr[mid]) / 2


# Example
arr = [7, 1, 3, 4, 5, 6, 2]
print("Median:", find_median(arr))