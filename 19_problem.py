#Q. Write a function that checks if a number is prime or not.
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5) + 1,2):
     if n%i==0:
        return False
    return True
print(is_prime(7))  #true