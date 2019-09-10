
auto = {
    "Модель": "Lada Vesta",
    "Год выпуска": "2015",
    "Регистрационный номер": "е215ва159",
    "Заводской №": "109186",
    "Объем двигателя, см3": "1,8",
    "Начальный пробег автоб, км": "158"
}

ownerAuto = {
    "ФИО": ["Иванов", "Иван", "Иванович"],
    "Адрес": ["Россия", "Пермский край", "г.Пермь", "ул.Попова", 20, 15],
    "Телефон": "89026316888",
    "E-mail": "email@email.ru"
}

bookAuto = {
    "Владелец": ownerAuto,
    "Автомобиль": auto,
    "Дата": [10,9,2019],
    "Пробег, км": "150000",
    "Выполненная работа": "Замена масла",
    "Материалы": "Масло",
    "Мастер": "Иванов И.И.",
    "Стоимость работ": "2500",
    "Примечание/рекомендации": "Хорошее масло"
}


for bookAutoKey in bookAuto:
    if bookAutoKey == "Владелец":
       print("\r\nВладелец авто:")
       for ownerAutokey in ownerAuto:
            print(ownerAutokey, "->", ownerAuto[ownerAutokey])
    if bookAutoKey == "Автомобиль":
        print("\r\nАвтомобиль:")
        for autoKey in auto:
            print(autoKey, "->", auto[autoKey])
        print(" ")
    elif bookAutoKey != "Владелец" and bookAutoKey != "Автомобиль":
        print(bookAutoKey, "->", bookAuto[bookAutoKey])

print(" ")
