from CafeFactory import CafeFactory
from MaquinaCafe import MaquinaDeCafe
from Adicionais import Chantilly, CaldaChocolate, Canela, LeiteEmPo, CremeAvela


def escolher_tipo_cafe():
    # Função que exibe opções e retorna o tipo de café escolhido pelo usuário
    print("\n=== Escolha o tipo de café ===")
    print("1 - Expresso")
    print("2 - Capuccino")
    print("3 - Latte")
    print("4 - Moccacino")
    print("5 - Extra Forte")
    print("6 - Gourmet")

    opc = input("Digite o número do café: ")

    tipos = {
        "1": "expresso",
        "2": "capuccino",
        "3": "latte",
        "4": "moccacino",
        "5": "extraforte",
        "6": "gourmet"
        # Dicionário que relaciona número -> nome do café.
    }

    return tipos.get(opc, None)
    # Pega o valor correspondente à chave digitada, se alguma inválida retorna None


def escolher_tamanho():
    print("\n=== Escolha o tamanho ===")
    print("1 - Pequeno")
    print("2 - Médio")
    print("3 - Grande")

    opc = input("Digite o número: ")

    tamanhos = {
        "1": "pequeno",
        "2": "medio",
        "3": "grande"
    }

    return tamanhos.get(opc, None)


def escolher_intensidade():
    print("\n=== Intensidade do café ===")
    print("1 - Suave")
    print("2 - Normal")
    print("3 - Forte")

    opc = input("Digite o número: ")

    intensidades = {
        "1": "suave",
        "2": "normal",
        "3": "forte"
    }

    return intensidades.get(opc, None)


def escolher_adicionais(cafe):
    # Função que permite o usuário selecionar 0 ou vários adicionais.
    print("\n=== Adicionais ===")
    print("Digite os números dos adicionais desejados separados por vírgula.")
    print("1 - Chantilly (+1.50)")
    print("2 - Calda de Chocolate (+2.00)")
    print("3 - Canela (+0.50)")
    print("4 - Leite em Pó (+1.00)")
    print("5 - Creme de Avelã (+2.50)")
    print("0 - Nenhum")

    opcs = input("Opções: ").split(",")
    # input() recebe um texto (ex: "1,3,4")
    # .split(",") separa em lista ["1", "3", "4"]
    # transforma uma única string em várias escolhas.

    for op in opcs:
        op = op.strip() #remove espaços
        # Cada adicional envolve o café original (Decorator)
        if op == "1":
            cafe = Chantilly(cafe)
        elif op == "2":
            cafe = CaldaChocolate(cafe)
        elif op == "3":
            cafe = Canela(cafe)
        elif op == "4":
            cafe = LeiteEmPo(cafe)
        elif op == "5":
            cafe = CremeAvela(cafe)

    return cafe


def menu():
    maquina = MaquinaDeCafe()
    # Sempre retorna a mesma instância (Singleton)

    while True:
        print("\n==========================")
        print("   SISTEMA DE CAFETERIA")
        print("==========================")
        print("1 - Fazer pedido")
        print("2 - Ver histórico")
        print("3 - Sair")

        opc = input("Escolha: ")

        if opc == "1":
            tipo = escolher_tipo_cafe()
            if not tipo:
                print("Opção inválida!")
                continue

            tamanho = escolher_tamanho()
            if not tamanho:
                print("Tamanho inválido!")
                continue

            intensidade = escolher_intensidade()
            if not intensidade:
                print("Intensidade inválida!")
                continue

            # Cria café base com Factory
            cafe = CafeFactory.criar_cafe(tipo, tamanho=tamanho, intensidade=intensidade)

            # adiciona extras
            cafe = escolher_adicionais(cafe)

            print("\n=== RESUMO DO PEDIDO ===")
            print(f"Café: {cafe.nome}")
            print(f"Tamanho: {cafe.tamanho}")
            print(f"Intensidade: {cafe.intensidade}")
            print(f"Preço final: R$ {cafe.preco:.2f}")

            confirmar = input("Confirmar pedido? (s/n): ").lower()
            if confirmar == "s":
                maquina.preparar_cafe(cafe)
                print("Pedido preparado com sucesso!")
            else:
                print("Pedido cancelado.")

        elif opc == "2":
            maquina.exibir_historico()

        elif opc == "3":
            print("Saindo...!")
            break

        else:
            print("Opção inválida! Tente novamente.")


menu()
