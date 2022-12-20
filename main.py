import math
result = 0
p = 0
i = 1
count = int(input('Введите количество источников шума: '))

for i in range(1, count+1):
    print(' ')
    L = float(input('Введите уровень шума на расстоянии 1м: '))
    R = float(input('Введите расстояние до рассчётной точки: '))
    L = L + 20*(math.log10(1/(R*R)))
    p += 10**(L/20)
    print('Найденный уровень шума: ', L)

print('')
result = 20*(math.log10(p))
print('Общий уровень шума:', result)
