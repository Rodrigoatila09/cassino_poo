
class Jogador():


    def __init__(self, nome="",cpf = ""):
        self.nome = nome
        self._cpf = cpf
        self.__dinheiro = 100
        self.saldoFichas = 0


    def getMoney(self):
        return self.__dinheiro

    def setMoney(self,valor):
        self.__dinheiro = valor

    def nomeJogador(self):
        inputNome = input("Digite seu nome:\n")
        self.nome = inputNome
        return self.nome
    
    def cpfJogador(self):
        cpfJogador = int(input("Digite o número de seu CPF:\n"))
        self.cpf = cpfJogador
        return self.cpf



    