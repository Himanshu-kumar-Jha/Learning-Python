'''
Immutable: The value of the object can't be changed once it is created.
Mutable: The value of the object can be changed once it is created.
if you copy a mutable object, and change the value of the copied object, the original object will also change.
to avoid this use copy.deepcopy() method

some mutable objects are:
1. List
2. Dictionary
3. Set
4. User-defined classes

some immutable objects are:
1. int
2. float    
3. decimal
4. complex
5. bool
6. string
'''
x=10
y=x
x=5
print(x)
print(y)

s="Himanshu"
s[0]='1' #throws eroor
print(s)