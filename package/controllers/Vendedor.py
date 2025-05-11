class Vendedor ():
    def __init__(self, jogador):
        self.jogador = jogador
        


    def comprarFichas(self):
        cotacao = 5
        mensagemVendedor = input(f"Bem vindo {self.jogador.nome}! Deseja comprar alguns tickets?\n (S) | (N)\n").upper()

        if(mensagemVendedor == "N"):
            print("\n Tudo bem! Qualquer coisa estarei aqui!")
        elif(mensagemVendedor == "S"):
            fichasPedidas = int(input("Muito bem!\n Quantas fichas voce deseja?\n "))
            precoFInal = cotacao * fichasPedidas
            if(self.jogador.dinheiro >= precoFInal):
                self.jogador.saldo += fichasPedidas
                self.jogador.dinheiro -= precoFInal
                print(f"Fichas compradas com sucesso! | Saldo atual : {self.jogador.saldo} \n")
                print(f"Você ainda têm : {self.jogador.dinheiro}")
            else:
                print("Você está liso amigão!")
        else:
            print("Opção inválida")
    

