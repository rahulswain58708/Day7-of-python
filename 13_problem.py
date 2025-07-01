#Q.write a function to check if a string is a palindrome.
def palindrome_str(text):
    if text==text[::-1]:
        return f"{text} is palindrome"
    else:
        return f"{text} is not palindrome"
print(palindrome_str("madam"))