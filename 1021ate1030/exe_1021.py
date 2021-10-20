v = float(input())
lista1 = (100, 50, 20, 10, 5, 2)
print(f"NOTAS:")
for n in lista1:
    notas = int(v // n)
    print(f"{notas} nota(s) de R$ {n:.2f}")
    v -= notas * n
print(f"MOEDAS:")
lista2 = (1, 0.5, 0.25, 0.1, 0.05, 0.01)
for x in lista2:
    moedas = int(round(v, 2) // x)
    print(f"{moedas} moeda(s) de R$ {x:.2f}")
    v -= moedas * x


# n100 = (v // 100)
# r100 = v % 100
# n50 = (r100 // 50)
# r50 = r100 % 50
# n20 = (r50 // 20)
# r20 = r50 % 20
# n10 = (r20 // 10)
# r10 = r20 % 10
# n5 = (r10 // 5)
# r5 = r10 % 5
# n2 = (r5 // 2)
# r2 = r5 % 2
# m1 = (r2 // 1)
# rm1 = r2 % 1
# m50 = (rm1 // 0.5)
# mr50 = rm1 % 0.5
# m25 = (mr50 // 0.25)
# mr25 = mr50 % 0.25
# m10 = (mr25 // 0.1)
# mr10 = mr25 % 0.1
# m5 = round(mr10 // 0.05, 2)
# mr5 = mr10 % 0.05
# m01 = round(mr5 // 0.01, 2)
# print(f'NOTAS:')
# print(f'{int(n100)} nota(s) de R$ 100.00')
# print(f'{int(n50)} nota(s) de R$ 50.00')
# print(f'{int(n20)} nota(s) de R$ 20.00')
# print(f'{int(n10)} nota(s) de R$ 10.00')
# print(f'{int(n5)} nota(s) de R$ 5.00')
# print(f'{int(n2)} nota(s) de R$ 2.00')
# print(f'MOEDAS:')
# print(f'{int(round(m1, 2))} moeda(s) de R$ 1.00')
# print(f'{int(round(m50, 2))} moeda(s) de R$ 0.50')
# print(f'{int(round(m25, 2))} moeda(s) de R$ 0.25')
# print(f'{int(round(m10, 2))} moeda(s) de R$ 0.10')
# print(f'{int(round(m5, 2))} moeda(s) de R$ 0.05')
# print(f'{int(round(m01, 2)) + 0.01} moeda(s) de R$ 0.01')
