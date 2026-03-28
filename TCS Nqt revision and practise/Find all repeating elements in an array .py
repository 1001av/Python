# Find all repeating elements in an array 

def find_repeating(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


arr = [1, 2, 3, 1, 3, 6, 6]
print("Repeating elements:", find_repeating(arr))