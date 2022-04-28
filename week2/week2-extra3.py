# EXTRA - Atividade 3
# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas

# Aluna: Erica Zasimowicz 

numero = int(input("Digite um número inteiro:"))
numero_aux = numero//10
dezena = str(numero_aux)
dezena = dezena[-1]
print(f'O dígito das dezenas é',dezena)