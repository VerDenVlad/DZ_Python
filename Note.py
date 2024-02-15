# -*- coding: utf-8 -*-
import json
from datetime import datetime

class NotesApp:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.load_notes_from_file()

    def save_notes_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.notes, file, ensure_ascii=False, indent=2)

    def load_notes_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def display_notes(self):
        for note in self.notes:
            print(f"ID: {note['id']}; Имя: {note['title']}; Текст: {note['body']}; Дата заметки: {note['created_at']}")

    def add_note(self, title, body):
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'body': body,
            'created_at': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        self.notes.append(note)
        print("Запись успешно добавлена!")
        self.save_notes_to_file()

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note['id'] == note_id:
                note['title'] = title
                note['body'] = body
                note['created_at'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print("Запись успешно отредактирована!")
                self.save_notes_to_file()
                return
        print("Запись не найдена.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                self.notes.remove(note)
                print("Запись успешно удалена!")
                self.save_notes_to_file()
                return
        print("Запись не найдена.")

    def filter_notes_by_date(self, date):
        filtered_notes = [note for note in self.notes if note['created_at'].startswith(date)]
        for note in filtered_notes:
            print(f"ID: {note['id']}; Имя: {note['title']}; Текст: {note['body']}; Дата заметки: {note['created_at']}")


if __name__ == "__main__":
    app = NotesApp()

    while True:
        print("\nМеню:")
        print("1. Отобразить все заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Отфильтровать заметки по дате")
        print("6. Выход")

        choice = input("Введите номер команды: ")
        print()
      
        if choice == '1':
            app.display_notes()
        elif choice == '2':
            title = input("Введите имя заметки: ")
            body = input("Введите текст заметки: ")
            app.add_note(title, body)
        elif choice == '3':
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новое название заметки: ")
            body = input("Введите новый текст заметки: ")
            app.edit_note(note_id, title, body)
        elif choice == '4':
            note_id = int(input("Введите ID заметки для редактирования: "))
            app.delete_note(note_id)
        elif choice == '5':
            date = input("Введите дату (DD-MM-YYYY): ")
            app.filter_notes_by_date(date)
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")