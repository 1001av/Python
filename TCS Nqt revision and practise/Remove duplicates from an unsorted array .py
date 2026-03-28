# Remove duplicates from an unsorted array 

arr = [4, 2, 1, 2, 3, 4]
result = []

for i in arr:
    if i not in result:
        result.append(i)

print("Array without duplicates:", result)