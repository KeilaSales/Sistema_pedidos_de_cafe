from abc import ABC, abstractmethod
from datetime import datetime

class Cafe(ABC):

    """
    Classe abstrata base para todos os cafés.
    Define estrutura e obriga as subclasses a implementarem descrição e preço.
    """

    def __init__(self, nome, preco, tamanho, intensidade, gramas):
        self._nome = nome
        self._preco = preco
        self._tamanho = tamanho.lower()
        self._intensidade = intensidade.lower()
        self._gramas = gramas
        self._hora_preparo = None  # será definido ao preparar
    
        self.validar_tamanho()
        self.validar_intensidade() 

    def validar_tamanho(self):
        #Verifica se o tamanho informado é válido.
        tamanhos_validos = ["pequeno", "medio", "médio", "grande"]
        if self._tamanho not in tamanhos_validos:
            raise ValueError("Tamanho inválido. Use: pequeno, médio ou grande.")

    def validar_intensidade(self):
        #Verifica se a intensidade informada é válida.
        intensidades_validas = ["suave", "normal", "forte"]
        if self._intensidade not in intensidades_validas:
            raise ValueError("Intensidade inválida. Use: suave, normal ou forte.")

    @property
    def tamanho(self):
        return self._tamanho
    
    @property
    def intensidade(self):
        return self._intensidade
    
    @property
    def hora_preparo(self):
        return self._hora_preparo
    
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

#jeito padrão de preparo 
    
    def preparar(self):
        #Etapas básicas, comuns a todos os cafés
        self._hora_preparo = datetime.now()

        print(f"\nPreparando {self.nome} ({self.tamanho})...")
        print(f"- Intensidade: {self.intensidade}")
        print(f"- Usando {self._gramas}g de café moído.")
 

    def __str__(self):
        #Exibição simples do café.
        return f"{self.nome} - {self.tamanho} - R$ {self.preco:.2f}"



    