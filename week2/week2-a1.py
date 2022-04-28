# Exercício 1
# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

# Observação: a saída deve estar no formato: "perímetro: x - área: y"

# Aluna: Erica Zasimowicz

lado = int(input("Digite o valor correspondente ao lado de um quadrado: "))

perim = 4 * lado
area = lado **2
print("perímetro:",perim,"- área:",area)
