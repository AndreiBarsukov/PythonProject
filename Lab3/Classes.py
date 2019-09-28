from pprint import pprint

# region Блок определения классов
class Owner():
    # Класс, определяющий владельцев автомобилей
    
    def __init__(self, fullName, address, phoneNum, email):
        self.fullName = fullName
        self.address = address
        self.phoneNum = phoneNum
        self.email = email

    def __repr__(self):
        return {"name": self.fullName, "age": self.address, "phoneNum": self.phoneNum, "email": self.email}
    def __str__(self):
        return "Владелец (ФИО = " + self.fullName + ", Возраст = " + self.address + ", Номер телефона = " + self.phoneNum + ", Е-mail = " + self.email + ")"

class Auto():
    # Класс, определяющий автомобили владельцев

    def __init__(self, model, year, regNumber, factoryNumber, engineVolume, startMileage):
        self.model = model
        self.year = year
        self.regNumber = regNumber
        self.factoryNumber = factoryNumber
        self.engineVolume = engineVolume
        self.startMileage = startMileage

class Book():
    # Класс, определяющий книгу тех. осмотров

    def __init__(self, owner, auto, records):
        self.owner = owner
        self.auto = auto
        self.records = records
    

class Record():
    # Класс, определяющий тех. осмотры в книжке

    def __init__(self, date, millage, works, recomendation):
        self.date = date
        self.millage = millage
        self.works = works
        self.recomendation = recomendation

class Work():
    # Класс, определяющий работы тех. осмотров
    
     def __init__(self, nameWork, materials, master, price):
        self.nameWork = nameWork
        self.materials = materials
        self.master = master
        self.price = price
# endregion

# region Блок тестирования модуля
def test():
    owner = Owner("owner", "2", "3", "4")
    auto = Auto("auto", "1", "1", "1", "1", "1")
    work = Work("word", "4", "4", "4")
    record = Record("record", "3", "3", "3")
    book = Book(owner, auto, record)

    pprint(owner.__repr__())


if __name__ == "__main__":
    test()
# endregion
