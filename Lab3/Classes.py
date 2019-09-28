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
    #{!r} - внутреннее представление ('test1') {!s} - человеческое представление (test1)
    def __repr__(self):        
        return 'Owner({!r},{!r},{!r},{!r})'.format(self.fullName, self.address, self.phoneNum, self.email)
    def __str__(self):
        return "\n ФИО = {}, \n Возраст = {}, \n Номер телефона = {}, \n Е-mail = {})".format(self.fullName, self.address, self.phoneNum, self.email)

class Auto(Service):
    """
    Автомобиль владельца, содержит информацию о:
    модели, годе выпуска, регистрационном номере, заводском номере, объеме двигателя и начальном пробеге
    
    """

    def __init__(self, model="", year="", regNumber="", factoryNumber="", engineVolume="", startMileage=""):
        self.model = model
        self.year = year
        self.regNumber = regNumber
        self.factoryNumber = factoryNumber
        self.engineVolume = engineVolume
        self.startMileage = startMileage
    
    def __repr__(self):
        return 'Auto({!r},{!r},{!r},{!r},{!r},{!r})'.format(self.model, self.year, self.regNumber, self.factoryNumber, self.engineVolume, self.startMileage)
    def __str__(self):
        return "\n Модель =  {}, \n Год выпуска = {}, \n Регистрационный номер = {}, \n Заводской номер = {}, \n Объем двигателя = {}, \n Начальный пробег = {})".format(self.model, self.year, self.regNumber, self.factoryNumber, self.engineVolume, self.startMileage)

class Work(Service):
    """
    Работы проделанные на тех. осмотре, содержащие информацию о:
    наименовании работы, используемых материалов, мастере, выполнившем работу и стоимость проделанной работы
    
    """
    
    def __init__(self, nameWork="", materials="", master="", price=""):
        self.nameWork = nameWork
        self.materials = materials
        self.master = master
        self.price = price

    def __repr__(self):
        return 'Work({!r},{!r},{!r},{!r})'.format(self.nameWork, self.materials, self.master, self.price)
    def __str__(self):
        return "\n    [Наименование работы = {}, \n    Использованные материалы = {}, \n    Проделанные работы = {} \n    Стоимость = {}]\n".format(self.nameWork, self.materials, self.master, self.price)

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
        return 'Record({!r},{!r},{},{!r})'.format(self.date, self.millage, self.works.__repr__(), self.recomendation)        
    def __str__(self):
        return '\n Дата = {}, \n Текущий пробег = {}, \n Проделанные работы: {} Коментарий = {})\n'.format(self.date, self.millage, ''.join(str(x) for x in self.works), self.recomendation )

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
        return "Book({},{},{})".format(self.__owner.__repr__(), self.__auto.__repr__(), self.__records.__repr__())
    
    def __str__(self):
        return "\nВладелец автомобиля: {}, \n\nАвтомобиль: {}, \n\nТехнические осмотры: {})".format(self.__owner, self.__auto, ''.join(str(x) for x in self.__records))


# endregion

# Иллюстрация полиморфизма с функцией - общий метод вывода данных
def showDataClass(classObj):
    print(classObj.__repr__())

# region Блок тестирования модуля
def test():
    owner = Owner("Иванов Иван Иванович", "г.Пермь, ул. Попова, 20", "88888888888", "email@email.com")
    auto = Auto("Ford Mustang gt500", "2018", "в500ся", "500500", "1.8", "15000")
    work = Work("Замена масла", "Масло", "Петров Петр Петрович", "150")
    work2 = Work("2", "Новое", "Владимир Константинович Ватников", "15550")
    work3 = Work("3", "Старно", "Иванов Петр Иванович", "5450")
    work4 = Work("4", "Что то еще", "Кто-то Ктоевич Ктотов", "100")
    record = Record(date(2019,8,18), "17500",  [work, work2], "Машина в отличном состоянии")

    book = Book(owner, auto, [record])
    rec1 = Record(date(2019,8,18), "1", [work2], "1" )
    book.addRecords(rec1)
    book.records[1].addWork(work3)
    book.records[1].addWork(work4)
    #print(book)
    
    # mro - позволяет получить иерархию наследования классов
    #pprint(Book.mro())
    showDataClass(book)  
    
    book2 = Book(
    Owner('Иванов Иван Иванович','г.Пермь, ул. Попова, 20','88888888888','email@email.com'),
    Auto('Ford Mustang gt500','2018','в500ся','500500','1.8','15000'),
        [
        Record(
            date(2019, 8, 18),
            '17500',
            [
                Work('Замена масла','Масло','Петров Петр Петрович','150'),
                Work('2','Новое','Владимир Константинович Ватников','15550')
            ],
            'Машина в отличном состоянии'),
        Record(
            date(2019, 8, 18),
            '1',
            [
                Work('2','Новое','Владимир Константинович Ватников','15550'), 
                Work('3','Старно','Иванов Петр Иванович','5450'), 
                Work('4','Что то еще','Кто-то Ктоевич Ктотов','100')
            ],
            '1')
        ])
    print(book2)
    
if __name__ == "__main__":
    test()
# endregion
