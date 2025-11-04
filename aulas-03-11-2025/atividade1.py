# Ativivade 1
# Nome: Verificador de Maioridade
# Objetivo: Praticar o uso de input (para receber dados do usuário), int (para converter o tipo de dado) e a estrutura condicional if/else (para tomar uma decisão)


# Criação da clase "Pessoa"
class Pessoa:

    # Método Construtor
    def __init__ (self):
        # Solicitação do nome
        self.nome = input("Qual é o seu nome?\n")
    # Solicitação do número e validação se é um inteiro maior ou igual a zero.
        while True:
            self.idade_txt = input("Qual é a sua idade?\n")
            try:
                self.idade_num = int(self.idade_txt)
                if self.idade_num < 0:
                    print("Idade inválida: Insira um número inteiro maior ou igual a zero.")
                else:
                    self.idade = self.idade_num
                    break
            except ValueError:
                print("Entrada inválida: Insira um número inteiro maior ou igual a zero.")
    
    # Função para verificar se a pessoa é menor ou maior de idade
    def verificar_idade (self):
        if self.idade >= 18:
            print(f"Olá {self.nome}, você é maior de idade.")
        else:
            print (f"Olá {self.nome}, você é menor de idade")


# Programa Principal
pessoa = Pessoa ()
pessoa.verificar_idade()