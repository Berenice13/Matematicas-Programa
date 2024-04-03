import tkinter as tk
from tkinter import ttk, messagebox
import euler_mejorado
import runge_kutta
import newton_raphson

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0')

        self.title("Menú")
        
        #tamaño del contenedor
        self.geometry("400x200")

        #contenedor para centrar el contenido
        self.frame = ttk.Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.nombre = ttk.Label(self.frame, text="NOMBRE: Berenice de la Cruz de la Cruz")
        self.nombre.grid(row=0, column=0, pady=10)

        self.label = ttk.Label(self.frame, text="Seleccione un método:")
        self.label.grid(row=1, column=0, pady=10)

        #select
        self.combo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frame, textvariable=self.combo, values=["Resolver EDO con Euler mejorado", "Resolver EDO con Runge-Kutta", "Resolver ecuación con Newton-Raphson", "Salir"], width=40)
        self.combobox.grid(row=2, column=0, pady=10)

        self.button = ttk.Button(self.frame, text="Ejecutar", command=self.ejecutar_opcion)
        self.button.grid(row=3, column=0, pady=10)

    def ejecutar_opcion(self):
        opcion = self.combo.get()

        if opcion == "Resolver EDO con Euler mejorado":
            self.ejecutar_euler_mejorado()
        elif opcion == "Resolver EDO con Runge-Kutta":
            self.ejecutar_runge_kutta()
        elif opcion == "Resolver ecuación con Newton-Raphson":
            self.ejecutar_newton_raphson()
        elif opcion == "Salir":
            messagebox.showinfo("Salir", "¡Hasta luego!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Opción no válida. Por favor, seleccione una opción válida.")

    def ejecutar_euler_mejorado(self):
        euler_mejorado.MetodoEuler(self).mostrar_interfaz_grafica()

    def ejecutar_runge_kutta(self):
        runge_kutta.MetodoRungeKutta(self).mostrar_interfaz_grafica()

    def ejecutar_newton_raphson(self):
        newton_raphson.MetodoNewtonRaphson(self).mostrar_interfaz_grafica()

if __name__ == "__main__":
    app = Menu()
    app.mainloop()
