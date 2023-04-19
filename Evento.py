import tkinter as tk
class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.boton = tk.Button(master, text="Haz clic", command=self.hacer_clic)
        self.boton.pack()
    def hacer_clic(self):
        print("¡Se hizo clic en el botón!")
root = tk.Tk()
ventana = VentanaPrincipal(root)
root.mainloop()