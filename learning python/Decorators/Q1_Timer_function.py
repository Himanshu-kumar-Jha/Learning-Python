#Decoratoes in python  are like toll booth on highway , you have to pass through them before going on actual highway
#same way function has to pass through another function before excuting , a decorator can we writeen aboue the function as @function_name(from which you want to pass the below function).

#Boiler plate of  decorator
'''
def Decorator_name(function):                 #name of decorator function which accepts the function.
    def warapper_function(*args,**kwargs):    #wrapper function in which code is execuited.
        execute_function=func(agrumnets)      #execuite the original passed function.
        return execute_function               #return it's result.
    return warapper_function                  #return wrapper for decorator.

@Decorator_name
def function(a, b):
    #some logic 
    return a;
'''
#Problem 1 Timing function execution ->write a decorator which mesures the time of execution of function

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start}")
        return result
    return wrapper

@timer
def example_func(n):
    time.sleep(n)

example_func(2)





