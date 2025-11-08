# Ativivade 2
# Nome: Herança de Veículos
# Objetivo: Criar uma classe base (Veiculo) com atributos gerais, e uma classe filha (Carro) que herda de Veiculo e adiciona um atributo específico.

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        return f"Marca: {self.marca}; \nModelo: {self.modelo}; \nAno: {self.ano} \n"

class Carro (Veiculo):
    def __init__(self, marca, modelo, ano, cor, numero_portas):
        super().__init__(marca, modelo, ano)
        self.cor = cor
        self.numero_portas = numero_portas

    def exibir_informacoes(self):
        return f"Marca: {self.marca}; \nModelo: {self.modelo}; \nAno: {self.ano}; \nCor: {self.cor}; \nNúmero de portas: {self.numero_portas} \n"
    
# Exemplo 1:
carro1 = Carro("Toyota", "Corolla", 2022, "Vermelho", 4)
# Exemplo 2:
carro2 = Carro("Ferrari", "Roma", 2024, "Prata", 2)

# Mostrando Exemplos:
print (f"=== Informações Carro 1 === \n{carro1.exibir_informacoes()}")
print (f"=== Informações Carro 2 === \n{carro2.exibir_informacoes()}")