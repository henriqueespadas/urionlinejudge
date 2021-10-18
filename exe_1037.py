v = float(input())
if v < 0 or v > 100:
    print(f"Fora de intervalo")
elif v <= 25:
    print(f"Intervalo [0,25]")
elif v <= 50:
    print(f"Intervalo (25,50]")
elif v <= 75:
    print(f"Intervalo (75,100]")
else:
    print(f"Intervalo (75,100]")


# v = float(input())
# if v > 0 and v <= 25:
#     print(f'Intervalo [0,25]')
# elif v > 25 and v <= 50:
#     print(f'Intervalo (25,50]')
# elif v > 50 and v <= 75:
#     print(f'Intervalo (50,75]')
# elif v > 75 and v <= 100:
#     print(f'Intervalo (75,100]')
# else:
#     print(f'Fora de intervalo')
