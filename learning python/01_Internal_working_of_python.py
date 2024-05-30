#####Garbage collection in python
#2 ways -> 1. Reference count , 2.Grabage collection

#1.Reference count 
'''
It keeps track of number of times an object has been reffred . once the refernce count reaches zreo it means that, the object's memory needs to be de allocated

import sys
sys.getrefcount()

'''
import sys
x=10
print(sys.getrefcount(x))
x=11
print(sys.getrefcount(x))

#In the above we observed that we are getting large numbers , it's due to python's optimisation techniques
l1=[1,2,3]
l2=l1
l2=[1,2,3]
print(id(l1))
print(id(l2))


