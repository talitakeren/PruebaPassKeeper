# src/modelo/declarative_base.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///gestor_contraseñas.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
