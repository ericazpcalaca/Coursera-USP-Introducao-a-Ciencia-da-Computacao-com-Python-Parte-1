# EXTRA - Exercício 2
# Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

# Aluna: Erica Zasimowicz 

segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))

minutos = segundos//60
segundos_restante = segundos%60
horas = minutos//60
minutos_restante = minutos%60
dias = horas//24
horas_restante = horas%24
print(f"{dias} dias, {horas_restante} horas, {minutos_restante} minutos e {segundos_restante} segundos")