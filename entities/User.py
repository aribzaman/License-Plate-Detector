from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from DbConifg import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    __table_args__ = (UniqueConstraint("email", name="unique_email"),)
