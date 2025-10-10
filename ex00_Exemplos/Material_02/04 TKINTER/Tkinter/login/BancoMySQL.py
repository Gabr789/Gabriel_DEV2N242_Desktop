# pip install bcrypt
#mysqladmin -u root password
import mysql.connector
from mysql.connector import Error
import bcrypt

class BancoMySQL:
    def __init__(self):
    
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='teste'
        )
        cursor = cnx.cursor()
        cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "sistema_login";')
        num_results = cursor.fetchone()[0]
        cnx.close()

        if num_results == 0:
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='teste'
            )
            cursor = cnx.cursor()
            cursor.execute('CREATE DATABASE sistema_login;')
            cnx.commit()
            cnx.close()

        try:
            self.conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='teste',
                database='sistema_login'
            )
            self.cursor = self.conexao.cursor()
            self._criar_tabela_usuarios()
            self._criar_tabela_logins()
            self._criar_tabela_grupos()
            self._criar_grupos_padrao()
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

    def _criar_tabela_grupos(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS grupos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) UNIQUE NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuario_grupo (
                usuario_id INT NOT NULL,
                grupo_id INT NOT NULL,
                PRIMARY KEY (usuario_id, grupo_id),
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
                FOREIGN KEY (grupo_id) REFERENCES grupos(id) ON DELETE CASCADE
            )
        """)
        self.conexao.commit()

    def _criar_grupos_padrao(self):
        setores = ["alunos", "professores", "secretaria", "direção", "contabilidade", "coordenação"]
        for grupo in setores:
            self.adicionar_grupo(grupo)

    def adicionar_grupo(self, nome_grupo):
        try:
            self.cursor.execute("INSERT INTO grupos (nome) VALUES (%s)", (nome_grupo,))
            self.conexao.commit()
        except mysql.connector.IntegrityError:
            pass 

    def associar_usuario_grupo(self, usuario_id, grupo_nome):
        self.cursor.execute("SELECT id FROM grupos WHERE nome = %s", (grupo_nome,))
        grupo = self.cursor.fetchone()
        if not grupo:
            self.adicionar_grupo(grupo_nome)
            self.cursor.execute("SELECT id FROM grupos WHERE nome = %s", (grupo_nome,))
            grupo = self.cursor.fetchone()

        grupo_id = grupo[0]

       
        self.cursor.execute(
            "SELECT * FROM usuario_grupo WHERE usuario_id = %s AND grupo_id = %s",
            (usuario_id, grupo_id)
        )
        if self.cursor.fetchone():
            return

        self.cursor.execute(
            "INSERT INTO usuario_grupo (usuario_id, grupo_id) VALUES (%s, %s)",
            (usuario_id, grupo_id)
        )
        self.conexao.commit()

    def salvar_usuario(self, usuario, senha, perfil='usuário', grupo_nome=None):        
        self.cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
        if self.cursor.fetchone():
            raise ValueError("Usuário já existe.")

       
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

        self.cursor.execute(
            "INSERT INTO usuarios (usuario, senha, perfil) VALUES (%s, %s, %s)",
            (usuario, senha_hash, perfil)
        )
        self.conexao.commit()

        self.cursor.execute("SELECT id FROM usuarios WHERE usuario = %s", (usuario,))
        usuario_id = self.cursor.fetchone()[0]

        if grupo_nome:
            self.associar_usuario_grupo(usuario_id, grupo_nome)

    def validar_credenciais(self, usuario, senha):
        query = "SELECT senha FROM usuarios WHERE usuario = %s"
        self.cursor.execute(query, (usuario,))
        resultado = self.cursor.fetchone()
        if resultado:
            senha_hash = resultado[0]
            return bcrypt.checkpw(senha.encode(), senha_hash.encode())
        return False

    def registrar_login(self, usuario):
        self.cursor.execute("SELECT id FROM usuarios WHERE usuario = %s", (usuario,))
        usuario_id = self.cursor.fetchone()
        if usuario_id:
            self.cursor.execute("INSERT INTO logins (usuario_id) VALUES (%s)", (usuario_id[0],))
            self.conexao.commit()

    def usuario_admin(self):
        self.cursor.execute("SELECT COUNT(*) FROM usuarios WHERE usuario = %s", ("admin",))
        if self.cursor.fetchone()[0] == 0:
            senha_hash = bcrypt.hashpw("123".encode(), bcrypt.gensalt()).decode()
            self.cursor.execute(
                "INSERT INTO usuarios (usuario, senha, perfil) VALUES (%s, %s, %s)",
                ("admin", senha_hash, "administrador")
            )
            self.conexao.commit()
            self.cursor.execute("SELECT id FROM usuarios WHERE usuario = %s", ("admin",))
            admin_id = self.cursor.fetchone()[0]
            self.associar_usuario_grupo(admin_id, "direção")
            print("Usuário 'admin' criado com sucesso.")

    def obter_grupos_usuario(self, usuario):
        query = """
            SELECT g.nome FROM grupos g
            JOIN usuario_grupo ug ON g.id = ug.grupo_id
            JOIN usuarios u ON u.id = ug.usuario_id
            WHERE u.usuario = %s
        """
        self.cursor.execute(query, (usuario,))
        return [row[0] for row in self.cursor.fetchall()]

    def __del__(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'conexao') and self.conexao:
            self.conexao.close()