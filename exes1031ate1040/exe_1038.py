"""Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay.
This is a very simple program with the only intention of practice of selection commands.
Input
The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.
Output
The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.
Input Sample	Output Sample
3 2
Total: R$ 10.00
4 3
Total: R$ 6.00
2 3
Total: R$ 13.50
"""

lista = {
    1: ("Cachoro Quente", 4.00),
    2: ("X-Salada", 4.50),
    3: ("X-Bacon", 5.00),
    4: ("X-Torrada simples", 2.00),
    5: ("Refrigerante", 1.50),
}


def mercado(codigo, quantidade):
    valor = lista[codigo][1] * quantidade
    print(f"Total: R$ {valor:.2f}")


compra = input().split()

mercado(int(compra[0]), int(compra[1]))
