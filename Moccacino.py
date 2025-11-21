from Cafe import Cafe

class Moccacino(Cafe):
    def __init__(self, tamanho="médio", intensidade = "normal"):
        super().__init__(nome = "Café Moccacino", 
                         preco = 6.00, 
                         tamanho = tamanho, 
                         intensidade = intensidade,
                         gramas = 12)

    def preparar(self):
        super().preparar()
        print("- Misturando chocolate quente.")
        print("- Adicionando espresso.")
        print("- Finalizando com leite vaporizado.\n")
