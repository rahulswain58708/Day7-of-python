x=10 #Global scope
def my_func():
    x=5 #Local Scope
    print(x)
my_func()
print(x) 
# using the global Keyword:-To modify a global variable inside function,using the global keyword.
x=50 #global scope(variable)
def modify_global():
    global x
    x=100   #modify the global
modify_global()
print(x) #output:-100

