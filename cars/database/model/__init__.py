from sqlalchemy import Column, Integer, Text, text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True, server_default=text("nextval('manufacturer_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    models = relationship("Model", back_populates="manufacturer")


class Model(Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))
    manufacturer = relationship("Manufacturer", back_populates="models")
