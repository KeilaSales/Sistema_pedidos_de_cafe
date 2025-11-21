from Cafe import Cafe

class Expresso(Cafe):
    def __init__(self, tamanho="medio", intensidade = "normal"):
        super().__init__(
            nome = "Café Expresso", 
            preco = 5.00, 
            tamanho= tamanho,
            intensidade = intensidade,
            gramas = 8)
    
    def preparar(self):
        super().preparar()
        print("- Passando água.")
        print("- Extraindo café intenso.\n")
