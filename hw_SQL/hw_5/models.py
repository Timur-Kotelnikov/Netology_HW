import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR)


class Book(Base):
    __tablename__ = 'book'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.VARCHAR)
    publisher_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey('publisher.id'))


class Shop(Base):
    __tablename__ = 'shop'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR)


class Stock(Base):
    __tablename__ = 'stock'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    book_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey('book.id'))
    shop_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey('shop.id'))
    count = sqlalchemy.Column(sqlalchemy.INTEGER)


class Sale(Base):
    __tablename__ = 'sale'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    price = sqlalchemy.Column(sqlalchemy.DECIMAL)
    date_of_sale = sqlalchemy.Column(sqlalchemy.DATE)
    stock_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey('stock.id'))
    count = sqlalchemy.Column(sqlalchemy.INTEGER)


#Base.metadata.create_all(bind=engine)
#Base.metadata.drop_all(bind=engine)