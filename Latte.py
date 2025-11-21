from Cafe import Cafe

class Latte(Cafe):
    def __init__(self, tamanho="médio", intensidade = "normal"):
        super().__init__( nome ="Café Latte",
                          preco = 7.00, 
                          tamanho = tamanho,
                          intensidade = intensidade,
                          gramas = 12)

    def preparar(self):
        super().preparar()
        print("- Adicionando leite vaporizado.")
        print("- Finalizando com uma camada fina de espuma.\n")
