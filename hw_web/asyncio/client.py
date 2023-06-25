from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import SwapiPeople

PG_DSN = 'postgresql://app:12345@127.0.0.1:5431/hw_asyncio'
engine = create_engine(url=PG_DSN)
Session = sessionmaker(bind=engine)


with Session() as session:
    print([i.name for i in session.query(SwapiPeople).filter(SwapiPeople.mass <= '80').
          filter(SwapiPeople.mass >= '60').filter(SwapiPeople.height <= '175').all()])



