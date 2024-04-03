import tkinter as tk
from tkinter import ttk, messagebox

class MetodoEuler(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Método de Euler Mejorado")
        self.geometry("600x500")
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        # f(x,y)
        self.label_funcion = ttk.Label(self, text="Ingrese la función en términos de x e y (por ejemplo, 2 * x * y):")
        self.label_funcion.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")
        self.input_funcion = ttk.Entry(self)
        self.input_funcion.grid(row=0, column=3, columnspan=2, pady=5)

        #y0
        self.label_y0 = ttk.Label(self, text="Ingrese el valor inicial de y (y0):")
        self.label_y0.grid(row=2, column=0, pady=5, sticky="w")
        self.input_y0 = ttk.Entry(self)
        self.input_y0.grid(row=2, column=3, pady=5)
        
        #x0
        self.label_x0 = ttk.Label(self, text="Ingrese el valor inicial de x (x0):")
        self.label_x0.grid(row=3, column=0, pady=5, sticky="w")
        self.input_x0 = ttk.Entry(self)
        self.input_x0.grid(row=3, column=3, pady=5)

        #xn
        self.label_xn = ttk.Label(self, text="Ingrese el valor final de x (xn):")
        self.label_xn.grid(row=4, column=0, pady=5, sticky="w")
        self.input_xn = ttk.Entry(self)
        self.input_xn.grid(row=4, column=3, pady=5)

        #h
        self.label_h = ttk.Label(self, text="Ingrese el tamaño del paso (h):")
        self.label_h.grid(row=5, column=0, pady=5, sticky="w")
        self.input_h = ttk.Entry(self)
        self.input_h.grid(row=5, column=3, pady=5)

        #btn
        self.frame_btn = ttk.Frame(self)
        self.frame_btn.grid(row=6, column=0, columnspan=5, pady=20)

        self.btn_calcular = ttk.Button(self.frame_btn, text="Calcular", command=self.calcular_euler_mejorado)
        self.btn_calcular.grid(row=6, column=0, pady=5, sticky="w")

        #tabla
        self.frame = ttk.Frame(self)
        self.frame.place(relx=0.4, rely=0.7, anchor="center")

        self.tabla = ttk.Treeview(self.frame, columns=("x", "y"), show="headings")
        self.tabla.heading("x", text="x")
        self.tabla.heading("y", text="y")
        self.tabla.grid(row=7, column=0, columnspan=2, pady=20)

    def cerrar_ventana(self):
        self.parent.deiconify()
        self.destroy()

    def calcular_euler_mejorado(self):
        try:
            expresion_funcion = self.input_funcion.get()
            funcion = lambda x, y: eval(expresion_funcion)
            y0 = float(self.input_y0.get())
            x0 = float(self.input_x0.get())
            xn = float(self.input_xn.get())
            h = float(self.input_h.get())

            tiempo = [x0]
            valores_y = [y0]

            while tiempo[-1] < xn:
                x_n = tiempo[-1]
                y_n = valores_y[-1]
                
                # Paso 1 del método de Euler mejorado
                k1 = h * funcion(x_n, y_n)
                
                # Paso 2 del método de Euler mejorado
                k2 = h * funcion(x_n + h, y_n + k1)
                
                # Actualizar los valores
                y_n1 = y_n + 0.5 * (k1 + k2)
                x_n1 = x_n + h
                
                valores_y.append(y_n1)
                tiempo.append(x_n1)

            # Limpiar la tabla antes de agregar nuevos datos
            for item in self.tabla.get_children():
                self.tabla.delete(item)

            # Agregar los resultados a la tabla
            for x, y in zip(tiempo, valores_y):
                self.tabla.insert("", "end", values=(f"{x:.4f}", f"{y:.4f}"))

        except Exception as e:
            messagebox.showerror("Error", f"Asegúrate de que la expresión de la derivada tenga una sintaxis válida.")

if __name__ == "__main__":
    app = MetodoEuler(None)
    app.mainloop()
