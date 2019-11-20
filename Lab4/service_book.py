from pyDatalog import pyDatalog

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

class Owner(Service, pyDatalog.Mixin):
    """
    Владелец автомобиля, содержит информацию о:
    ФИО, адрессе проживания, номере телефона и электронной почты
    
    """
    
    def __init__(self, fullName="", address="", phoneNum="", email=""):
        super(Owner, self).__init__()
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

class Auto(Service, pyDatalog.Mixin):
    """
    Автомобиль владельца, содержит информацию о:
    модели, годе выпуска, регистрационном номере, 
    заводском номере, объеме двигателя и начальном пробеге
    
    """

    def __init__(self, model="", year="", regNumber="", factoryNumber="", engineVolume="", startMileage=""):
        super(Auto, self).__init__()
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

class Work(Service, pyDatalog.Mixin):
    """
    Работы проделанные на тех. осмотре, содержащие информацию о:
    наименовании работы, используемых материалов, мастере, 
    выполнившем работу и стоимость проделанной работы
    
    """
    
    def __init__(self, nameWork="", materials="", master="", price=""):
        super(Work, self).__init__()
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

class Record(Service, pyDatalog.Mixin):
    """
    Записи о тех. осмотрах автомобиля, содержащие информацию о:
    дате ТО, текущем пробеге автомобиля, проделанных работах и коментарии о ТО
    
    """

    def __init__(self, date="", millage="", recomendation=""):
        super(Record, self).__init__()
        self.date = date
        self.millage = millage             
        self.recomendation = recomendation

    def __repr__(self):
        return 'Record({!r},{!r},{},{!r})'.format(
                self.date, 
                self.millage, 
                self.recomendation)        
    def __str__(self):
        return """
                Дата = {}, 
                Текущий пробег = {},  
                Коментарий = {}""".format(
                    self.date, 
                    self.millage,
                    self.recomendation )
# endregion



