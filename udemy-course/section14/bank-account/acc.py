#!/usr/bin/python3.5
import sys

# create class
class Account():

    def __init__(self, filepath):
        # instance variables
        self.path = filepath
        with open(filepath, 'r') as f:
            self.balance = int(f.read())

    def commit(self):
        with open(self.path, 'w') as f:
            f.write(str(self.balance))

    def withdraw(self, val):
        self.balance -= val
        self.commit()

    def deposit(self, val):
        self.balance += val
        self.commit()

path = sys.path[0]+'/'
file = 'balance.txt'
# object instance
acc = Account(path+file)
# acc.withdraw(500)
# acc.deposit(2000)
# print(acc.balance)

# inheritance class
class CheckingAcc(Account):
    # Doc string
    """ Explaination of an object"""
    # class variable and it is a data member
    type = 'checking'

    # constructor and it is a method(special)
    def __init__(self, filepath, fee):
        super().__init__(filepath)
        # instance variables and it is a data member
        self.fee = fee

    # class method
    def transfer(self, val):
        self.balance -= val + self.fee


file = 'jack.txt'

# instantiation of a class ro get object instance
jack_chacc = CheckingAcc(path+file, 10)
# chacc.deposit(1000)
# jack_chacc.transfer(500)
# jack_chacc.commit()

# accecing to attributes
print(jack_chacc.balance)
print(jack_chacc.type)

# Print doc string
print(jack_chacc.__doc__)

file = 'john.txt'
john_chacc = CheckingAcc(path+file, 10)
# chacc.deposit(1000)
# chacc.transfer(500)
# chacc.commit()
print(john_chacc.balance)
print(john_chacc.type)