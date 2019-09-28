
# region Блок определения классов
class Owner():
    # Класс, определяющий владельцев автомобилей
    
    def __init__(self, fullName, address, phoneNum, email):
        self.fullName = fullName
        self.address = address
        self.phoneNum = phoneNum
        self.email = email

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


