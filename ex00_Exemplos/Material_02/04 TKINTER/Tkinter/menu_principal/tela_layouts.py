import tkinter as tk
import os


from layouts.menu_place.place import TelaPlace
from layouts.meu_pack.pack import TelaPack
from layouts.menu_grid.grid import TelaGrid


class TelaLayouts:
    def __init__(self, master=None):
        self.master = master
        self.janela = tk.Toplevel(master) if master else tk.Tk()
        self.janela.title("Layouts Tkinter")
        self.janela.geometry("500x400")
        self.janela.configure(bg="white")
        self.janela.resizable(False, False)
        
        caminho_icone = os.path.join(os.path.dirname(__file__), "../logo.ico")
        if os.path.exists(caminho_icone):
            self.janela.iconbitmap(caminho_icone)
        
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_janela)

        titulo = tk.Label(self.janela, text="Gerenciadores de Layout", font=("Arial", 16), bg="white")
        titulo.pack(pady=15)


        frame_menu = tk.Frame(self.janela, bg="white")
        frame_menu.pack(pady=20)

        tk.Button(frame_menu, text="Layout Place", command=self.abrir_tela_place, width=15, bg="#007acc", fg="white").pack(pady=5)
        tk.Button(frame_menu, text="Layout Pack", command=self.abrir_tela_pack, width=15, bg="#007acc", fg="white").pack(pady=5)
        tk.Button(frame_menu, text="Layout Grid", command=self.abrir_tela_grid, width=15, bg="#007acc", fg="white").pack(pady=5)

    def fechar_janela(self):
        if self.master:
            self.master.deiconify()  
        self.janela.destroy()


    def abrir_tela_place(self):
        TelaPlace(self.janela).iniciar()

    def abrir_tela_pack(self):
        TelaPack(self.janela).iniciar()

    def abrir_tela_grid(self):
        TelaGrid(self.janela).iniciar()

    def iniciar(self):
        if isinstance(self.janela, tk.Tk):
            self.janela.mainloop()


if __name__ == "__main__":
    app = TelaLayouts()
    app.iniciar()