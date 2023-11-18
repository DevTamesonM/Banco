class Main:
    pass

print("Testando ")

from cliente import Cliente

from conta import Conta

c1 = Cliente("Tameson", "44444-55555")
conta = Conta(c1.get_nome(), 3546)

conta.depositar(100)
conta.saque(50)
conta.extrato()




