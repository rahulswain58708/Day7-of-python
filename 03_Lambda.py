#Syntax:
square=lambda x: x*x
print(square(5))
#1. Example 
numbers=[2,4,5,7,3]
square=list(map(lambda x:x*x,numbers))
print(square)
#2.Example
sum=lambda x,y: x+y
print(sum(5,10))