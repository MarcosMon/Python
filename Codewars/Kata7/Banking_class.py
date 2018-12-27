class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
        
    def withdraw(self, money_withdraw):
        if money_withdraw > self.balance:
            raise ValueError()
        self.money_withdraw = money_withdraw
        self.balance -= self.money_withdraw
        return self.name + " has " + str(self.balance) + "."
    
    def check(self, other, money):
        if not other.checking_account: raise ValueError()
        self.balance+= money
        other.balance-=money
        
        return  self.name + " has " + str(self.balance) + " and "   + other.name + " has " + str(other.balance) + "." 
    
    def add_cash(self, money_add ):
    
        self.balance+=money_add
        return self.name + " has " + str(self.balance) + "."


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)


if __name__ == '__main__':

    assert Jeff.withdraw(2) == 'Jeff has 68.'
    assert Joe.check(Jeff, 50) == 'Joe has 120 and Jeff has 18.'
    assert Jeff.check(Joe, 80) == 'Jeff has 98 and Joe has 40.'
    assert Jeff.add_cash(20) == 'Jeff has 118.'