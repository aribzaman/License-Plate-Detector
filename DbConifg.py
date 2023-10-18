from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

db_url = "mysql://root:root@localhost/lpd"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()
