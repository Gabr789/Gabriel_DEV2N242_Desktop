import tkinter as tk
from exercicios.widgets.combo import MeuCombo
from exercicios.widgets.radio import MeuRadioGroup
from exercicios.widgets.check import MeuCheckGroup
from exercicios.widgets.botoes import MeuBotao
from exercicios.widgets.labels import MeuLabel

class Ex10_7(tk.Frame):
    def __init__(self, janela):
        super().__init__(janela)

     
        MeuLabel(self, "Selecione o curso:")
        self.combo_curso = MeuCombo(self, ["ADS", "Jogos", "Redes"])

       
        MeuLabel(self, "Selecione o turno:")
        self.radios_turno = MeuRadioGroup(self, [
            ("Manhã", "Manhã"),
            ("Tarde", "Tarde"),
            ("Noite", "Noite")
        ])

      
        MeuLabel(self, "Selecione as opções adicionais:")
        self.checks = MeuCheckGroup(self, ["Participa do Discord", "Gosta de programação"])

       
        MeuBotao(self, "Enviar", comando=self.enviar)

    def enviar(self):
        curso = self.combo_curso.pegar_valor()
        turno = self.radios_turno.pegar_valor()
        opcoes = self.checks.pegar_valores()

       
        nova_janela = tk.Toplevel(self)
        nova_janela.title("Resumo do Formulário")

        texto = f"Curso: {curso or 'Não selecionado'}\n"
        texto += f"Turno: {turno or 'Não selecionado'}\n"
        texto += f"Opções: {', '.join(opcoes) if opcoes else 'Nenhuma marcada'}"

        MeuLabel(nova_janela, texto)