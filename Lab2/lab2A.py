from datetime import date

from pprint import pprint

import functions_book as fBook

# Данные для создания книги
dataOwner = {"auto": {
        "Модель": "Lada Vesta",
        "Год выпуска": "2015",
        "Регистрационный номер": "е215ва159",
        "Заводской №": "109186",
        "Объем двигателя, л": "1.8",
        "Начальный пробег автоб, км": "158"
    }, "owner": {
    "ФИО": ["Иванов", "Иван", "Иванович"],
    "Адрес": ["Россия", "Пермский край", "г.Пермь", "ул.Попова", 20, 15],
    "Телефон": "89026316888",
    "E-mail": "email@email.ru"
    }
}
# Вызов метода по созданию сервисной книги
book = fBook.сreate_book(**dataOwner)

fBook.add_record(book,
                 dateRecord=date(2015, 7, 14),
                 mileage=10000,
                 recomendation="Все впорядке")

fBook.add_work(book,
               0,
               workTitle="Замена масла",
               materials="Масло",
               master="Иванов И.И.",
               price="800")
fBook.add_work(book,
               0,
               workTitle="Диагностика компьютера",
               materials="",
               master="Сидоров И.И.",
               price="3000")
fBook.add_work(book,
               0,
               workTitle="Замена колес",
               materials="Колесо",
               master="Петров А.Б.",
               price="6500")
fBook.add_record(book,
                 dateRecord=date(2017, 7, 14),
                 mileage=18500,
                 recomendation="Новая машина")
fBook.add_work(book,
               1,
               workTitle="Диагностика двигателя",
               materials="",
               master="Прокофьев Е.В.",
               price="5000")
fBook.add_work(book,
               1,
               workTitle="Замена двигателя",
               materials="Двигатель",
               master="Прокофьев Е.В.",
               price="30000")

# Вывод данных сервисной книги
pprint(book)
