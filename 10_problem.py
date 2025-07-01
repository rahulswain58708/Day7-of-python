#Q.Write a function that returns the largest of Three number.
def number():
    numb1=int(input("Enter First number : "))
    numb2=int(input("Enter Second number : "))
    numb3=int(input("Enter third number : "))
    if numb1>numb2 and numb1>numb3:
        return numb1
    elif numb2>numb1 and numb2>numb3:
        return numb2
    else:
       return numb3
largest=number()
print(f'The largest number is {largest}')