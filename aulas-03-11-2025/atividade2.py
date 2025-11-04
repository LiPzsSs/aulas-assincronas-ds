# Ativivade 2
# Nome: A Tabuada
# Objetivo:  Praticar o uso de input(), int() e o loop for com a função range()


# Criação da Classe Tabuada
class Tabuada:
    # Método Construtor
    def __init__ (self):
        # Solicitação do número e validação se é um inteiro
        while True:
            self.numero_txt = input (f"Digite um número para ver a tabuada: ")
            try:
                self.numero = int(self.numero_txt)
                break
            except ValueError:
                print (f"Valor Inválido: Insira um número inteiro para ver sua tabuada: ")

    # Função de multiplicar o valor dado de 1 a 10 e mostrar o resultado na tela
    def calcular_tabuada(self):
        for i in range(1,11):
            resultado = i * self.numero
            print(f"{i} * {self.numero} = {resultado}")


# Programa Principal
calculo = Tabuada ()
calculo.calcular_tabuada()