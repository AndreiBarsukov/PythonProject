# Функция создания сервисной книги
def сreate_book(**ownerAuto):
    book = {
        "Владелец": ownerAuto["owner"],
        "Автомобиль": ownerAuto["auto"], 
        "Технический осмотр": list()
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
