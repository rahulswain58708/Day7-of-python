#Q.Write a function to check whether number is even or odd
def check_number(number):
    if number%2==0:
        return f"{number} is even"
    else:
        return f"{number} is odd"
print(check_number(8))