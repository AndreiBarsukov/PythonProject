
# Функция создания сервисной книги
def сreateBook(**ownerAuto):
    book = {
        "Владелец": ownerAuto["owner"],
        "Автомобиль": ownerAuto["auto"], 
        "Технический осмотр": list()
    }
    return book
