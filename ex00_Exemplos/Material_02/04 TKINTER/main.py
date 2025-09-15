import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "Tkinter")))

from Tkinter.login.login import TelaLogin  
from Tkinter.login.BancoTxt import SimuladorBancoTxt
if __name__ == "__main__":
    banco = SimuladorBancoTxt()
    app =TelaLogin()
    app.iniciar()

