#Variavel
Saida = ""

#Função adição 
def adicao(a, b):
    return(a+b)

# Função Subtração
def subtracao(a, b):
    return(a-b)

#Função Multiplicação
def miltiplicacao(a, b):
    return(a*b)

#Função Divisão
def divisao(a, b):
    if b == 0:
        return"Não foi possível realizar a divisâo por 0"
    else:
        return(a/b)

#Função Calculadora
def calculadora(num1, num2, operação):
    if operação == "+" or operação.lower() == "soma":
        return num1 + num2
    elif operação == "-" or operação.lower() == "subtracao":
        return num1 - num2
    elif operação == "*" or operação.lower() == "multiplicacao":
        return num1 * num2
    elif operação == "/" or operação.lower() == "divisao":
        if num2 == 0:
            return "não foi possível realizar a divisão por 0 "
        else:
            return num1 / num2
    else:
         return "operação inválida"
    return resultado
while saida.lower() != 'N':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou o nome): ").strip()
        resultado = calculadora(num1, num2, operacao)  
    print(f"Resultado da operação: {resultado}")
    saida = input("Deseja continuar? (S/N): ").strip()
if saida.lower() not in['s','n']:
    except ValueError:
print("Entrada inválida. Certifique-se de digitar números válidos e tentar novamente.")
print("Programa encerrado.")