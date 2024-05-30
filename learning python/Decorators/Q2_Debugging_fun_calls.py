#Q2 Create a decorator to print the function name and values of it's argumnets everytime the function is called .
#decorator function 

def Debug(func):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(arg) for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k , v in kwargs.items())
        print(f"calling function {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper

@Debug
def Greet(name,Greeting="Namaste ji"):
    print(f"{name} {Greeting}")

Greet("Himanshu"," Hello")