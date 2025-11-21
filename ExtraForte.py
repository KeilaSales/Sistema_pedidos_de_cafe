from Cafe import Cafe

class ExtraForte(Cafe):
    def __init__(self, tamanho="médio", intensidade = "normal"):
        super().__init__(nome = "Café Extra Forte", 
                         preco = 7.00,
                         tamanho = tamanho,
                         intensidade = intensidade,
                         gramas = 9)

    def preparar(self):
        super().preparar()
        print("- Usando extração mais longa.")
        print("- Garantindo sabor intenso.\n")
