entrada = input().split()
N1 = entrada[0]
N2 = entrada[1]
N3 = entrada[2]
N4 = entrada[3]
media = (float(N1) * 2 + float(N2) * 3 + float(N3) * 4 + float(N4) * 1) / 10

print(f'Media: {media:.1f}')
if media >= 7.0:
    print(f'Aluno aprovado.')
elif media >= 5.0:
    print('Aluno em exame.')
    exame = input()
    nota_exame = (float(exame) + media)/2
    print(f'Nota do exame: {exame}')
    if nota_exame >= 5.0:
        print(f'Aluno aprovado.')
        print(f'Media final: {nota_exame}')
    else:
        print(f'Aluno reprovado.')
        print(f'Media final: {nota_exame}')
else:
    print(f'Aluno reprovado.')
