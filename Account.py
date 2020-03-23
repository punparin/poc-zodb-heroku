import persistent

class Account(persistent.Persistent):
    def __init__(self, name):
        self.name = name
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def cash(self, amount):
        assert amount < self.balance
        self.balance -= amount

    def toJson(self):
        return self.__dict__