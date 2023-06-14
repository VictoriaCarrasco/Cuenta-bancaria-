class CuentaBancaria:
    def __init__ (self, nombre, tasa_interes,balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        self.nombre = nombre


    def hacer_deposito(self, amount):
        self.balance += amount
        print ("Retiro realizado. Tu nuevo saldo es:", self.balance)
        return self

    def retiro(self, amount):
        if self.balance >= amount:
                self.balance -= amount 
        else: 
            print ("Fondos Insuficientes: Cobrando una tarifa de $5")
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print ("Nombre del usuario:", self.nombre)
        print ("Este es tu estado de cuenta. Balance: $", self.balance)
        return self 
        
    def mostrar_interes (self):
        print ("Nombre del usuario:", self.nombre)
        print ("Este es tu interes:", self.balance)
        return self 

    def generar_interes (self):
        if self.balance > 0: 
            interes= self.balance * self.tasa_interes
            self.balance = interes
        self.mostrar_interes
        return self 


#Cuentas bancarias. 
Usuario1 = CuentaBancaria ("Robert" , 0.01, 100)
Usuario2= CuentaBancaria ("Lyan", 0.01, 400)


Usuario1.hacer_deposito(200).hacer_deposito(100).hacer_deposito(300).retiro(500).mostrar_info_cuenta ().generar_interes().mostrar_interes ()

Usuario2.hacer_deposito(100).hacer_deposito(400).retiro(100).retiro(50).retiro(50).retiro(1000).mostrar_info_cuenta ().generar_interes().mostrar_interes ()

print ("___________________________________________")

#Metodo de clase para imprimir instancias de la informacion de una cuenta bancaria. 
class CuentaBancaria:
    cuentas_bancarias= []

    def __init__(self, titular, saldo): 
        self.titular = titular
        self.saldo = saldo
        CuentaBancaria.cuentas_bancarias.append(self)

    @classmethod
    def imprimir_cuenta(cls):
        for cuenta in cls.cuentas_bancarias: 
            print ("Titular:", cuenta.titular)
            print ("Saldo:", cuenta.saldo )

cuenta1 = CuentaBancaria("Donald", 200)
cuenta2= CuentaBancaria ("Mariano", 500)
CuentaBancaria.imprimir_cuenta()


