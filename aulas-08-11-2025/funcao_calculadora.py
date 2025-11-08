# Ativivade 1
# Nome: Calculadora
# Objetivo: definir uma função que receba três parâmetros e retorne o resultado de uma operação matemática básica.

# Função da calucadora
def calculadora(numero1, numero2, operacao):
    # Definir a operação correspondente à escolhida
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        # Divisão por zero é impossível
        else:
            return "Erro: divisão por zero não é possível"
    # Caso coloque um valor que não corresponde a nenhuma operação
    else:
        return "Operação inválida!"

# Exemplo:
resultado = calculadora(88, 4, '/')
print(f"Resultado: {resultado}")
