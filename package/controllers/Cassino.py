from package.models.Maquina import Maquina, CacaNiquel, Roleta
from package.models.Jogador import Jogador
from package.controllers.Vendedor import Vendedor


class Cassino:
    def __init__(self):
        self.jogador = Jogador()
        self.vendedor = Vendedor(self.jogador)

    def iniciar(self):
        print("🎰 Bem-vindo ao PyVegas 🎲")
        self.jogador.nomeJogador()
        while True:
            self.menu_principal()
            escolha = input("Escolha uma opção: ").strip()
            if escolha == "1":
                self.vendedor.comprarFichas()
            elif escolha == "2":
                self.jogar_maquina(Roleta)
            elif escolha == "3":
                self.jogar_maquina(CacaNiquel)
            elif escolha == "4":
                saldo_input = input("Deseja visualizar o dinheiro ou as fichas?\n (D) - Dinheiro \n (F) - Fichas |").upper()
                if(saldo_input == "D"):
                    print(f"Saldo atual: {self.jogador.getMoney()}")
                else:
                    print(f"Saldo atual: {self.jogador.saldoFichas} fichas")
            elif escolha == "5":
                print("Obrigado por visitar o cassino! Até logo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_principal(self):
        print("\n=== MENU DO CASSINO ===")
        print("1 - Comprar Fichas 💰")
        print("2 - Jogar Roleta 🎯")
        print("3 - Jogar Caça-Níquel 🍒")
        print("4 - Ver Saldo 💸")
        print("5 - Sair 🚪")

    def jogar_maquina(self, MaquinaClass):
        jogo = MaquinaClass(self.jogador.nome, self.jogador.saldoFichas)
        jogo.jogar()
        self.jogador.saldoFichas = jogo.saldofichas
