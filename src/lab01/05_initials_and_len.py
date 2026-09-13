a,b,c = input('ФИО: ').split()

print(f'Инициалы: {a[0].upper()}{b[0].upper()}{c[0].upper()}.')
print(f'Длина (символов): {len(a) + len(b) + len(c) + 2}')