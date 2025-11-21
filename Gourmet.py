from Cafe import Cafe

class Gourmet(Cafe):
    def __init__(self, tamanho="médio", intensidade = "normal"):
        super().__init__( nome = "Café Gourmet",
                          preco = 9.00, 
                          tamanho = tamanho,
                          intensidade = intensidade,
                          gramas = 8)

    def preparar(self):
        super().preparar()
        print("- Moendo grãos 100% selecionados.")
        print("- Extraindo lentamente para realçar aroma.")
        print("- Servindo com textura aveludada.\n")
