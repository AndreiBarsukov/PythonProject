import service_book as serv_book

from datetime import date

from pprint import pprint

from pyDatalog import pyDatalog


# Через предикаты можно искать количество ТО, суммарную стоимость всех ТО, минимальную стоимость то, количество хозяев у машины, выодить самих хозяев 

pyDatalog.create_terms('X, Y, Z, H, book_contains, work_included, has_car, count_records, works_auto')


def main():
    owner0 = serv_book.Owner(
        "Иванов Иван Иванович", 
        "г.Пермь, ул. Попова, 20", 
        "88888888888", 
        "email@email.com")
    owner1 = serv_book.Owner(
        "Колоколова Лекса Алексеевна", 
        "г.Березники, ул. Мира, 15", 
        "88888888899", 
        "emailmail@email.com")
    owner2 = serv_book.Owner(
        "Сигачева Инесса Павловна", 
        "г.Пермь, ул. Попова, 20", 
        "88888888889", 
        "mail@email.com")
 
    auto0 = serv_book.Auto(
        "Ford Mustang gt500", 
        "2018", 
        "в500ся", 
        "500500", 
        "1.8", 
        "15000")
    auto1 = serv_book.Auto(
        "Ferrari 458 Italia", 
        "2013", 
        "в600ся", 
        "600600", 
        "1.8", 
        "16000")
    auto2 = serv_book.Auto(
        "Ferrari 458 Italia", 
        "2013", 
        "в600ся", 
        "600600", 
        "1.8", 
        "16000")

    work0 = serv_book.Work(
        "Замена масла", 
        "Масло", 
        "Петров Петр Петрович", 
        "150")
    work1 = serv_book.Work(
        "Смена шин", 
        "Зимние шины", 
        "Петров Петр Петрович", 
        "12000")
    work2 = serv_book.Work(
        "Замена передних фар", 
        "Передние фары", 
        "Сидоров Иван Иванович", 
        "2000")
    work3 = serv_book.Work(
        "Замена задних фар", 
        "Задние фары", 
        "Кожевников Виктор Сергеевич ", 
        "2500")

    record0 = serv_book.Record(
        date(2019,8,18), 
        "17500",  
        "Машина в отличном состоянии")
    record1 = serv_book.Record(
        date(2019,8,19), 
        "21000",  
        "Все хорошо")
    record2 = serv_book.Record(
        date(2019,8,15), 
        "25000",  
        "Довольно неплохо")
    

    print('\n--------VVV----- pyDatalog -------VVV------\n')
    
    # Формирование фактов
    + has_car(owner0, auto0)
    + has_car(owner1, auto1)
    + has_car(owner2, auto2)

    + (work_included[work0] == record0)
    + (work_included[work1] == record0)
    + (work_included[work2] == record1)
    + (work_included[work3] == record2)

    + (book_contains[record0] == auto0)
    + (book_contains[record1] == auto0)
    + (book_contains[record2] == auto2)


    print('\n-------^^^------ pyDatalog ------^^^-------\n')

if __name__ == "__main__":
    main()


