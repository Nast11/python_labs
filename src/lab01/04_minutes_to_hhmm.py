m = int(input('Минуты: '))
hours = (m // 60)%24
min = m % 60
print(f'{hours:02d}:{min:02d}')