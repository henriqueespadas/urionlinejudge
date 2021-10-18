valor = input().split(" ")

A = float(valor[0])
B = float(valor[1])
C = float(valor[2])
rect = (A * C) / 2
rec = A * C
cic = 3.14159 * C ** 2
trap = ((A + B) * C) / 2
square = B ** 2
print(
    f"TRIANGULO: {rect:.3f}\n"
    f"CIRCULO: {cic:.3f}\n"
    f"TRAPEZIO: {trap:.3f}\n"
    f"QUADRADO: {square:.3f}\n"
    f"RETANGULO: {A * B:.3f}"
)
