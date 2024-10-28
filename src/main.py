# src/main.py
from src.modelo.declarative_base import Base, engine
from src.logica.usuario_manager import UsuarioManager
from src.logica.contaseña_manager import ContraseñaManager

if __name__ == "__main__":
    # Crear la base de datos
    Base.metadata.create_all(engine)

    # Ejemplo de uso de UsuarioManager y ContraseñaManager
    usuario_manager = UsuarioManager()
    contraseña_manager = ContraseñaManager()

    # Añade usuarios y contraseñas según sea necesario
