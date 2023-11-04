def exe_1021_1():
    """runtime:0.00000048 segundos segundos"""
    v = input(float()) * 100
    lista1 = (10000, 5000, 2000, 1000, 500, 200)
    print("NOTAS:")
    for n in lista1:
        notas = v // n
        print(f"{int(notas)} nota(s) de R$ {n / 100:.2f}")
        v %= n

    print("MOEDAS:")
    lista2 = (100, 50, 25, 10, 5, 1)
    for x in lista2:
        moedas = v // x
        print(f"{int(moedas)} moeda(s) de R$ {x / 100:.2f}")
        v %= x


def exe_1022_2(valor_total):
    dicionario = {
        "moeda100": 10000,
        "moeda50": 5000,
        "moeda20": 2000,
        "moeda10": 1000,
        "moeda5": 500,
        "moeda2": 200,
        "moeda1": 100,
        "moeda050": 50,
        "moeda025": 25,
        "moeda010": 10,
        "moeda005": 5,
        "moeda001": 1,
    }

    def contar_moeda(valor_moeda, valor_total):
        quantidade = 0
        while valor_total >= valor_moeda:
            quantidade += 1
            valor_total -= valor_moeda
        return quantidade

    def contar(valor_total):
        valor_total = int(valor_total * 100)
        for moeda, valor_moeda in dicionario.items():
            quantidade_moeda = contar_moeda(valor_moeda, valor_total)
            valor_total -= quantidade_moeda * valor_moeda
            if valor_moeda > 100:
                if valor_moeda == 10000:
                    print("NOTAS:")
                print(f"{quantidade_moeda} nota(s) de R$ {valor_moeda / 100:.2f}")
                continue
            if valor_moeda == 100:
                print("MOEDAS:")
            print(f"{quantidade_moeda} moeda(s) de R$ {valor_moeda / 100:.2f}")

    contar(valor_total)


def exe_1022_3(valor_total):
    dicionario = {
        "moeda100": 10000,
        "moeda50": 5000,
        "moeda20": 2000,
        "moeda10": 1000,
        "moeda5": 500,
        "moeda2": 200,
        "moeda1": 100,
        "moeda050": 50,
        "moeda025": 25,
        "moeda010": 10,
        "moeda005": 5,
        "moeda001": 1,
    }

    def contar_moeda(valor_moeda, valor_total):
        quantidade = valor_total // valor_moeda
        return quantidade

    def contar(valor_total):
        valor_total = int(valor_total * 100)
        for moeda, valor_moeda in dicionario.items():
            quantidade_moeda = contar_moeda(valor_moeda, valor_total)
            valor_total -= quantidade_moeda * valor_moeda
            if valor_moeda > 100:
                if valor_moeda == 10000:
                    print("NOTAS:")
                print(f"{quantidade_moeda} nota(s) de R$ {valor_moeda / 100:.2f}")
                continue
            if valor_moeda == 100:
                print("MOEDAS:")
            print(f"{quantidade_moeda} moeda(s) de R$ {valor_moeda / 100:.2f}")

    contar(valor_total)
    inserir_valor = float(input())
