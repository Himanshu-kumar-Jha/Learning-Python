#############Tuples##########
#->Immutable ->()
#Can contain duplicates
import copy
my_Tuple=(1,2,3,'Himanshu',True)
print(len(my_Tuple))

##METHODS
#count(ele) ->returns freq of ele
Test_tuple=(1,2,3,4,3,2,5,6,5)
print(Test_tuple.count(2))
#index(ele,st(op),end(op))->returns first occ of ele
print(Test_tuple.index(5))
#max , min ===max(tuplename)

##Reverse a tuple
my_tup=Test_tuple[::-1]
print(my_tup)

##accessing last element
print(Test_tuple[-1])

##clearing a tuple
my_Tuple=my_Tuple*0
print(my_Tuple)

#Two tuples can be added 
Tuple1=(1,2,3,"Himanshu")
Tuple2=("Golu",5,6,7)
print(Tuple1+Tuple2)

