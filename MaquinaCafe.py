from datetime import datetime

class MaquinaDeCafe:
    _maquina = None

    #SINGLETON

    def __new__(cls):
        #Garante que só exista UMA máquina de café.
        if cls._maquina is None:
           cls._maquina = super().__new__(cls)
           cls._maquina.historico = []  # cria lista de histórico
        return cls._maquina
    
    def preparar_cafe(self, cafe):
        #Recebe um objeto Café e prepara.
        print("\n=== MÁQUINA DE CAFÉ ===")
        cafe.preparar()

        # registra no histórico (nome + hora)
        registro = (
            f"{cafe.nome} | "
            f"Tamanho: {cafe.tamanho} | "
            f"Intensidade: {cafe.intensidade} | "
            f"Preparado em: {datetime.now().strftime('%H:%M:%S')}"
        )
        self.historico.append(registro)

    def exibir_historico(self):
        #Mostra todos os cafés preparados.
        print("\n=== HISTÓRICO DE CAFÉS PREPARADOS ===")
        if not self.historico:
            print("Nenhum café foi preparado ainda.")
        else:
            for item in self.historico:
                print("- " + item)