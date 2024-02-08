'''
Instituição: FIAP
Turma: 1TDCG
Integrantes do Grupo:
Danilo da Gama Campos
Eduardo do Nascimento Silva
Gustavo Duarte Bezerra da Silva
Henrique Batista de Souza
Vinicius Saraiva Campelo
'''

fibonacci = [0, 1]
n = int(input("Digite um número maior ou igual a 2: "))
if n < 2:
    print("O número deve ser maior ou igual a 2.")
    n = int(input("Digite um número maior ou igual a 2: "))
else:
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        print("Os {n} primeiros termos da sequência de Fibonacci são:")
    for i in range(n):
        print(fibonacci[i])
