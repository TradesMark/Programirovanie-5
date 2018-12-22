'''
Галкин Антон |  ИВТ | 3 курс | 1 подгруппа
1.2 Создание пользовательского пакета для приложения
«Гостевая книга» («Регистрация на конференцию») с прототипами
методов, позволяющих взаимодействовать с JSON-файлом (создание,
удаление, переименование, чтение, запись). Формирование отчета
по практическому заданию и публикация его в портфолио.
'''


class Partisipant:
    def __init__(self):
        self.participants = list()

    """Добавление участника"""

    def Adding(self, name, surname, age, email):
        self.participants.append({"participant_name": name,
                                  "participant_surname": surname,
                                  "participant_age": age,
                                  "participant_email": email})

    """Удаление участника"""

    def Delete(self, name):
        for participant in self.participants:
            if participant.get("participant_email") == email:
                self.participants.remove(participant)

    """Запись в файл"""

    def Recorder(self):
        import json
        with open("./file.json", 'a') as file:
            json_data = {"all_participant": self.participants}
            file.write(json.dumps(json_data, indent=4))


if __name__ == "__main__":
    Book = Partisipant()
    Book.Adding("Anton", "Galkin", 20, "Figvam@gmail.com")
    Book.Recorder()