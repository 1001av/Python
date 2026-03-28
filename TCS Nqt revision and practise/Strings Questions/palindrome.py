# Check if a given string is palindrome or not. 

def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower() 
    
    # Check if the string is equal to its reverse
    return s == s[::-1] 

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False

