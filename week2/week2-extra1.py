# EXTRA - Exercício 1
# Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. 
# Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.

# Aluna: Erica Zasimowicz 

nome = input("Digite o nome do cliente: ")
dia = input("Digite o dia de vencimento: ")
mes = input("Digite o mês de vencimento: ")
valor = input("Digite o valor da fatura: ")

print(f"Olá, {nome}\nA sua fatura com vencimento em {dia} de {mes} no valor de R$ {valor} está fechada.")