import random

class Maquina():

    def __init__(self,nomeJogador ="",saldoFichas="", preco=""):
        self.nome= nomeJogador
        self.saldofichas = saldoFichas
        self.precoMaquina = 20

    # def debitarFichas(self):
    #     if(self.nome and self.saldofichas >= self.precoMaquina ):
    #         self.


class CacaNiquel(Maquina):
    
        def __init__(self,pontosJogador):
            super().__init__()
            self.pontosJogador = pontosJogador
            self.arrayFrutas  = ["🍒","🍋","🍓","💀"]

        def jogoCacaNiquel(self):
        
            precoJogo = 20
            sorteador = random.choices(self.arrayFrutas, k=3)
            if(self.nome and self.saldofichas >= precoJogo ):   
                inciarJogo = input("Deseja tentar a sorte?\n (S) | (N)").upper()
                if(inciarJogo =="S"):
                     return sorteador
            elif(self.saldofichas < precoJogo):
                print("Você não tem fichas suficientes!")
            elif(self.nome):
                 print("O jogador não está cadastrado corretamente!")
            else:
                 print("Oops, algum erro inesperado aconteceu")
        
        





            # print(sorteador)

            # if(self.nomeJogador):
                 
testeCacaniquel = CacaNiquel
testeCacaniquel.jogoCacaNiquel()