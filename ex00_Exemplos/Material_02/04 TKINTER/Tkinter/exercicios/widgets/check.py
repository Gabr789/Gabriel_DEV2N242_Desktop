import tkinter as tk
class MeuCheckGroup:
    def __init__(self, tela_pertence, opcoes, tipo="bool",**kwargs):
        self.frame = tk.Frame(tela_pertence,**kwargs)
        self.frame.pack(pady=10)

        self.vars = []
        for texto in opcoes:
            if tipo == "int":
                var = tk.IntVar(value=0)
            else:
                var = tk.BooleanVar(value=False)

            chk = tk.Checkbutton(self.frame, text=texto, variable=var, font=("Arial", 11))
            chk.pack(anchor="w")
            self.vars.append((texto, var))

    def pegar_valores(self):
        
        selecionados = [texto for texto, var in self.vars if var.get()]
        return selecionados

    def limpar(self):
       
        for _, var in self.vars:
            if isinstance(var, tk.IntVar):
                var.set(0)
            else:
                var.set(False)