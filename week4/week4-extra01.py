# EXTRA - Exercício 1
# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

#Aluna: Erica Zasimowicz 

def prime_checker(number):
    cont = 1
    check = 0
    while number >= cont:
      if number % cont == 0:
        check+=1
      cont+=1

    if check ==2:
      print("É primo")
    else:
      print("Não é primo")

number = int(input("Digite um numero positivo: "))
while number > 0:
  prime_checker(number)
  number = int(input("Digite um numero positivo: "))