# Exercício 2
# Receba um número inteiro positivo na entrada e imprima os  n primeiros números ímpares naturais. 

# Aluna: Erica Zasimowicz 

def num_impar(num):
  i = 1
  count = 1
  while count <= num:
    if not i%2==0:
      print(i)
      count += 1 
    i += 1
    

num = int(input("Digite o valor de n:"))
num_impar(num)