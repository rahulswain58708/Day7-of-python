#Q. Write a function that returns the Fibonacci series up to n terms
def fibonacci_series(n):
    series=[]
    a,b=0,1
    for _ in range(n):
        series.append(a)
        a,b=b,a+b
    return series
print(fibonacci_series(9))