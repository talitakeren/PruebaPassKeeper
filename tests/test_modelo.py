# tests/test_modelo.py
import unittest
from src.modelo.modelo import Usuario, Contraseña
from src.modelo.declarative_base import session, Base, engine

class TestModelo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(engine)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(engine)

    def setUp(self):
        self.session = session

    def tearDown(self):
        self.session.rollback()
        for table in reversed(Base.metadata.sorted_tables):
            self.session.execute(table.delete())
        self.session.commit()

    def test_crear_usuario(self):
        usuario = Usuario(nombre="UsuarioTest")
        self.session.add(usuario)
        self.session.commit()
        usuario_db = self.session.query(Usuario).filter_by(nombre="UsuarioTest").first()
        self.assertIsNotNone(usuario_db)

    def test_crear_contraseña(self):
        usuario = Usuario(nombre="UsuarioTest")
        self.session.add(usuario)
        self.session.commit()

        contraseña = Contraseña(usuario_id=usuario.id, servicio="TestService", nombre_usuario="UserTest", valor="password123")
        self.session.add(contraseña)
        self.session.commit()

        contraseña_db = self.session.query(Contraseña).filter_by(servicio="TestService").first()
        self.assertIsNotNone(contraseña_db)

if __name__ == '__main__':
    unittest.main()
