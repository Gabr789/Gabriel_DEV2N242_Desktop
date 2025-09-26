import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "Tkinter")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox,ttk




from menu_interativo.informativo import TelaInformativa
from widgets.widgets_basicos.menu_botao.botao import TelaBotoes
from widgets.widgets_basicos.menu_label.label import TelaLabel
from widgets.widgets_basicos.menu_frame.frame import TelaFrame

from widgets.widgets_entrada.menu_entrada.entrada import TelaEntry
from widgets.widgets_entrada.menu_combo.combo import TelaCombobox
from widgets.widgets_entrada.menu_text.text import TelaText
from widgets.widgets_entrada.menu_spinbox.spin import TelaSpinbox
from widgets.widgets_entrada.menu_scale.scale import TelaScale

from widgets.widgets_selecao.menu_radio.radio import TelaRadiobutton    
from widgets.widgets_selecao.menu_check.check import TelaCheckbutton
from widgets.widgets_selecao.menu_list.list import TelaListbox

from widgets.widgets_interface.menu.menu import TelaMenu

from widgets.widgets_ttk.arvore.treeview import TelaTreeview

from eventos_Interacoes.mouse.menu_clique.clique import TelaEventoClick
from eventos_Interacoes.mouse.menu_entrada_saida.entrada_saida import TelaEventoEnterLeave
from eventos_Interacoes.mouse.menu_movimentomouse.movimentomouse import TelaEventoMotion

from eventos_Interacoes.teclado.menu_teclas.login_enter import TelaLoginEnter
from eventos_Interacoes.teclado.menu_teclas.teclas import TelaEventoTecla
from eventos_Interacoes.teclado.menu_atalho_teclado.atalho_teclado import TelaAtalhosTeclado

from layouts.menu_place.place import TelaPlace
from layouts.meu_pack.pack import TelaPack
from layouts.menu_grid.grid import TelaGrid

from estilos.estilos import Estilos

from exercicios.exercicios04.exercicio01.exercicio01 import Ex1
from exercicios.exercicios04.exercicio02.exercicio02 import Ex2
from exercicios.exercicios04.exercicio03.exercicio03 import Ex3
from exercicios.exercicios04.exercicio04.exercicio04 import Ex4
from exercicios.exercicios04.exercicio05.exercicio05 import Ex5
from exercicios.exercicios04.exercicio06.exercicio06 import Ex6
from exercicios.exercicios04.exercicio07.exercicio07 import Ex7
from exercicios.exercicios04.exercicio08.exercicio08 import Ex8
from exercicios.exercicios04.exercicio09.exercicio09 import Ex9
from exercicios.exercicios04.exercicio10.exercicio10 import Ex10

from exercicios.exercicios05.exercicio01.exercicio01 import Ex1_5
from exercicios.exercicios05.exercicio02.exercicio02 import Ex2_5
from exercicios.exercicios05.exercicio03.exercicio03 import Ex3_5
from exercicios.exercicios05.exercicio04.exercicio04 import Ex4_5
from exercicios.exercicios05.exercicio05.exercicio05 import Ex5_5
from exercicios.exercicios05.exercicio06.exercicio06 import Ex6_5
from exercicios.exercicios05.exercicio07.exercicio07 import Ex7_5
from exercicios.exercicios05.exercicio08.exercicio08 import Ex8_5
from exercicios.exercicios05.exercicio09.exercicio09 import Ex9_5
from exercicios.exercicios05.exercicio10.exercicio10 import Ex10_5

from exercicios.exercicios07.exercicio01.exercicio01 import Ex1_7
from exercicios.exercicios07.exercicio02.exercicio02 import Ex2_7
from exercicios.exercicios07.exercicio03.exercicio03 import Ex3_7
from exercicios.exercicios07.exercicio04.exercicio04 import Ex4_7
from exercicios.exercicios07.exercicio05.exercicio05 import Ex5_7
from exercicios.exercicios07.exercicio06.exercicio06 import Ex6_7
from exercicios.exercicios07.exercicio07.exercicio07 import Ex7_7
from exercicios.exercicios07.exercicio08.exercicio08 import Ex8_7
from exercicios.exercicios07.exercicio09.exercicio09 import Ex9_7
from exercicios.exercicios07.exercicio10.exercicio10 import Ex10_7

from gerenciadores.gerenciadortexto.main import TelaArquivos
from gerenciadores.gerenciadorword.main import TelaArquivosWord
from gerenciadores.selecionador_arquivo.selecionador import TelaFileDialog

from usuarios.main import TelaListaUsuarios
from login.BancoMySQL import BancoMySQL
from Tkinter.login.BancoMySQL import BancoMySQL