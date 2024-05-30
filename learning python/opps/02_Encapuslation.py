#make bard data member private and make a getter function to access it
#to make a datameber private we need to use __datamemname
class Car:
    def __init__(self,Brand,Model):#Constructor    self i slike this in cpp
        self.__Brand=Brand           #Data members can be written as this
        self.Model=Model
    def Full_name(self):
        print(self.__Brand)
        print(" ",self.Model)
    
    def Getter(self):
        return self.__Brand

'''
class EV(Car):
    def __init__(self,Brand,Model,Battery_size):
        super().__init__(__Brand,Model)              #super keyword gives access to class above and we can access it's methods
        self.Battery_size=Battery_size
    
    def Full_info(self):
        return f"{self.__Brand} {self.Model} {self.Battery_size}"

My_EV=EV("Tata","Nexon","500KW")
print(My_EV.Full_info())
My_EV.Full_name() #accessing a method from car class
'''
my_car=Car("Audi","A7")
print(my_car.Getter())
print(my_car.Model)