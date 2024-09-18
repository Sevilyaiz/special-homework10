plaer1 = input('Введитеде действие игрок1')
plaer2 = input('Введитеде действие игрок2')

if plaer1 == 'камень' and plaer2 == 'бумага':
    print('игрок2 выйграл')
elif plaer1 == 'ножницы' and plaer2 == 'бумага':
    print('игрок1 выйграл ')
elif plaer1 == 'камень' and plaer2 == 'камень':
    print('Ничья ')
elif plaer1 == 'камень' and plaer2 == 'ножницы':
    print('игрок1 выйграл')


