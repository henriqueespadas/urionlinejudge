v = float(input())
n100 = v // 100
r100 = v % 100
n50 = r100 // 50
r50 = r100 % 50
n20 = r50 // 20
r20 = r50 % 20
n10 = r20 // 10
r10 = r20 % 10
n5 = r10 // 5
r5 = r10 % 5
n2 = r5 // 2
r2 = r5 % 2
n1 = r2 // 1
print(f"{v}")
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")
