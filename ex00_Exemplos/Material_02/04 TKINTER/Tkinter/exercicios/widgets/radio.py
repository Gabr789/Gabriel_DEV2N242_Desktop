import tkinter as tk

class MeuRadioGroup:
    def __init__(self, tela_pertence, opcoes, tipo="string",**kwargs):
        self.frame = tk.Frame(tela_pertence,**kwargs)
        self.frame.pack(pady=10)

        if tipo == "int":
            self.var = tk.IntVar(value=0)  
        else:
            self.var = tk.StringVar(value="")  

        for texto, valor in opcoes:
            rb = tk.Radiobutton(self.frame, text=texto, variable=self.var, value=valor, font=("Arial", 11))
            rb.pack(anchor="w")

    def pegar_valor(self):
       
        return self.var.get()

    def limpar(self):
   
        if isinstance(self.var, tk.IntVar):
            self.var.set(0)
        else:
            self.var.set("")
