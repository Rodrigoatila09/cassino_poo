class Jogador():


    def __init__(self, nome="", cpf=""):
        self.nome = nome
        self.cpf = cpf
        self.dinheiro = 100
        self.saldo = 0

    def nomeJogador(self):
        inputNome = input("Digite seu nome:\n")
        self.nome = inputNome
        return self.nome
    
    def cpfJogador(self):
        cpfJogador = int(input("Digite o número de seu CPF:\n"))
        self.cpf = cpfJogador
        return self.cpf



    