all_product = {'Весь склад': {}}


admin = input('Что вы хотите сделать? ')
if admin.upper() == 'Добавить' :
    product_name = input('Введите название продукта: ')
    product_count = input('Введите количество: ')
    all_product['Весь склад'] [product_name] = product_count
    print('Продукт добавлен')
elif admin.upper() == 'Продукты' :
    print(all_product)
chto_kupit = input('korzina')
print(korzina)

# all_products = {'Весь склад': {}}
# korzina = []
#
# while True:
#     admin = input('Выберите действие: ')
#     if admin.upper() == 'ДОБАВИТЬ':
#         product_name = input('Введите название продукта: ')
#         product_count = int(input('Введите кол-во продукта: '))
#         all_products['Весь склад'][product_name] = product_count
#         print('Продукт добавлен!')
#     elif admin.upper() == 'ПРОДУКТЫ':
#         print(all_products)
#     elif admin.upper() == 'КУПИТЬ':
#         print(all_products)
#         # Выбор товара ДЛЯ ПОКУПКИ
#         pr_name = input('Выберите продукт: ')
#         # Выбор кол-ва товара ДЛЯ ПОКУПКИ
#         pr_count = int(input('Выберите количество продукта: '))
#         # Проверка есть ли товар на складе и его кол-во превышает то, которое покупает пользователь
#         if pr_name in all_products['Весь склад'] and all_products['Весь склад'][pr_name] >= pr_count:
#             # Собираем заказа
#             new_order = (pr_name, pr_count)
#             # Добавляем в корзину
#             korzina.append(new_order)
#             # Минусуем товар со склада
#             all_products['Весь склад'][pr_name] -= pr_count
#             print('Товар успешно помещен в корзину!')
#     else:
#         print('Error')
from re import search