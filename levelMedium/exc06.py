#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa em dias. Leve em consideração o ano com 365dias e o mês com 30.(Ex: 3 anos, 2 meses e 15 dias = 1170 dias.)

#Recebendo os inputs de anos, meses, dias
anos= int(input("anos: "))

meses= int(input("meses: "))

dias= int(input("dias: "))

#formula pura
totalDias = (anos * 365) + (meses * 30) + dias

#Exibição
print(f"O total de dias é: {totalDias}")
