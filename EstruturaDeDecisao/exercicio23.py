# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input("Digite um número: "))

if num // 1 == num:
    print("Esse número é inteiro")
else:
    print("Esse número é decimal")