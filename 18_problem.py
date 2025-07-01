#Q. Write a function to count how many times each charecter appears in string.
def chracter_str(string):
    char_count={}
    for char in string:
        if char in char_count :
            char_count[char] +=1
        else:
            char_count[char] =1
    return char_count
text="Hello python"
result=chracter_str(text)
print(result)