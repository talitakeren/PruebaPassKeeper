# src/controller/contraseña_manager.py
from src.modelo.modelo import Contraseña
from src.modelo.declarative_base import session

class ContraseñaManager:
    def __init__(self, session):
        self.session = session

    def agregar_contraseña(self, usuario_id, servicio, nombre_usuario, valor):
        contraseña = Contraseña(usuario_id=usuario_id, servicio=servicio, nombre_usuario=nombre_usuario, valor=valor)
        self.session.add(contraseña)
        self.session.commit()
        return contraseña

    def leer_contraseña(self, contraseña_id):
        return self.session.query(Contraseña).filter_by(id=contraseña_id).first()

    def eliminar_contraseña(self, contraseña_id):
        contraseña = self.leer_contraseña(contraseña_id)
        if contraseña:
            self.session.delete(contraseña)
            self.session.commit()
        return contraseña
