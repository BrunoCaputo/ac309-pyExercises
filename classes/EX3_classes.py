class Conta:
    def __init__(self):
        self.__number = ""
        self.__accOwner = ""
        self.__balance = 0.0
    def verSaldo(self):
        return self.__balance
    def sacar(self, val):
        if self.__balance - val < 0:
            return -1
        self.__balance -= val;
        return self.__balance
    def depositar(self, val):
        self.__balance += val
        return self.__balance
    def transferir(self, dest, val):
        if self.sacar(val) == -1:
            return -1
        dest.depositar(val)
        return 1
    def getNum(self):
        return self.__number
    def setNum(self, num):
        self.__number = num
    def getAccOwner(self):
        return self.__accOwner
    def setAccOwner(self, name):
        self.__accOwner = name
    def setBalance(self, val):
        self.__balance = val

acc1 = Conta()
acc2 = Conta()

# Conta 1
acc1.setNum("1111-1")
acc1.setAccOwner("Bruno")
acc1.setBalance(500.0)

# Conta 2
acc2.setNum("2222-2")
acc2.setAccOwner("Bruno 2")
acc2.setBalance(1000.0)

# Verificar saldo
print(
    "Saldo da conta de %s: R$%0.2f"
    %(acc1.getAccOwner(), acc1.verSaldo())
)
print(
    "Saldo da conta de %s: R$%0.2f"
    %(acc2.getAccOwner(), acc2.verSaldo())
)

# Depositar
dep1 = float(input("Quanto deseja depositar? "))
print(
    "Depósito de R$%0.2f na conta de %s. Novo saldo: R$%0.2f"
    %(dep1, acc1.getAccOwner(), acc1.depositar(dep1))
)
dep2 = float(input("Quanto deseja depositar? "))
print(
    "Depósito de R$%0.2f na conta de %s. Novo saldo: R$%0.2f"
    %(dep2, acc2.getAccOwner(), acc2.depositar(dep2))
)

# Sacar
wit1 = float(input("Quanto deseja sacar? "))
newBal = acc1.sacar(wit1)
if newBal == -1:
    print("Saldo insuficiente!")
else:
    print(
        "Saque de R$%0.2f na conta de %s. Novo saldo: R$%0.2f"
        %(wit1, acc1.getAccOwner(), newBal)
    )

wit2 = float(input("Quanto deseja sacar? "))
newBal = acc2.sacar(wit2)
if newBal == -1:
    print("Saldo insuficiente!")
else:
    print(
        "Saque de R$%0.2f na conta de %s. Novo saldo: R$%0.2f"
        %(wit2, acc2.getAccOwner(), newBal)
    )

# Transferir
transfer = float(input("Quanto deseja transferir? "))
transfer = acc1.transferir(acc2, transfer)
if transfer == -1:
    print("Saldo insuficiente na conta %s" %acc1.getNum())
else:
    print(
        "Transferêcia feita!\nOrigem: %s - %s. Novo saldo: R$%0.2f\nDestino: %s - %s. Novo saldo: R$%0.2f"
        %(acc1.getNum(), acc1.getAccOwner(), acc1.verSaldo(), acc2.getNum(), acc2.getAccOwner(), acc2.verSaldo())
    )