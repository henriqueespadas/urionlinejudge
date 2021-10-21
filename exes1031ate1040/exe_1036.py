import math

V = input().split()
A = float(V[0])
B = float(V[1])
C = float(V[2])

d = (B ** 2) - (4 * A * C)
if d < 0:
    print(f"Impossivel calcular")
elif A == 0:
    print(f"Impossivel calcular")
else:
    r1 = (-B + math.sqrt(d)) / (2 * A)
    r2 = (-B - math.sqrt(d)) / (2 * A)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
