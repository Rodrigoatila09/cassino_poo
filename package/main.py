from models.Jogador import Jogador
from models.Maquina import Maquina
from controllers.Vendedor import Vendedor

is_jogador = Jogador()
is_vendedor = Vendedor(is_jogador)


is_jogador.nomeJogador()
is_vendedor.comprarFichas()
