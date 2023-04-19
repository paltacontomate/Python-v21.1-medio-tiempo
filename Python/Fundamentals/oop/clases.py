class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
        

    def deposito_cash(self, amount):
        self.amount += amount
        return self

    def retiro_cash(self,amount):
        self.amount -= amount
        return self

    def acc_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.acc_balance()
        user.acc_balance()
        return self


aaron = User("aaron")
lukas = User("lukas")
mauricio = User("mauricio")


aaron.deposito_cash(100).make_deposit(200).make_deposit(50).retiro_cash(45).acc_balance()

lukas.deposito_cash(1000).make_deposit(1000).retiro_cash(500).retiro_cash(300).acc_balance()

mauricio.deposito_cash(1500).retiro_cash(1000).retiro_cash(5000).retiro_cash(3000).acc_balance()

