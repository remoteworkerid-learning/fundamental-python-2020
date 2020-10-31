print('Tipe Data Skalar')
anak1 = 'Eko'
anak2 = 'Dwi'

print(anak1)
print(anak2)

print('\nTipe Data List')
anak = ['Eko','Dwi', 'Tri', 'Catur']
print(anak)
anak.append('Limo')
print(anak)

print('\nSapa Anak ke-2')
print(f'Hai {anak[1]}!')

print('\nsapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nsapa semua anak cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. hai {anak[a]}!')

