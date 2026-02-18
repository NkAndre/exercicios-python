#5. Crie um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário,calcule a quantidade de salários mínimos esse usuário ganha e imprima o resultado.(1SM=R$788,00)


# O enunciado fixou o SM em 788.00, mas pedir o input deixa o código dinâmico.
salario_minimo = float(input("Insire o Salário Minimo: "))

salario_usuario = float(input("Insira seu Salário : "))

#calculo entre o salario do usuario e o salario minimo
salario_calculado = salario_usuario/salario_minimo

#Exibicao
print(f"\n1Sm= : {salario_calculado:.2f}")