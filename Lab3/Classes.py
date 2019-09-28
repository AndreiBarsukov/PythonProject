from datetime import date

from pprint import pprint


# region Блок определения классов
class Service():
    """
    Основой класс
    
    """

    # Абстрактные методы, которые будут переопределены в классах потомках
    def __repr__(self):
        pass
    def __str__(self):
        pass

class Owner(Service):
    """
    Владелец автомобиля, содержит информацию о:
    ФИО, адрессе проживания, номере телефона и электронной почты
    
    """
    
    def __init__(self, fullName, address, phoneNum, email):
        self.fullName = fullName
        self.address = address
        self.phoneNum = phoneNum
        self.email = email

    def __repr__(self):
        return {"name": self.fullName, "age": self.address, "phoneNum": self.phoneNum, "email": self.email}   
    def __str__(self):
        return "Владелец (ФИО = " + self.fullName + ", Возраст = " + self.address + ", Номер телефона = " + self.phoneNum + ", Е-mail = " + self.email + ")"

class Auto(Service):
    """
    Автомобиль владельца, содержит информацию о:
    модели, годе выпуска, регистрационном номере, заводском номере, объеме двигателя и начальном пробеге
    
    """

    def __init__(self, model, year, regNumber, factoryNumber, engineVolume, startMileage):
        self.model = model
        self.year = year
        self.regNumber = regNumber
        self.factoryNumber = factoryNumber
        self.engineVolume = engineVolume
        self.startMileage = startMileage

    def __repr__(self):
        return {"model": self.model, "year": self.year, "regNumber": self.regNumber, "factoryNumber": self.factoryNumber, "engineVolume": self.engineVolume, "startMileage": self.startMileage}   
    def __str__(self):
        return "Автомобиль (Модель = " + self.model + ", Год выпуска = " + self.year + ", Регистрационный номер = " + self.regNumber + ", Заводской номер = " + self.factoryNumber + ", Объем двигателя = " + self.engineVolume + ", Начальный пробег = " + self.startMileage + ")"

class Work(Service):
    """
    Работы проделанные на тех. осмотре, содержащие информацию о:
    наименовании работы, используемых материалов, мастере, выполнившем работу и стоимость проделанной работы
    
    """
    
    def __init__(self, nameWork, materials, master, price):
        self.nameWork = nameWork
        self.materials = materials
        self.master = master
        self.price = price

    def __repr__(self):
        return {"nameWork": self.nameWork, "materials": self.materials, "master": self.master, "price": self.price}   
    def __str__(self):
        return "Проделанная работа (Наименование работы = " + self.nameWork + ", Использованные материалы = " + self.materials + ", Проделанные работы = " + self.master + ", Стоимость = " + self.price + ")"

class Record(Service):
    """
    Записи о тех. осмотрах автомобиля, содержащие информацию о:
    дате ТО, текущем пробеге автомобиля, проделанных работах и коментарии о ТО
    
    """

    def __init__(self, date, millage, works, recomendation):
        self.date = date
        self.millage = millage
        if (isinstance(works, Work)):
            self.works = works
        else:
            raise Exception("Не соответсвие типов передавемых данынх!")
        self.recomendation = recomendation

    def __repr__(self):
        return {"date": self.date, "millage": self.millage, "works": self.works.__repr__(), "recomendation": self.recomendation}   
    def __str__(self):
        return "Технический осмотр (Дата = " + self.date + ", Текущий пробег = " + self.millage + ", Проделанные работы = " + self.works + ", Коментарий = " + self.recomendation + ")"

class Book(Service):
    """
    Сервисная книжка автомобиля, содержащая информацию о:
    владельце, автомобиле и записях о тех. осмотрах
    
    """

    def __init__(self, owner, auto, records):
        if (isinstance(owner, Owner) and isinstance(auto, Auto) and isinstance(records, Record)):
            self.__owner = owner
            self.__auto = auto
            self.__records = records
        else:
            raise Exception("Не соответсвие типов передавемых данных!")
    
    @property
    def owner(self):
        return self.__owner
    @property
    def auto(self):
        return self.__auto
    @property
    def records(self):
        return self.__records

    @owner.setter
    def owner(self, owner):
        if (isinstance(owner, Owner)):
            self.__owner = owner
        else:
            raise Exception("Передаваемый объект не является типом класса *Owner*!")
    @auto.setter
    def auto(self, auto):
        if (isinstance(auto, Auto)):
            self.__auto = auto
        else:
            raise Exception("Передаваемый объект не является типом класса *Auto*!")
    @records.setter
    def records(self, records):
        if (isinstance(records, Record)):
            self.__records = records
        else:
            raise Exception("Передаваемый объект не является типом класса *Record*!")
            



    def addRecords(self):
        pass

    def __repr__(self):
        return {"owner": self.__owner.__repr__(), "auto": self.__auto.__repr__(), "records": self.__records.__repr__()}   
    def __str__(self):
        return "Автомобиль (Владелец автомобиля = " + self.__owner + ", Автомобиль = " + self.__auto + ", Технические осмотры = " + self.__records + ")"


# endregion

# Иллюстрация полиморфизма с функцией - общий метод вывода данных
def showDataClass(classObj):
    pprint(classObj.__repr__())

# region Блок тестирования модуля
def test():
    owner = Owner("Иванов Иван Иванович", "г.Пермь, ул. Попова, 20", "88888888888", "email@email.com")
    auto = Auto("Ford Mustang gt500", "2018", "в500ся", "500500", "1.8", "15000")
    work = Work("Замена масла", "Масло", "Петров Петр Петрович", "150")
    record = Record(date(2019,8,18), "17500",  work, "Машина в отличном состоянии")
    book = Book(owner, auto, record)



    # mro - позволяет получить иерархию наследования классов
    pprint(Book.mro())
    showDataClass(book)


if __name__ == "__main__":
    test()
# endregion
