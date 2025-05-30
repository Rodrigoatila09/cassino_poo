from package.models.Jogador import Jogador
from package.models.Maquina import Maquina
from package.controllers.Vendedor import Vendedor
from package.controllers.Cassino import Cassino

if __name__ == "__main__":
    app = Cassino()
    app.iniciar()
