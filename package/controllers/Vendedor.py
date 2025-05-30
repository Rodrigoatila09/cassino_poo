class Vendedor ():
    def __init__(self, jogador):
        self.jogador = jogador
        


    def comprarFichas(self):
        mensagemVendedor = input(f"Bem vindo {self.jogador.nome}! Deseja comprar alguns tickets?\n (S) | (N)\n").upper()

        if(mensagemVendedor == "N"):
            print("\n Tudo bem! Qualquer coisa estarei aqui!")
        elif(mensagemVendedor == "S"):
            fichasPedidas = int(input("Muito bem!\n Quantas fichas voce deseja?\n "))
            precoFInal = 5 * fichasPedidas
            if(self.jogador.getMoney() >= precoFInal):
                self.jogador.saldoFichas += fichasPedidas
                self.jogador.setMoney(self.jogador.getMoney() - precoFInal)
                print(f"Fichas compradas com sucesso! | Saldo atual : {self.jogador.saldoFichas} \n")
                print(f"Você ainda têm : {self.jogador.getMoney()}")
            else:
                print("Você está liso amigão!")
        else:
            print("Opção inválida")
    

