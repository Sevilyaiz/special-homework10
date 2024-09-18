# names = ['ivan', 'psha', 'jordan']
#
#
# while True:
#     new = input('ого добавить?')
#
#     if new == "Список":
#         print(names)
#
#     else:
#         names.append(new)
#         print(f'{new} добавлен')
from tkinter.font import names

# name = []
# numb = []
# uslu = []
#
# while True:
#     tok = input('Что сделать?')
#     if tok == 'Номер':
#         print(numb)
#     else:
#         numb.append(tok)
#         print(f'{tok} добавить')

# name = input('Введите имя')
# for i in name:
#     print(f'{name} Добро пожаловать')

# name = input('Введите имя')
# print(f'{name} Добро пожаловать')

#
# my_list = [1, 'a', 2,4.5]
# my = [ i + 2 for i in my_list]
#
# print(my)

# my_list = [i for  i in range(1,11,2)]
# print(my_list)

# names = ['Pasha','Sasha',bbbbbnames]
#
# print(answer)

answer = [i for i in range(1,21)]
answer2 = [r for r in answer if r % 2!=0]

print(answer2)