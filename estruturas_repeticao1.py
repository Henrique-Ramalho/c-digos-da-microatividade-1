#variavel
entrada_idade = 19

entrada_idade = int(input("Digite a sua idade (0 para sair): "))

while entrada_idade != 0:
    print(f"Sua idade é: {entrada_idade}")
    entrada_idade = int(input("Digite sua idade novamente (0 para sair): "))

print("Programa encerrado.")