# Find the second smallest and second largest element in an array

def find_second_smallest_largest(arr):
    if len(arr) < 2:
        return None, None  # Not enough elements for second smallest/largest

    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')

    for num in arr:
        # Update smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

        # Update largest and second largest
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    # Handle cases where second smallest/largest doesn't exist
    if second_smallest == float('inf'):
        second_smallest = None
    if second_largest == float('-inf'):
        second_largest = None

    return second_smallest, second_largest


# Example usage
arr = [10, 5, 20, 8, 15]
second_smallest, second_largest = find_second_smallest_largest(arr)

print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)