x=40
y=60.01
a=float(x+y)
print(a)

######
print(repr('Himanshu'))
print(str(('Himanshu')))
print(('Himanshu'))

#######
import math
g=math.floor(3.5) #3 takes you to the lower value
print(g)
math.trunc(2.8) #2 takes to towards 0

complex_num=3+4j
#octal number system
print(0o20)
#hexadecimal
print(0xFF)
#Binary
print(0b1000)
#print decimal rep
print(oct(64))
#print hex
print(hex(64))
#print binary
print(bin(20))

#Another way
a=int("1001",2) #int('Number is current sys',base of the system)
print(a)

#playing with random libraries in python
import random as rd 
print(rd.random()) #values from 0 to 1(1 not inc)
print(rd.randint(1,10))

l1=['Himanshu','Himu','BB']
print(rd.choice(l1))

rd.shuffle(l1)
print(l1)

#Decimal libraray in python
from decimal import Decimal as de
print(de('0.1')+de('0.2')+de('0.3'))

#For union intersection and other stuff
setone={1,2,3,4}
print(setone&{1,3}) #INTERSECTION
print(setone|{1,3})  #UNION
print(setone-{1,2,3,4}) 