
#Данные об авто
auto = {
    "Модель": "Lada Vesta",
    "Год выпуска": "2015",
    "Регистрационный номер": "е215ва159",
    "Заводской №": "109186",
    "Объем двигателя, см3": "1,8",
    "Начальный пробег автоб, км": "158"
}

#Данные о владельце
ownerAuto = {
    "ФИО": ["Иванов", "Иван", "Иванович"],
    "Адрес": ["Россия", "Пермский край", "г.Пермь", "ул.Попова", 20, 15],
    "Телефон": "89026316888",
    "E-mail": "email@email.ru"
}

#Работа 1
work1 = {
   "Наименование работы": "Замена масла",
    "Материалы": ["Масло"],
    "Мастер": "Иванов И.И.",
    "Стоимость, руб": "800"
}
#Работа 2
work2 = {
    "Наименование работы": "Диагностика компьютера",
    "Материалы": [""],
    "Мастер": "Сидоров И.И.",
    "Стоимость, руб": "2500"
}
#Работа 3
work3 = {
    "Наименование работы": "Замена антифриза",
    "Материалы": ["Антифриз"],
    "Мастер": "Иванов И.И.",
    "Стоимость, руб": "500"
}
#Работа 4
work4 = {
    "Наименование работы": "Замена тормозного шланга",
    "Материалы": ["Тормозной шланг"],
    "Мастер": "Сидовров И.И.",
    "Стоимость, руб": "3500"
}

#Технический осмотр 1
recordBookAuto1 = {
    "Дата": [10,9,2019],
    "Пробег, км": "150000",
    "Проделанные работы": [
        work1,
        work2,
        work3
    ],
    "Примечание/рекомендации": "Да вроде все нормально"
}

#Технический осмотр 2
recordBookAuto2 = {
    "Дата": [12,9,2019],
    "Пробег, км": "150050.8",
    "Проделанные работы": [
        work4
    ],
    "Примечание/рекомендации": "Машину на помойку"
}

#Сервисная книга владельца автомобиля
bookAuto = {
    "Владелец": ownerAuto,
    "Автомобиль": auto, 
    "Технический осмотр": [recordBookAuto1, recordBookAuto2]
}

for bookAutoKey in bookAuto:
    #вывод данных о владельце
    if bookAutoKey == "Владелец":
       print("\r\n\tВладелец авто:".upper())
       owner = bookAuto[bookAutoKey]
       for ownerKey in owner:
            print(ownerKey, "->", owner[ownerKey])
    #вывод данных об автомобиле владельца
    elif bookAutoKey == "Автомобиль":
        print("\r\n\tАвтомобиль:".upper())
        auto = bookAuto[bookAutoKey]
        for autoKey, autoValue in auto.items():
            print(autoKey, "->", autoValue)
        print(" ")
    #вывод данных о тех. осмотрах автомобиля
    elif bookAutoKey == "Технический осмотр":
        print("\r\n\tТехнические осмотры:".upper())
        recordBook = bookAuto[bookAutoKey]
        #Перебор списка записей о ТО
        for record in recordBook:
            for dataRecordKey, dataRecordValue in record.items():
                if dataRecordKey == "Проделанные работы":
                    for works in dataRecordValue:
                        for workKey, workValue in works.items():
                            print("\t", workKey, "->", workValue)
                else:
                    print(dataRecordKey, "->", dataRecordValue)
            print("\r\n".upper())  
        print(" ")
print(" ")
