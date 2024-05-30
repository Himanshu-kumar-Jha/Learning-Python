'''
Immutable
In Python, objects are categorized into two main types based on their mutability: immutable and mutable.

Immutable Objects:
Immutable objects are those whose state cannot be changed after they are created. Once created, any attempt to modify their state will result in the creation of a new object. Examples of immutable objects in Python include integers, floats, strings, tuples, and frozensets. 
'''

'''
Mutable Objects
Mutable objects, on the other hand, can be modified after creation. Lists, dictionaries, and sets are examples of mutable objects.

Lists: Lists can have elements added, removed, or modified after creation. For example, my_list = [1, 2, 3] allows you to modify my_list by appending elements, changing existing elements, or removing elements.
Dictionaries: Dictionaries allow you to add, remove, or modify key-value pairs after creation.
Sets: Sets are mutable unordered collections of unique elements. You can add or remove elements from a set after creation.
'''
x=10
y=x
x=5
print(x)  
print(y)  #pointing to another block of memory


s="Himanshu"
s[0]='1' #throws eroor because strings are immutable
print(s)
