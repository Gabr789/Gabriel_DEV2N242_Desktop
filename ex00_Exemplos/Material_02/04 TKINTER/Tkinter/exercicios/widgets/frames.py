import tkinter as tk

class MeuFrame(tk.Frame):
    def __init__(self, tela_pertence, relief="sunken", bd=2, padx=20, pady=20,**kwargs):
        super().__init__(tela_pertence, relief=relief, bd=bd,**kwargs)
        self.pack(expand=True, fill="both", padx=padx, pady=pady)