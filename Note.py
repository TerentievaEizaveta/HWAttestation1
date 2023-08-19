import datetime
import uuid

class Note:
    def __init__(self, id = str(uuid.uuid1())[0:2],  title = "текст", body = "текст", date = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def to_dict(self):
        return{
            "id":self.id,
            "title":self.title,
            "body":self.body,
            "date":str(self.date)
        }

    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body

    def get_date(note):
        return note.date

    def set_id(note):
        note.id = id

    def set_title(note, title):
        note.title = title

    def set_body(note, body):
        note.body = body

    def set_date(note):
        note.date = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def show_console_note(note):
        return '\nID: ' + note.id + '\n' + 'Название заметки: ' + note.title + '\n' + 'Содержание: ' + note.body + '\n' + 'Дата: ' + note.date 
