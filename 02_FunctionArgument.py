#1.position Argument
def add(a,b):
    return a+b
print(add(5,3))#output:-8
#2.Deafult Argument
def greet(name="Guest"):
    return f"Hello, {name}"
print(greet())
#3.keyword Argument
def student(name,age):
    print(f"{name},age:{age}")
student(name="Rahul",age=18)