from CafeDecorator import CafeDecorator

# Chantilly
class Chantilly(CafeDecorator):
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + 1.50  # adiciona preço

    def preparar(self):
        super().preparar()
        print("- Adicionando chantilly por cima.\n")


# Calda de Chocolate
class CaldaChocolate(CafeDecorator):
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + 2.00

    def preparar(self):
        super().preparar()
        print("- Adicionando calda de chocolate.\n")


# Canela
class Canela(CafeDecorator):
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + 0.50

    def preparar(self):
        super().preparar()
        print("- Polvilhando canela por cima.\n")

# Leite em Pó 
class LeiteEmPo(CafeDecorator):
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + 1.00 

    def preparar(self):
        super().preparar()
        print("- Adicionando leite em pó por cima.\n")

# Creme de Avelã
class CremeAvela(CafeDecorator):
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + 1.00 

    def preparar(self):
        super().preparar()
        print("- Adicionando creme de avelã.\n")