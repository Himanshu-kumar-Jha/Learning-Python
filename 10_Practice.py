#Q1. age categorition
'''
print("Enter Age")
s = int(input())  # Convert input to integer

if (s > 12 and s<60):
    print("Adult")
elif (s > 60):
    print("Senior Citizen")
else:
    print("Child")
'''
#Q2.Movie ticket pricing 
'''
age=int(input("My age is "))
day="Tuesday"
total=0
if(age<=12 and day=="Wednesday"):
    total=(8-2)
elif(age>12 and day=="Wednesday"):
    total=(12-2)

else:
    if(age>=12):
        total=12
    elif (age<12):
        total=8
print(total)
'''
#Q3 weather activities I will be using a dictinory
'''
My_dict={
    "Summer":"Take a bath ",
    "Winter":"Eat hot soup ",
    "Rainy":"Pakroe khao "
}
season=(input("The season is "))
if(season=="Summer"):
    print(My_dict.get(season))

elif(season=="Winter"):
    print(My_dict.get(season))

else:
    print(My_dict.get(season))

#Q4 check leap year
Year=1243
'''
'''
#Count positive numbers
List=[1,-2,4,6,-8,-9,10]
positive_numbers=0
for i in List:
    if(i>0):
        positive_numbers+=1
print(positive_numbers)
positive_numbers=0
for i in range(0,len(List)):
    if(List[i]%2==0):
        positive_numbers+=List[i]
print(positive_numbers)
'''
'''
#Multiplication table but skip the fifth iteration
N=3
for i in range(0,11):
    print(N,"*",i," = ",N*i)
'''
'''
#Reverse a string using two pointers
S="HIMANSHU"
K=""
for i in range(len(S)-1,-1,-1):
    K+=S[i]
print(K)
'''
''' 
#Word that occurs once
Name="iyer venkatr"
for i in Name:
    if(Name.count(i)==1):
        print(i)
'''
#Factorial calculator
def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)


print(fact(5))

#factorial using dp
def fact_dp(n):
    List=[0]*(n+1)
    List[0]=1
    for i in range(1,n+1):
        List[i]=i*List[i-1]
    
    return List[n]

print(fact_dp(5))

#Keep asking the user to enter a number b/w 1 to 10 untill he eneters
'''
while True:
    N=int(input("Enter Number saaar"))

    if(N>0 and N<10):
        break
    else:
        print("Good saaar")
    '''
#Check prime number saaar
import math
def check_prime(n):
    if(n<=1):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                return False

    
    return True

print(check_prime(6))
#check uniquness 
List_Name=["Orange","Bnanan","Papaya","Orange"]
My_set=set()
for i in List_Name:
    if(i in My_set):
        print("Duplicate: ",i)
        break
    My_set.add(i)
# Retries wait time exopentaion
import time
wait_time=1
max_attempts=5
attempts=0

while (attempts<max_attempts):
    print("Attempts ",attempts+1," wait time is ",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1









