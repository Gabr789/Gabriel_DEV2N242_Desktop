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

        if num_results > 0:
           pass
        else:
        
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password=''
            )
            cursor = cnx.cursor()
            cursor.execute('CREATE DATABASE sistema_login;')
            cnx.commit()

        try:
            self.conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='sistema_login'  
            )
            self.cursor = self.conexao.cursor()
            self._criar_tabela() 
            self.usuario_admin() 
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            raise

    def _criar_tabela(self):
  
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario VARCHAR(255) UNIQUE NOT NULL,
                senha VARCHAR(255) NOT NULL
            )
        """)
        self.conexao.commit()

    def validar_credenciais(self, usuario, senha):
     
        query = "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s"
        self.cursor.execute(query, (usuario, senha))
        resultado = self.cursor.fetchone()
        return resultado is not None

    def salvar_usuario(self, usuario, senha):
  
        query = "SELECT * FROM usuarios WHERE usuario = %s"
        self.cursor.execute(query, (usuario,))
        if self.cursor.fetchone():
            raise ValueError("Usuário já existe!")

 
        query = "INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)"
        self.cursor.execute(query, (usuario, senha))
        self.conexao.commit()

    def usuario_admin(self):
  
        query = "SELECT COUNT(*) FROM usuarios WHERE usuario = %s"
        self.cursor.execute(query, ("admin",))
        resultado = self.cursor.fetchone()

        if resultado[0] == 0:
            query = "INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)"
            self.cursor.execute(query, ("admin", "123"))
            self.conexao.commit()
            print("Usuário 'admin' criado com sucesso!")
        

    def __del__(self):
     
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'conexao') and self.conexao:
            self.conexao.close()