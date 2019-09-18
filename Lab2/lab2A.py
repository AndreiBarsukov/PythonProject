from datetime import date

from pprint import pprint

# Функция создания сервисной книги
def сreate_book(**ownerAuto):
    book = {
        "Владелец": ownerAuto["owner"],
        "Автомобиль": ownerAuto["auto"], 
        "Технический осмотр": []
    }
    return book

# Функция добавления работы в тех. осмотр
def add_work(book, numRecord, **workData):
    book["Технический осмотр"][numRecord]["Проделанные работы"].append({
        "Наименование работы": workData["workTitle"],
        "Материалы": workData["materials"],
        "Мастер": workData["master"],
        "Стоимость, руб": workData["price"]
    })

# Функция добавления тех. осмотра в книжку
def add_record(book, **recordData):
    book["Технический осмотр"].append({
        "Дата": recordData["dateRecord"],
        "Пробег, км": recordData["mileage"],
        "Проделанные работы": [],
        "Примечание/рекомендации": recordData["recomendation"]
    })


# Данные для создания книги
dataOwner = {"auto" : {
        "Модель": "Lada Vesta",
        "Год выпуска": "2015",
        "Регистрационный номер": "е215ва159",
        "Заводской №": "109186",
        "Объем двигателя, л": "1.8",
        "Начальный пробег автоб, км": "158"
    }, "owner" : {
    "ФИО": ["Иванов", "Иван", "Иванович"],
    "Адрес": ["Россия", "Пермский край", "г.Пермь", "ул.Попова", 20, 15],
    "Телефон": "89026316888",
    "E-mail": "email@email.ru"
    }
}

# Вызов метода по созданию сервисной книги
book = сreate_book(**dataOwner)



add_record(book, dateRecord = date(2015,7,14), mileage = 10000, recomendation = "Все впорядке")

add_work(book, 0, workTitle="Замена масла", materials="Масло", master="Иванов И.И.", price="800")
add_work(book, 0, workTitle="Диагностика компьютера", materials="", master="Сидоров И.И.", price="3000")
add_work(book, 0, workTitle="Замена колес", materials="Колесо", master="Петров А.Б.", price="6500")


add_record(book, dateRecord = date(2017,7,14), mileage = 18500, recomendation = "Новая машина")

add_work(book, 1, workTitle="Диагностика двигателя", materials="", master="Прокофьев Е.В.", price="5000")
add_work(book, 1, workTitle="Замена двигателя", materials="Двигатель", master="Прокофьев Е.В.", price="30000")

# Вывод данных сервисной книги
pprint(book)

