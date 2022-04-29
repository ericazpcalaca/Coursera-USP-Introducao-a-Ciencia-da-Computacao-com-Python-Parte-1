# Exercício 1
# Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída

# Aluna: Erica Zasimowicz

numero = int(input("Digite o valor de n: "))
i = 1
fatorial = 1
while i <= numero:
  fatorial = fatorial * i
  i +=1

print(fatorial)