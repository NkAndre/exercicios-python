#INVERSO DO 06 : O usuário vai digitar um número total de dias (ex: 1100) e você deve transformar isso em Anos, Meses e Dias, mantendo a regra de que 1 ano tem 365 dias e 1 mês tem 30 dias.

total_dias = int (input("Digite o total de dias: "))

# 1. Quantos anos cabem nesses dias?
anos = total_dias//365

restoAnos = total_dias % 365 

# 2. Dos dias que sobraram, quantos meses cabem?
meses = restoAnos // 30

# 3. O que sobrar dos meses são os dias finais
dias = restoAnos % 30

#EXIBIÇÃO : 
print(f"Resultado: {anos} anos, {meses} meses e {dias} dias.")