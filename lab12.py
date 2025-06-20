'''class Animal:
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        print("meow")
class Dog(Animal):
    def sound(self):
        print("woof")
def make_sound(Animal):
    Animal.sound()
cat=Cat()
dog=Dog()
make_sound(cat)
make_sound(dog)'''

'''class Shape:
    def __init__(self,color):
        self.color=color
        pass
class Circle(Shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,color,width,height):
        super().__init__(color)
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
circle=Circle("red",5)
rectangle=Rectangle("blue",4,6)
print("circle area:",circle.area())
print("rectangle area:",rectangle.area())'''

'''class Myclass:
    def __init__(self):
        self.public_attribute="i'm a public attribute"
        self._protected_attribute="i'm a protected attribute"
        self.__private_attribute="i'm a private attribute"
    def public_method(self):
        print("i'm a public method")
    def _protected_method(self):
        print("i'm a protected method")
    def __private_method(self):
        print("i'm a private method")
obj=Myclass()
print(obj.public_attribute)
obj.public_method()
print(obj._protected_attribute)
obj._protected_method()
print(obj._Myclass__private_attribute)
obj._Myclass__private_method()'''

class Bankaccount:
    def __init__(self,account_number,balance):
        self._account_number=account_number
        self._balance=balance
    def get_account_number(self):
        return self._balance
    def get_balance(self):
        return self._balance
    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print("deposit successful.")
        else:
            print("invalid amount for deposit.")
    def withdraw(self,amount):
        if amount>0 and amount<=self._balance:
            self._balance-=amount
            print("withdrawal successful.")
        else:
            print("insufficient funds or invalid amount for withdrawal.")
account=Bankaccount("1234567890",1000)
print("account number:",account.get_account_number())
print("balance:",account.get_balance())
account.deposit(500)
account.withdraw(200)
account._account_number="9876543210"
account._balance=5000
print("account number:",account.get_account_number())
print("balance:",account.get_balance())



