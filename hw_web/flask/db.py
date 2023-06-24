import atexit
from sqlalchemy import Column, String, Integer, DateTime, create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

PG_DSN = 'postgresql://app:12345@127.0.0.1:5431/hw_flask'

engine = create_engine(url=PG_DSN)

Base = declarative_base()
Session = sessionmaker(bind=engine)

atexit.register(engine.dispose)


class Adv(Base):
    __tablename__ = 'app_adv'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())


Base.metadata.create_all(bind=engine)
