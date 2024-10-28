# tests/test_controller.py
import unittest
from src.logica.usuario_manager import UsuarioManager
from src.logica.contaseña_manager import ContraseñaManager
from src.modelo.declarative_base import session, Base, engine
from src.modelo.modelo import Usuario, Contraseña

class TestController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(engine)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(engine)

    def setUp(self):
        self.session = session
        self.usuario_manager = UsuarioManager(self.session)
        self.contraseña_manager = ContraseñaManager(self.session)

    def tearDown(self):
        self.session.rollback()
        for table in reversed(Base.metadata.sorted_tables):
            self.session.execute(table.delete())
        self.session.commit()

    def test_crear_y_leer_usuario(self):
        usuario = self.usuario_manager.crear_usuario("UsuarioTest")
        usuario_db = self.usuario_manager.leer_usuario(usuario.id)
        self.assertIsNotNone(usuario_db)
        self.assertEqual(usuario_db.nombre, "UsuarioTest")

    def test_agregar_y_leer_contraseña(self):
        usuario = self.usuario_manager.crear_usuario("UsuarioTest")
        contraseña = self.contraseña_manager.agregar_contraseña(usuario.id, "TestService", "UserTest", "password123")
        contraseña_db = self.contraseña_manager.leer_contraseña(contraseña.id)
        self.assertIsNotNone(contraseña_db)
        self.assertEqual(contraseña_db.servicio, "TestService")

if __name__ == '__main__':
    unittest.main()
