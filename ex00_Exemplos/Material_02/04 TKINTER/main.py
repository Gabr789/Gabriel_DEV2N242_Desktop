import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "Tkinter")))

from Tkinter.login.login import TelaLogin  
from Tkinter.login.BancoMySQL import BancoMySQL
if __name__ == "__main__":
    banco = BancoMySQL()
    app = TelaLogin(banco)
    app.iniciar()

