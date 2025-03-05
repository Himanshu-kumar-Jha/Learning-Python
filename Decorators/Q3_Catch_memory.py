#Q3. Make a decorator which caches return value of function and returns ans from cache when called with same arguments, insted of rerunning the function
import time
def cache(func):
    cache_value={}
    print(cache_value)     #to check 
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper



def long_function(a,b):
    time.sleep(4)          #notice the time difference after executing two fucntions
    return a+b

print(long_function(3,4))
print(long_function(3,4))

