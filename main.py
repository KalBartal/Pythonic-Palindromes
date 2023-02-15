def is_palindrome(s: str) -> bool:
    # Remove all non-alphanumeric characters and convert to lowercase
    s = ''.join(c for c in s if c.isalnum()).lower()
    
    # Check if the resulting string is equal to its reverse
    return s == s[::-1]

def test_is_palindrome():
    # Test a single-word palindrome
    assert is_palindrome("racecar") == True

    # Test a single-word non-palindrome
    assert is_palindrome("hello") == False

    # Test a multi-word palindrome with spaces and punctuation
    assert is_palindrome("A man, a plan, a canal, Panama!") == True

    # Test a multi-word non-palindrome with spaces and punctuation
    assert is_palindrome("Was it a car or a cat I saw?") == True

    # Test an empty string
    assert is_palindrome("") == True

    # Test a string with a single character
    assert is_palindrome("a") == True

    # Test a string with only non-alphanumeric characters
    assert is_palindrome(".,;:!@#") == True

    # Test a string with only spaces
    assert is_palindrome("   ") == True

test_is_palindrome()
