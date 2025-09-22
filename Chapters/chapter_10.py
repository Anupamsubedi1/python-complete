class Programmer:
    name = None
    age = 0
    work = None
    salary = 0.0

    def greet_each_coder(self):
        print(f"Hello  Coder ,{self.name} welcome to the world of programming")

p1 = Programmer()
p1.name = "Anupam"
p1.age = 24
p1.work = "Programmer"
p1.salary = 250000.0
p1.greet_each_coder()
print(p1.name)    # None
print(p1.salary)  # 0.0

class programmer:
    name=""
    age=0   
    work=""
    salary=0
    def __init__(self,name , age,work, salary):
        self.name =name
        self.age=age
        self.work=work
        self.salary=salary
    
programmer1=programmer("Anupam",24,"Programmer",25000)
progammer2 =programmer("Rohan",22,"Programmer",20000)
programmer3=programmer("Sohan",23,"Programmer",22000)
programmer4=programmer("Mohan",25,"Programmer",28000)
programmer5=programmer("Sourav",26,"Programmer",35000)
programmer1.salary=30000
print(programmer1.name)
print(programmer1.age)  
print(programmer1.work)
print(programmer1.salary)


class calculator:
    num1=0
    num2=0
    
    def sum(self):
        print(self.num1+self.num2)
    
    def mul(self):
        print(self.num1*self.num2)
    
    def sub(self):
        print(self.num1-self.num2)
    
    def div(self):
        print(self.num1/self.num2)
    
calculator1=calculator()
calculator1.num1=20 
calculator1.num2=10
calculator1.sum()
calculator1.mul()
calculator1.sub()

calculator1.div()

import random

class train:
        def __init__(self,trainno):
            self.trainno =trainno

        def getflare(self,fro , to):
            print(f"the flare is {random.randint(555,1000)}...{fro} ...{to}")
        
        def ticketstatus(self):
            print(f"the {self.trainno} is on the way")

        def bookticket(self,seatno,fro,to):
            print(f"{seatno} is booked , of the train {self.trainno} going from {fro} to {to}")


obj1 = train(112)
obj1.bookticket("3a", "paris","madrid")
obj1.ticketstatus()
obj1.getflare("paris","madrid")
