# Parent Class:

class User():  
    
    def __init__(self,name,age,gender): #Initializer
        self.name = name # self assigns a property or function
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Personal Details ")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)


#x = User('Karan', 22, 'Male')
#x.show_details()

# Child Class:

class Bank(User):
    
    def __init__(self,name,age,gender):
        self.name = name # Here we can also use 'super' function --> super().__init__(name,age,gender)
        self.age = age
        self.gender = gender
        self.balance = 0
        
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account Balance has been updated : Rs. ", self.balance)
    
    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Balance, Balance Available : Rs. ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account Balance has been updated : Rs. ", self.balance)
    
    def view_balance(self):
        self.show_details()
        print("Account Balance has been updated : Rs. ", self.balance)
        

x = Bank('Karan', 22, 'Male')
x.deposit(500)
x.withdraw(400)
x.withdraw(50)
x.withdraw(1000)
x.view_balance()
        
#x.name
