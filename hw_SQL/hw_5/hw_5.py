import sqlalchemy
from sqlalchemy.orm import sessionmaker
import json
import models

with open(file='credentials') as credentials:
    username = credentials.readline().strip()
    password = credentials.readline().strip()
    database = credentials.readline().strip()


engine = sqlalchemy.create_engine(url=f'postgresql://{username}:{password}@localhost:5432/{database}')
Session = sessionmaker(bind=engine)
session = Session()


def load_from_json(some_file):
    with open(file=some_file, encoding='utf-8') as f:
        data = json.load(fp=f)
        for i in data:
            if i['model'] == 'publisher':
                publisher = models.Publisher(id=i['pk'], name=i['fields']['name'])
                session.add(publisher)
            if i['model'] == 'book':
                book = models.Book(id=i['pk'], title=i['fields']['title'], publisher_id=i['fields']['id_publisher'])
                session.add(book)
            if i['model'] == 'shop':
                shop = models.Shop(id=i['pk'], name=i['fields']['name'])
                session.add(shop)
            if i['model'] == 'stock':
                stock = models.Stock(id=i['pk'], book_id=i['fields']['id_book'], shop_id=i['fields']['id_shop'],
                                     count=i['fields']['count'])
                session.add(stock)
            if i['model'] == 'sale':
                sale = models.Sale(id=i['pk'], price=i['fields']['price'], date_of_sale=i['fields']['date_sale'],
                                   stock_id=i['fields']['id_stock'], count=i['fields']['count'])
                session.add(sale)
            session.commit()


#load_from_json('test_data.json')


def select_publisher_by_id():
    pub_id = int(input('Type publisher id: '))
    publisher = session.query(models.Publisher).filter(models.Publisher.id == pub_id).first()
    return f'Publisher name is {publisher.name}'


def select_shop_by_publisher_id():
    pub_id = int(input('Type publisher id: '))
    result = list()
    book = session.query(models.Book).filter(models.Book.publisher_id == pub_id).subquery()
    stock = session.query(models.Stock).join(book, models.Stock.book_id == book.c.id).subquery()
    shop = session.query(models.Shop).join(stock, models.Shop.id == stock.c.shop_id).all()
    for c in shop:
        result.append(c.name)
    return f'Shop list = {result}'


#print(select_publisher_by_id())
#print(select_shop_by_publisher_id())