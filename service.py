import file_service
import Note
def menu():
    print("\nМеню:\n\n1 - добавление заметки\n2 - чтение всех заметок\n3 - редактирование заметки\n4 - удаление заметки\n5 - сортировка заметок по дате\n6 - выход\n ")

def create_note():
    title = check_len( input('Название заметки: '))
    body = check_len(input('Тело заметки: '))
    return Note.Note(title=title, body=body)


def check_len(text):
    while len(text) <= 1:
        print('Вы ввели пустую строку\n')
        text = input('Введите тескт: ')
    else:
        return text
    
def add_note():
    note = create_note()
    array = file_service.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_service.write_file(array, 'a')
    print('Заметка добавлена успешно')


def show_notes():
    temp = True
    array =file_service.read_file()
    for notes in array:
        temp = False
        print(Note.Note.show_console_note(notes))
    if temp == True:
        print('Нет заметок')


def edit_note():
    id = input('Введите id заметки: ')
    array = file_service.read_file()
    temp = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            temp = False
            note = create_note()
            Note.Note.set_title(notes, note.get_title())
            Note.Note.set_body(notes, note.get_body())
            Note.Note.set_date(notes)
            print('Изменения внесены')       
    if temp == True:
        print('Hеверный id')
    file_service.write_file(array, 'a')


def del_note():
    id = input('Введите id заметки: ')
    array = file_service.read_file()
    temp = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            temp = False
            array.remove(notes)
            print('Заметка удалена')
    if temp == True:
        print('Hеверный id')
    file_service.write_file(array, 'a')

def sort_key(note):
    return Note.Note.get_date(note)

def sort_notes():
    array = file_service.read_file()
    temp = True
    sort_arr = sorted(array, key=sort_key,reverse=True)
    for notes in sort_arr:
        temp = False
        print(Note.Note.show_console_note(notes))
    if temp == True:
        print('Ошибка сортировки ')
def exit():
    print("Выход")