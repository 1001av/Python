import os

# Specify the directory path (use '.' for current directory)
directory = "C:/Users/AKHIL/Desktop"

# Get list of contents
contents = os.listdir(directory)

print(f"Contents of {directory}:")
for item in contents:
    print(item)
