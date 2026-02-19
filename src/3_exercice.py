def is_palindrome(string: str) -> bool:
    return list(reversed(string)) == list(string)


print(is_palindrome("radar"))
print(is_palindrome("hello"))
