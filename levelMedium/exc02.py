# Fazer um programa que imprima a média aritmética dos números 8,9 e 7. A média dos números 4, 5 e 6. A soma das duas médias. A média das médias.

import statistics

print("--- Calculadora de Médias Grupais ---")


print("== Exibindo a Média do grupo 1==")
notasGrupo1 = [8.0, 9.0 , 7.0]

mediaGrupo1 = statistics.mean(notasGrupo1)

print(f" Média do Grupo 1  - {mediaGrupo1} - ")

notasGrupo2 = [4.0, 5.0, 6.0]

print("== Exibindo a Média do grupo 2 == ")
mediaGrupo2 = statistics.mean(notasGrupo2)

print(f"Média do grupo 2  - {mediaGrupo2} -")

print("== Exibindo a soma das médias == ")

somaDasMedias = mediaGrupo1+mediaGrupo2

print(f" Soma Das Médias - {somaDasMedias} - ")

print("==Exibindo  a Média das Médias == ")
mediaDasMedias  = somaDasMedias/2

print(f" A Média das Médias - {mediaDasMedias} - ")