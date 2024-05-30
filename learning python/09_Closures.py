#Closures in python are function which keep the refernce of pervious frunction In Python, a closure is a nested function that captures and remembers the values of variables from the outer (enclosing) scope, even after the outer function has finished executing. This allows the inner function to access those variables when it is called later.

#Example
def outer_function(num):
    def inner_function(x):
        return num**x
    return inner_function

x=outer_function(3)
print(x(2))