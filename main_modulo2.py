import tkinter as tk
from imports import *

class MenuModulo02():
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Menu Exercícios Tkinter")
        self.janela.geometry("800x800")

        barra_menu = tk.Menu(self.janela)
        menu_exercicios = tk.Menu(barra_menu, tearoff=0)

        lista04 = tk.Menu(menu_exercicios, tearoff=0)
        lista05 = tk.Menu(menu_exercicios, tearoff=0)
        lista06 = tk.Menu(menu_exercicios, tearoff=0)
        lista07 = tk.Menu(menu_exercicios, tearoff=0)
        lista08 = tk.Menu(menu_exercicios, tearoff=0)
        lista09 = tk.Menu(menu_exercicios, tearoff=0)


        for i in range(1, 11):
            lista04.add_command(label=f"Exercício 4.{i}", command=lambda n=i: self.iniciarExercicio(4, n))
            lista05.add_command(label=f"Exercício 5.{i}", command=lambda n=i: self.iniciarExercicio(5, n))
            if i < 4:
                lista06.add_command(label=f"Exercício 6.{i}", command=lambda n=i: self.iniciarExercicio(6, n))
            if i < 10:
                lista07.add_command(label=f"Exercício 7.{i}", command=lambda n=i: self.iniciarExercicio(7, n))
            if i < 8:
                lista08.add_command(label=f"Exercício 8.{i}", command=lambda n=i: self.iniciarExercicio(8, n))
            if i < 6:
                lista09.add_command(label=f"Exercício 9.{i}", command=lambda n=i: self.iniciarExercicio(9, n))


        menu_exercicios.add_cascade(label="Lista 4", menu=lista04)
        menu_exercicios.add_cascade(label="Lista 5", menu=lista05)
        menu_exercicios.add_cascade(label="Lista 6", menu=lista06)
        menu_exercicios.add_cascade(label="Lista 7", menu=lista07)
        menu_exercicios.add_cascade(label="Lista 8", menu=lista08)
        menu_exercicios.add_cascade(label="Lista 9", menu=lista09)

        barra_menu.add_cascade(label="Exercícios", menu=menu_exercicios)
        self.janela.config(menu=barra_menu)


        self.exercicios = {
            
            4: {
                1: Ex0401,
                2: Ex0402,
                3: Ex0403,
                4: Ex0404,
                5: Ex0405,
                6: Ex0406,
                7: Ex0407,
                8: Ex0408,
                9: Ex0409,
                10: Ex0410
            },
            
            5: {
                1: Ex0501,
                2: Ex0502,
                3: Ex0503,
                4: Ex0504,
                5: Ex0505,
                6: Ex0506,
                7: Ex0507,
                8: Ex0508,
                9: Ex0509,
                10: Ex0510
            },
            
            6: {
                # 1: Ex0601,
                # 2: Ex0602,
                # 3: Ex0603
            },
            
            7: {
                # 1: Ex0701,
                # 2: Ex0702,
                # 3: Ex0703,
                # 4: Ex0704,
                # 5: Ex0705,
                # 6: Ex0706,
                # 7: Ex0707,
                # 8: Ex0708,
                # 9: Ex0709
            },
            
            8: {
                # 1: Ex0801,
                # 2: Ex0802,
                # 3: Ex0803,
                # 4: Ex0804,
                # 5: Ex0805,
                # 6: Ex0806,
                # 7: Ex0807
            },
            
            9: {
                # 1: Ex0901,
                # 2: Ex0902,
                # 3: Ex0903,
                # 4: Ex0904,
                # 5: Ex0905
            }
        }



    def iniciarExercicio(self, lista, exercicio):
        exe = self.exercicios[lista][exercicio]
        exe(self.janela).iniciar()



    

    def iniciar(self):
        self.janela.mainloop()


if __name__=="__main__":
    app = MenuModulo02()
    app.iniciar()
