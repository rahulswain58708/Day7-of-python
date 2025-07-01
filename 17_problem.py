#Q.Write a function that takes a list of number and return a new list with only them even number.
def list_number(number):
    return [num for num in number if num%2==0]
number=[1,2,3,4,5,6]
even_number=list_number(number)
print(even_number)
