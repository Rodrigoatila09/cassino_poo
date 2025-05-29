import random
from abc import ABC, abstractmethod

class Maquina(ABC):

    def __init__(self,nomeJogador ="",saldoFichas="", preco=""):
        self.nome= nomeJogador
        self.saldofichas = saldoFichas
        self.precoMaquina = 20

    @abstractmethod
    def jogar(self):
        pass
         

def Roleta(self):
      
    def __init__(self):
         pass
    
    numerosVermelhos = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37]
    numerosPretos = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]

    

class CacaNiquel(Maquina):
    
        def __init__(self,pontosJogador):
            super().__init__()
            self.pontosJogador = pontosJogador
            self.arrayFrutas  = ["🍒","🍋","🍓","💀"]

        def jogar(self):
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
        
                 
testeCacaniquel = CacaNiquel
testeCacaniquel.jogoCacaNiquel()