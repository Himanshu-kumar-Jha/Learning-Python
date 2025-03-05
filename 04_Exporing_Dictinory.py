# Dictionary in python
#->Mutable
#->ordered
#->No duplicates

My_dic={
    "Name":"Himanshu",
    "Age":21,
    "YOB":2002
}

x=My_dic["YOB"]  # to access the key
# or
x=My_dic.get("YOB")
#Check if key is present or not
if "Age" in My_dic:
    print("yes")

My_dic["Name"]="BB"

#To insert a new key value pair
My_dic.update({"State":"Delhi"})
# to remove a key
My_dic.pop("YOB")
#To store all of keys and values 
#MY_dic.keys() and MY_dic.values()

#To copy a dictnory we should not do dict1=dict2 coz it makes shallow copy we should use dict1=dict2.copy()->for deep copy

#Iteration through loop for key and values pair
for x, y in My_dic.items():
    print(x,y)

#Dictinory inside dictinory
tea_shop={
    "chai":{"Masala":"spicy","Ginger":"Zesty"},
    "Tea":{"Green":"Mild","Black":"Strong"}
}
print(tea_shop["chai"])
print(tea_shop["chai"]["Masala"])