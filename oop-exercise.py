'''
class Calc:
    def sum(self, x, y):
        print(x+y)



c= Calc()
c.sum(10,20)



d= Calc()
d.sum(50,70)
'''

'''
class Calc:
    def __init__(self, name):
        print(f'welcome {name}')
    
    def sum(self, x, y):
        print(x+y)



        
class SciCalc(Calc):
    def pow(self, x, y):
        print(x**y)


c = SciCalc('Salar')
c.sum(10,20)
c.pow(2,3)
'''

'''
class A:
    def do(self):
        print('in a')

class B(A):
    pass

class C:
    def do(self):
        pfint('in c')

class D(B,C):
    pass


z= D()
z.do()
print(D.mro())
'''

class User:
    def __init__(self,name,age,gender):
        print(f" welcome {name}")
        self.balance= 0
        self.name = name
        self.age = age
        self.gender = gender

    def show_Details(self):
        print(f" name : {self.name}")
        print(f"age : {self.age}")
        print(f"gender : {self.gender}")

class Bank(User):
    def deposite(self,amount):
        self.balance += amount
        print(f"your current balance ist : {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print('you dont have enough balance')
            return
        
            self.balance -= amount
            print(f"your current balance ist : {self.balance}") 

    def show_balance(self):
         print(f"your current balance ist : {self.balance}")

    
         
u1 = Bank('Salar' , 22, 'male')        


u1.deposite(500)

u1.withdraw(700)

u1.show_balance()

u1.show_Details()








u1 = Bank('Issa' , 27, 'male')        


u1.deposite(5000)

u1.withdraw(700)
u1.withdraw(1000)
u1.show_balance()

u1.show_Details()





























































