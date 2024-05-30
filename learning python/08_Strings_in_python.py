s="Himanshu kumar jha"
print(s.count('i'))
s="89.823"
print(s.isalnum())
print(s.isdigit())
print(s.isdecimal())

Name="0123456789"
print(Name[:])
print(Name[0:5])     #slicing [begin,end)
print(Name[:-3])     #slicing last 3 elements
print(Name[0:9:3])   #[start,end),jump]

bane="sanchita     "
print(bane)
print(bane.replace("san","tii"))
print(bane)

chai="Lemon chai, masala chai, nigga chai"
print(chai.split(",")) #if you write it as chai.split() it will do it on basis of spaces

name="Himanshu Kumar Jha"
print(name.find("Kumar"))

frequncy="ha ha ha ha he he he he"
print(frequncy.count("ha"))

#FORMAT OPERATION
chai_type="Maslala"
quantity=2
order="I ordered {} cups of {} chai"
print(order.format(quantity,chai_type))

chai_variety=["Lemon","Masala","Ginger"]
print("".join(chai_variety))
print("->".join(chai_variety))

##CONFILICTING USE OF STRING
#like "He said "I am going to college ""
# how to avoid this string inside string conflict
# Here is how :
sentence="He said ,\"Masala chai is awsome\" "
print(sentence)

