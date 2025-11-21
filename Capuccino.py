from Cafe import Cafe

class Capuccino(Cafe):
    def __init__(self, tamanho="médio", intensidade = "normal"):
        super().__init__(nome = "Café Capuccino", 
                         preco = 7.00, 
                         tamanho = tamanho,
                         intensidade = intensidade,
                         gramas = 10)

    def preparar(self):
        super().preparar()
        print("- Vaporizando leite.")
        print("- Adicionando espuma")
        print("- Finalizando com toque de leite em pó.\n")

