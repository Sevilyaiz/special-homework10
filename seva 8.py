client = {}
opened_rooms = [i for i in range(1, 71)]
closed_rooms = []


# Добавление клиента
def add_client(name, room):
    client[name] = room
    opened_rooms.remove(room)
    closed_rooms.append(room)

# Выселение клиента
def del_client(name):
    closed_rooms.remove(client[name])
    opened_rooms.insert(client[name] - 1, client[name])
    client.pop(name)

# Список занятых номеров
def show_rooms():
    return closed_rooms


while True:
    choice = input('Введите действие: ')

    if choice.lower() == 'добавить':
        cl_name = input('Автомобиль заведен: ')
        print(opened_rooms)
        cl_room = int(input('Выберите номер: '))
        add_client(cl_name, cl_room)
        print(clients)
    elif choice.lower() == 'выселить':
        cl_name = input('Имя клиента: ')
        if cl_name in clients:
            del_client(cl_name)
            print(clients)
        else:
            print('Такого клиента нет!')
    elif choice.lower() == 'номера':
        print(show_rooms())
    else:
        print('Error')