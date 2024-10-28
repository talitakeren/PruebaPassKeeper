# src/modelo/modelo.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    contraseñas = relationship("Contraseña", back_populates="usuario")

class Contraseña(Base):
    __tablename__ = 'contraseñas'

    id = Column(Integer, primary_key=True)
    servicio = Column(String, nullable=False)
    nombre_usuario = Column(String, nullable=False)
    valor = Column(String, nullable=False)  # Contraseña cifrada
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship("Usuario", back_populates="contraseñas")

class PreguntaSeguridad(Base):
    __tablename__ = 'preguntas_seguridad'

    id = Column(Integer, primary_key=True)
    pregunta = Column(String, nullable=False)
    respuesta = Column(String, nullable=False)  # Respuesta cifrada
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))

# Crear las tablas en la base de datos
if __name__ == "__main__":
    from src.modelo.declarative_base import engine, Base
    Base.metadata.create_all(engine)

