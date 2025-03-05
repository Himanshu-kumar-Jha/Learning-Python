import math
def check_prime(number):
    if(number<=1):
        return False
    else:
        for i in range(2,number):
            if((number%i)==0):
                return False
    
    return True


print(check_prime(6))

def summm(num1,num2):
    return num1+num2

def Multiply(num1,num2):
    return num1*num2

print(Multiply("a",5))  #this can handle both strings and integers

def area_circum(radius):
    area=round(math.pi*radius**2,3)
    circum=round(math.pi*radius*2,3)
    return area,circum

print(area_circum(5))

def greetUser(name="Himanshu"):
    print("hello",name)

print(greetUser())

#Lambda function , we use this if we have to use a function only once we see it's more use in django and mongo db
#cube of a number 
cube =lambda x:x**3
print(cube(3))

# *args type of function suppose we want to write a function which can take n number of agrumnets and we want to return their sum
def sum_all(*args):
    print(*args)
    for i in args:
        print(i*2)
    return sum(args)


print((sum_all(1,2,3,4,5)))

#write a function which takes any nuumber of argumnets and prints them in format of key : value
#we use *kwargs
def print_kwargs(name="Himanshu",age=20):
    print("name ",name," age ",age)

print_kwargs(age=40,name="geeta")
#but I can't print print_kwargs(name="smkm",age=39,weight=90)
# to solve this we use kwargs
def real_Kwargs(**kwargs):
    for key ,value in kwargs.items():
        print(f"{key}:{value}")

real_Kwargs(name="dbjn",age=39,wight=28,rf=0.5)

#Output using yeild keyword 
#what it does is : it remebers the point till which program has reached and remembers the state.
#for eg if we want to write a function which prints all the even numbers in a range , let's see
def even_nums(number):
    for i in range(2,number,2):
        print(i)

even_nums(12)






