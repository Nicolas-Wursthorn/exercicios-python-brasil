# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a sua senha: ")

while usuario == senha:
    print("Sua senha não pode ser igual ao nome de usuário, tente novamente.")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a sua senha: ")