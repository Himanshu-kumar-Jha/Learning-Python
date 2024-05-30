import copy
##################Lists in python##########
#->Lists are mutable and dynamic->[list]
#They can also contain duplicates
My_list=[1,2,3,'Himanshu',True]

####Methods in Lists

#1.append ->to insert ele at end of the list
My_list.append(23)
print(My_list)

#2.Copy , shallow and deep copy in python
##Shallow copy 
New_list=[1,2,3,4,5,6]
My_list_shallow=copy.copy(New_list)
print(id(My_list))
print(id(My_list_shallow))
New_list[3]='Fffff' 
print(My_list_shallow[3])
print(New_list[3])

##Deep copy
New_deep=[5,3,5,6,8]
check_deep=copy.deepcopy(New_deep)
New_deep[1]=99
print(New_deep[1])
print(check_deep[1])

#3. Clear operation
#clear any list by listname.clear()
#to delete element from a particular position
#use del method
del New_deep[1]

##about pop ->it removes and it can also return a value

#4. inset method ->my_list(pos,ele)->to insert ele at a particular pos

#5. sort a list 
Numbers=[1,2,3,4,5,6]
Numbers.sort()  #for inc order
Numbers.sort(reverse=True) #for dec order
print(Numbers)

#Slicing with lists
Slice=[0,1,2,3,4,5,6]
print(Slice[0:3])    # last number not included
print(Slice[:-1])    #to print everything expect the last element
print(Slice[2:])

#Inserting operations
Slice[1:3]=["Green","Tea"]
print(Slice)

#For loop
for i in Slice:
    print(i,end='->')
    if(i==4) :print("LOOL")

