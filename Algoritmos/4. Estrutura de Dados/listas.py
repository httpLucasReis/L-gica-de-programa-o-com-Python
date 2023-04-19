lista = [1,2,3,4,5]

print(lista)
print(lista[0])

meses = ['janeiro', 'feveiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'outubro', 'novembro', 'dezembro']
n = 1

while (n <= 4):
    mes = int(input('Escolha um mês de 1-12:'))
    if (1 <= mes < 13):
        print(f'O mês é {meses[n-1]}')

    n+=1