import random
import time
from abc import ABC, abstractmethod

class Maquina(ABC):

    def __init__(self,nomeJogador ="",saldoFichas=""):
        self.nome= nomeJogador
        self.saldofichas = saldoFichas
        self.precoMaquina = 20
        self.statusCompra = None
    @abstractmethod
    def jogar(self):
        pass
         
    def debitar_fichas(self):
        if(self.nome != None):
            inputComprar = input(f"Deseja Jogar este jogo? || VALOR : {self.precoMaquina} \n(S)|(N)").upper()
            if(inputComprar == "S" and self.saldofichas >= self.precoMaquina):
                self.statusCompra = True
                self.saldofichas -= self.precoMaquina
                print(" Compra aprovada ✔ \n  ✨ QUE A SORTE ESTEJA SEMPRE COM VOCÊ ✨")
                return True
            elif(inputComprar and self.saldofichas < self.precoMaquina):
                self.statusCompra = False
                print("Infelizmente você não têm fichas o suficiente para jogar\n Você pode comprar mais com algum dos nossos vendedores.")
                return False
        else:
            self.statusCompra = None
            print("O jogador não existe")   
            return False

class Roleta(Maquina):
      
    def __init__(self,nomeJogador, saldoFichas):
        super().__init__(nomeJogador,saldoFichas)
        self.numerosVermelhos = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
        self.numerosPretos = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    
    def jogar(self):
        if(self.debitar_fichas()):   
                inciarJogo = input("Deseja tentar a sorte?\n (S) | (N)").upper()
                if(inciarJogo =="S"):
                    escolherNumero = input("Muito bem!! Agora você deve escolher entre | (P) - Números Pretos | \n " \
                    " | (V) - Números Vermelhos |").upper()
                    numeroSorteado = random.randint(0,36)     

                    if(numeroSorteado == 0): 
                        print(f"O numero sorteado foi o 0 | Cor VERDE HAHA\n")
                        print("QUe azar!! Você perdeu tudo 😹")
                    if(escolherNumero == "P" and numeroSorteado in self.numerosPretos):
                        print(f"O número sorteado foi: {numeroSorteado}\n Parabéns, você ganhou!!")
                        self.saldofichas += 5
                    if(escolherNumero == "V" and numeroSorteado in self.numerosVermelhos):
                        print(f"O número sorteado foi: {numeroSorteado}\n Parabéns, você ganhou!!")   
                        self.saldofichas += 5 
                            
        



class CacaNiquel(Maquina):
    
        def __init__(self,nomeJogador,saldoFichas):
            super().__init__(nomeJogador,saldoFichas)
            self.arrayFrutas  = ["🍒","🍋","🍓","💀"]

        def jogar(self):
            sorteador = random.choices(self.arrayFrutas, k=3)
            if(self.debitar_fichas()):   
                inciarJogo = input("Deseja tentar a sorte?\n (S) | (N)").upper()
                if(inciarJogo =="S"):
                    print("Aguarde enquanto tiramos seu dinhei-... Tiramos sua sorte! 😸")
                    time.sleep(3)
                    if len(set(sorteador)) == 1:
                        print(f"Sua sorte foi: {sorteador}\n")
                        print("🎉|JackPot|🎉\n Tirou sorte grande! " )
                        self.saldofichas += (self.precoMaquina + 15)

                    elif len(set(sorteador)) == 2:
                        print(f"Sua sorte foi: {sorteador}\n")
                        print("Quase Conseguiu 😼")

                    else:
                        print(f"Sua sorte foi: {sorteador}\n")
                        print("Se deu mal amigão!!")
                    
            elif(self.statusCompra is False):
                print("Você não tem fichas suficientes!")

            elif(self.statusCompra is None):
                 print("O jogador não está cadastrado corretamente!")

            else:
                 
                 print("Oops, algum erro inesperado aconteceu")
        
                 
