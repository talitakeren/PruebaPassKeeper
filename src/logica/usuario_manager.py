# src/controller/usuario_manager.py
from src.modelo.modelo import Usuario
from src.modelo.declarative_base import session

class UsuarioManager:
    def __init__(self, session):
        self.session = session

    def crear_usuario(self, nombre):
        usuario = Usuario(nombre=nombre)
        self.session.add(usuario)
        self.session.commit()
        return usuario

    def leer_usuario(self, usuario_id):
        return self.session.query(Usuario).filter_by(id=usuario_id).first()

    def eliminar_usuario(self, usuario_id):
        usuario = self.leer_usuario(usuario_id)
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
        return usuario
