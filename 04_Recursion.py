#1.Example Factorial using Recursion.
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(4))
#2.sum of digits using recursion.
def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
print(sum_of_digits(1234))
