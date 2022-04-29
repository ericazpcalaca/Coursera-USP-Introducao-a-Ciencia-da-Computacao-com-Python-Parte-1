# Exercício 3
# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

# Aluna: Erica Zasimowicz

num = int(input("Digite um número inteiro: "))
soma = 0
while(num > 0):
    soma += num % 10
    num = int(num /10)
print(soma)