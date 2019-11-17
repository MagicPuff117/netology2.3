documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", 'name': "Аристарх Павлов"},
    {'type': 'passport', 'number': '122131', 'genius': 'Хидео Кодзима'}


]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def get_name(number):
    """
    Определяем имя человека по номеру документа
    """
    for document in documents:
        if document['number'] == number:
            return document['name']
    return 'Такого документа не существует!'


print(get_name('544253245524'))


def get_list():
    """
    Выведение всего списка документов
    """
    try:
        for document in documents:
            print(document['type'], document['number'], document['name'])
    except KeyError:
        print('Кодзима конечно гений, но нужно соблюдать название ключа)')
            # return document['type'], document['number'], document['name']


# print(get_list())

def get_shelf(doc_number):
    """
    Вывод номера полки по номеру документа
    """
    for shelf, number in directories.items():
        if doc_number in number:
            return shelf

        # print(get_shelf('10006'))


def delete_document_shelf_not_included(document_number):  # Какое ужасное название ))
    document_for_delete = None
    for document in documents:
        if document['number'] == document_number:
            document_for_delete = document
            break

    if document_for_delete in documents:
        documents.remove(document_for_delete)
        print('Документ успешно удален!')


def add(document_type, document_number, owner_name, shelf_number):
        documents.append({
            'type': document_type,
            'number': document_number,
            'name': owner_name,
        })


        if shelf_number in directories:
            directories[shelf_number].append(document_number)
            print('Документ добавлен')
        else:
            print('Такой полки не существует')
            question = input('Создать полку и добавить в нее документ Y/N:').lower()

            if question == 'y':
                directories[shelf_number] = []
                directories[shelf_number].append(document_number)
                print('Документ добавлен')
            else:
                document_number = input('Для отмены действия добавления введите номер введенного документа:')
                delete_document_shelf_not_included(document_number)


def delete_document(document_number):
    document_for_delete = None
    for document in documents:
        if document['number'] == document_number:
            document_for_delete = document
            break
    try:
        if document_for_delete:
            documents.remove(document_for_delete)
            directories[get_shelf(document_number)].remove(document_number)
            print('Файл удален')
        else:
            print('Такого файла не существует!')
        return
    except KeyError:
        print('Кодзима конечно гений, но нужно соблюдать название ключа)')

# print(add('passport','3415 08215','Anatoliy Vasserman','4'))

def main():
    while True:
        user_input = (input('Ввведите команду:'))
        if user_input == 'p':
            number = input('Введите номер документа:')
            print(get_name(number))
        elif user_input == 'l':
            get_list()
        elif user_input == 's':
            doc_number = input('Введите номер документа:')
            print(get_shelf(doc_number))
        elif user_input == 'a':
            document_type = input('Введите тип документа:')
            document_number = input('Введите номер документа:')
            owner_name = input('Введите владельца документа:')
            shelf_number = input('Введите номер полки:')
            add(document_type, document_number, owner_name, shelf_number)
        elif user_input == 'd':
            document_number = input('Введите номер документа для удаления:')
            delete_document(document_number)
        elif print('Пока!'):
            break


main()

def find_exception():
    try:
        for lost_name in documents:
            print(lost_name['name'])
    except KeyError:
        print('Кодзима конечно гений, но нужно соблюдать название ключа)')

# find_exception()