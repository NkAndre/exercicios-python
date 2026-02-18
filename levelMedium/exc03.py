# Escrever um algoritmo que lê:- a porcentagem do IPI a ser acrescido no valor das peças- o código da peça 1, valor unitário da peça 1, quantidade de peças 1- o código da peça 2, valor unitário da peça 2, quantidade de peças 2 O algoritmo deve calcular o valor total a ser pago e apresentar o resultado.Fórmula : (valor1*quant1 + valor2*quant2)*(IPI/100 + 1)

# Lendo a porcentagem do IPI
porcentagem_ipi = float(input("Digite a porcentagem do IPI (ex: 10): "))


# Dados da Peça 1
codPeca1 = int(input("Código da peça 1: "))
valorPeca1 = float(input("Valor unitário da peça 1: "))
quantPeca1 = float(input("Quantidade da peça 1: "))

# Dados da Peça 2
codPeca2 = int(input("Código da peça 2: "))
valorPeca2= float(input("Valor unitário da peça 2: "))
quantPeca2 = float(input("Quantidade da peça 2: "))


# Cálculo usando a fórmula fornecida
# (valor1*quant1 + valor2*quant2)*(IPI/100 + 1)
valorTotal = (valorPeca1*quantPeca1 + valorPeca2*quantPeca2) * (porcentagem_ipi/100+1)

print(f"\nO valor total a ser pago é: R$ {valorTotal:.2f}")