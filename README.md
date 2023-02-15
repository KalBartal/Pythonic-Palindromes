# Problem Description

Given a string `s`, determine whether it is a palindrome or not using Python. A string is considered a palindrome if it reads the same backward as forward. For example, "racecar" is a palindrome, while "hello world" is not.

Your task is to implement a function `is_palindrome(s: str) -> bool` that takes in a string `s` and returns a boolean value indicating whether `s` is a palindrome or not. 

# Signature

```python
def is_palindrome(s: str) -> bool:
    pass
```

# Constraints

- The input string `s` consists only of printable ASCII characters. 
- The length of `s` is at most 1000. 

# Examples

## Input

```python
s = "racecar"
```

## Output 

```python
True
```

## Input

```python
s = "hello world"
```

## Output

```python
False
```

# Solution 

A possible solution to this problem is to remove all non-alphanumeric characters from the input string and convert it to lowercase. We can then check if the resulting string is equal to its reverse. This can be done using Python's slicing syntax, which allows us to reverse the string by using a step of -1.

```python
def is_palindrome(s: str) -> bool:
    # Remove all non-alphanumeric characters and convert to lowercase
    s = ''.join(c for c in s if c.isalnum()).lower()
    
    # Check if the resulting string is equal to its reverse
    return s == s[::-1]
```

Note that we use the `isalnum` method to check if a character is alphanumeric. This method returns `True` if the character is a letter or a digit, and `False` otherwise. This ensures that we only keep letters and digits in the resulting string, and ignore spaces, punctuation, and other non-alphanumeric characters.

This solution has a time complexity of O(n), where `n` is the length of the input string. This is because we only iterate over the string once to remove non-alphanumeric characters and compare it to its reverse. The space complexity is also O(n), because we create a new string that is the same length as the input string.