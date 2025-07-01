# Write a function to return the factorial number.
def factorial_number(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial_number(number-1)
print(factorial_number(5))
