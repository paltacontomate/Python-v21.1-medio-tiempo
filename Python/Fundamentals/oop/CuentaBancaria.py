class CuentaBancaria:
    def __init__(self, tasa_interes, balance, name): 
        self.name= name
        self.balance = balance
        self.tasa_interes = tasa_interes

    def deposito_cash(self, amount):

        self.balance += amount
        return self
    
    def retiro_cash(self, amount):
        self.balance -= amount
        return self

    def tasa_inter(self):
        self.balance += self.balance * self.tasa_interes
        return self

    def mostrar_info_cuenta(self):
        print(f"CuentaBancaria: {self.name}-- balance: {self.balance}, Intereses: {self.tasa_interes}")
        return self
    

Aaron = CuentaBancaria(tasa_interes=0.2,balance=2000,name="Aaron")
Lukas = CuentaBancaria(tasa_interes=0.2,balance=1000,name="Lukas")

Aaron.deposito_cash(200).deposito_cash(2000).deposito_cash(2000).retiro_cash(500).tasa_inter().mostrar_info_cuenta()
Lukas.deposito_cash(5000).deposito_cash(2000).tasa_inter().mostrar_info_cuenta()

#Todos los Derechos Reservados a "by:elian"®