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
    
    def __init__(self, fullName="", address="", phoneNum="", email=""):
        self.fullName = fullName
        self.address = address
        self.phoneNum = phoneNum
        self.email = email
    # {!r} - внутреннее представление ('test1') {!s} - человеческое представление (test1)
    def __repr__(self):        
        return 'Owner({!r},{!r},{!r},{!r})'.format(
                self.fullName, 
                self.address, 
                self.phoneNum, 
                self.email)
    def __str__(self):
        return """\n ФИО = {},
                Возраст = {},
                Номер телефона = {},
                Е-mail = {}""".format(
                    self.fullName,
                    self.address, 
                    self.phoneNum, 
                    self.email)

class Auto(Service):
    """
    Автомобиль владельца, содержит информацию о:
    модели, годе выпуска, регистрационном номере, 
    заводском номере, объеме двигателя и начальном пробеге
    
    """

    def __init__(self, model="", year="", regNumber="", factoryNumber="", engineVolume="", startMileage=""):
        self.model = model
        self.year = year
        self.regNumber = regNumber
        self.factoryNumber = factoryNumber
        self.engineVolume = engineVolume
        self.startMileage = startMileage
    
    def __repr__(self):
        return 'Auto({!r},{!r},{!r},{!r},{!r},{!r})'.format(
                self.model, 
                self.year, 
                self.regNumber, 
                self.factoryNumber, 
                self.engineVolume, 
                self.startMileage)
    def __str__(self):
        return """\n Модель =  {},
                Год выпуска = {},
                Регистрационный номер = {}, 
                Заводской номер = {}, 
                Объем двигателя = {}, 
                Начальный пробег = {}""".format(
                    self.model,
                    self.year, 
                    self.regNumber, 
                    self.factoryNumber, 
                    self.engineVolume, 
                    self.startMileage)

class Work(Service):
    """
    Работы проделанные на тех. осмотре, содержащие информацию о:
    наименовании работы, используемых материалов, мастере, 
    выполнившем работу и стоимость проделанной работы
    
    """
    
    def __init__(self, nameWork="", materials="", master="", price=""):
        self.nameWork = nameWork
        self.materials = materials
        self.master = master
        self.price = price

    def __repr__(self):
        return 'Work({!r},{!r},{!r},{!r})'.format(
                self.nameWork, 
                self.materials, 
                self.master, 
                self.price)
    def __str__(self):
        return """
                [Наименование работы = {}, 
                Использованные материалы = {}, 
                Проделанные работы = {} 
                Стоимость = {}]""".format(
                                self.nameWork, 
                                self.materials, 
                                self.master, 
                                self.price)

class Record(Service):
    """
    Записи о тех. осмотрах автомобиля, содержащие информацию о:
    дате ТО, текущем пробеге автомобиля, проделанных работах и коментарии о ТО
    
    """

    def __init__(self, date="", millage="", works=[Work()], recomendation=""):
        self.date = date
        self.millage = millage        
        self.works = works        
        self.recomendation = recomendation

    def __repr__(self):
        return 'Record({!r},{!r},{},{!r})'.format(
                self.date, 
                self.millage, 
                self.works.__repr__(), 
                self.recomendation)        
    def __str__(self):
        return """
                Дата = {}, 
                Текущий пробег = {}, 
                Проделанные работы: {} 
                Коментарий = {}""".format(
                    self.date, 
                    self.millage, 
                    ''.join(str(x) for x in self.works), 
                    self.recomendation )

    def addWork(self, newWork):
        if (isinstance(newWork, Work)):
            self.works.append(newWork)        
        else:
            raise Exception("Добавляемый объект не является типом класса *Work*!")

class Book(Service):
    """
    Сервисная книжка автомобиля, содержащая информацию о:
    владельце, автомобиле и записях о тех. осмотрах
    
    """

    def __init__(self, owner=Owner(), auto=Auto(), records=[Record()]):
        if (isinstance(owner, Owner) and isinstance(auto, Auto)):
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
        #if (isinstance(records, Record)):
            self.__records = records
        #else:
        #    raise Exception("Передаваемый объект не является типом класса *Record*!")
            
    def addRecords(self, newRecord):
        if (isinstance(newRecord, Record)):
            self.__records.append(newRecord)        
        else:
            raise Exception("Добавляемый объект не является типом класса *Record*!")

    def __repr__(self):
        return "Book({},{},{})".format(
                self.__owner.__repr__(), 
                self.__auto.__repr__(), 
                self.__records.__repr__())
    def __str__(self):
        return """
                Владелец автомобиля: {},
                Автомобиль: {},
                Технические осмотры: {}""".format(
                    self.__owner, 
                    self.__auto, 
                    ''.join(str(x) for x in self.__records))

# endregion

# Иллюстрация полиморфизма с функцией - общий метод вывода данных
def showDataClass(classObj):
    print(classObj.__repr__())

# region Блок тестирования модуля
def test():
    pass
    owner = Owner(
        "Сидоров Сидр Сидорович", 
        "г.Пермь, ул. Уральская, 20", 
        "89999999999", 
        "email@ya.ru")
    auto = Auto(
        "DeLorean DMC-12", 
        "1982", 
        "в600ся", 
        "600600", 
        "2.8", 
        "1250000")
    work = Work(
        "Замена масла", 
        "Масло", 
        "Шуриков Анатолий Иванович", 
        "150")
    work2 = Work(
        "Замена колодок", 
        "Колодки", 
        "Шушиков Иван Сергеевич", 
        "500")
    record = Record(
        date(2019,8,18), 
        "1250350",  
        [work, work2], 
        "Раритет, а не машина")
    book = Book(owner, auto, [record])
    showDataClass(book)

    work3 = Work(
        "Замена тормозных дисков", 
        "Тормозные диски", 
        "Шушиков Иван Сергеевич", 
        "1500")
    record1 = Record(
        date(2019,8,25), 
        "1250680", 
        list(), 
        "Пора на свалку" )
    book.addRecords(record1)
    print("\n")
    showDataClass(book)
    book.records[1].addWork(work3)
    print("\n")
    showDataClass(book)
    
    # mro - позволяет получить иерархию наследования классов
    print("\n")
    pprint(Book.mro())
   
if __name__ == "__main__":
    test()
# endregion
