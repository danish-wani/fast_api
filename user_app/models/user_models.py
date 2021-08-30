from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from datetime import datetime
from sqlalchemy.sql.sqltypes import Integer, String, DateTime


BaseModel = declarative_base()


class AuditModel:
    created_on = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_on = Column(DateTime, default=datetime.utcnow, nullable=False)


class User(AuditModel, BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, nullable=False, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    city = Column(String(100))
    profession = Column(String(50))
