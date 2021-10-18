V = input().split()
A = int(V[0])
B = int(V[1])
C = int(V[2])
D = int(V[3])

if B > C and D > A and (C + D) > (A + B) and C >= 0 and D >= 0 and A % 2 == 0:
    print(f"Valores aceitos")
else:
    print(f"Valores nao aceitos")

print(A)
print(B)
print(C)
print(D)
