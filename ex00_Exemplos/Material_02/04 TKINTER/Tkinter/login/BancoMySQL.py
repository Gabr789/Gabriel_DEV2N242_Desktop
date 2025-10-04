import mysql.connector
from mysql.connector import Error

class BancoMySQL:
    def __init__(self):
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )
        cursor = cnx.cursor()
        cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "sistema_login";')
        num_results = cursor.fetchone()[0]
        cnx.close()

        if num_results == 0:
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password=''
            )
            cursor = cnx.cursor()
            cursor.execute('CREATE DATABASE sistema_login;')
            cnx.commit()
            cnx.close()

        try:
            self.conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='sistema_login'
            )
            self.cursor = self.conexao.cursor()
            self._criar_tabela_usuarios()
            self._criar_tabela_logins()
            self.usuario_admin()
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            raise

    def _criar_tabela_usuarios(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario VARCHAR(255) UNIQUE NOT NULL,
                senha VARCHAR(255) NOT NULL,
                perfil VARCHAR(50) NOT NULL DEFAULT 'usuário'
            )
        """)
        self.conexao.commit()

    def _criar_tabela_logins(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS logins (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario_id INT NOT NULL,
                data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
            )
        """)
        self.conexao.commit()

    def validar_credenciais(self, usuario, senha):
        query = "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s"
        self.cursor.execute(query, (usuario, senha))
        resultado = self.cursor.fetchone()
        return resultado is not None

    def registrar_login(self, usuario):
        self.cursor.execute("SELECT id FROM usuarios WHERE usuario = %s", (usuario,))
        usuario_id = self.cursor.fetchone()
        if usuario_id:
            self.cursor.execute("INSERT INTO logins (usuario_id) VALUES (%s)", (usuario_id[0],))
            self.conexao.commit()

    def salvar_usuario(self, usuario, senha, perfil='usuário'):
        query = "SELECT * FROM usuarios WHERE usuario = %s"
        self.cursor.execute(query, (usuario,))
        if self.cursor.fetchone():
            raise ValueError("Usuário já existe.")

        query = "INSERT INTO usuarios (usuario, senha, perfil) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (usuario, senha, perfil))
        self.conexao.commit()

    def usuario_admin(self):
        query = "SELECT COUNT(*) FROM usuarios WHERE usuario = %s"
        self.cursor.execute(query, ("admin",))
        resultado = self.cursor.fetchone()

        if resultado[0] == 0:
            query = "INSERT INTO usuarios (usuario, senha, perfil) VALUES (%s, %s, %s)"
            self.cursor.execute(query, ("admin", "123", "admin"))
            self.conexao.commit()
            print("Usuário 'admin' criado com sucesso.")

    def __del__(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'conexao') and self.conexao:
            self.conexao.close()