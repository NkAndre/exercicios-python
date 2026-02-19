#Informar um saldo e imprimir o saldo com reajuste de 1%.
saldo = float(input("Insira o seu Saldo Atual : "))

#  Multiplicar por 1.01 (que representa 101%)
saldoReajustado = saldo * 1.01

#Exibindo
print(f"Saldo Reajustado : {saldoReajustado:.2f} ")