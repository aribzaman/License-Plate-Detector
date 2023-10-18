from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from DbConifg import Base


class License(Base):
    __tablename__ = "licenses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    license = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
