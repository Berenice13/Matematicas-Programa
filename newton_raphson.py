import tkinter as tk
from tkinter import ttk, messagebox

class MetodoNewtonRaphson(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Método de Newton-Raphson")
        self.geometry("600x500")
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        #f(x)
        self.label_funcion = ttk.Label(self, text="Ingrese la función en términos de x (por ejemplo, x**2 - 4): ")
        self.label_funcion.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")
        self.input_funcion = ttk.Entry(self)
        self.input_funcion.grid(row=0, column=3, columnspan=2, pady=5)

        #'f(x)
        self.label_derivada = ttk.Label(self, text="Ingrese la derivada de la función (por ejemplo, 2*x): ")
        self.label_derivada.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")
        self.input_derivada = ttk.Entry(self)
        self.input_derivada.grid(row=1, column=3, columnspan=2, pady=5)

        #x0
        self.label_x0 = ttk.Label(self, text="Ingrese el valor inicial de x (x0):")
        self.label_x0.grid(row=3, column=0, pady=5, sticky="w")
        self.input_x0 = ttk.Entry(self)
        self.input_x0.grid(row=3, column=3, pady=5)

        #btn
        self.frame_btn = ttk.Frame(self)
        self.frame_btn.grid(row=6, column=0, columnspan=5, pady=20)

        self.btn_calcular = ttk.Button(self.frame_btn, text="Calcular", command=self.calcular_newton_raphson)
        self.btn_calcular.grid(row=6, column=0, pady=5, sticky="w")

        #tabla
        self.tabla = ttk.Treeview(self, columns=("Iteración", "Valor Actual", "Resultado"), show="headings")
        self.tabla.heading("Iteración", text="Iteración")
        self.tabla.heading("Valor Actual", text="Valor Actual")
        self.tabla.heading("Resultado", text="Resultado")
        self.tabla.grid(row=7, column=0, columnspan=5, pady=20)

    def cerrar_ventana(self):
        self.parent.deiconify()
        self.destroy()

    def calcular_newton_raphson(self):
        try:
            funcion = lambda x: eval(self.input_funcion.get())
            derivada = lambda x: eval(self.input_derivada.get())
            x_inicial = float(self.input_x0.get())

            resultados = self._newton_raphson(funcion, derivada, x_inicial)

            for item in self.tabla.get_children():
                self.tabla.delete(item)

            for iteracion, valor_actual, resultado in resultados:
                self.tabla.insert("", "end", values=(iteracion, valor_actual, resultado))
                
        except Exception as e:
            messagebox.showerror("Error", f"Asegúrate de que la expresión de la derivada tenga una sintaxis válida.")

    def _newton_raphson(self, funcion, derivada, x_inicial):
        max_iteraciones = 100
        tolerancia = 1e-6
        x_actual = x_inicial
        iteracion = 0
        valores_antiguos = []

        while iteracion < max_iteraciones:
            # Aplicar la fórmula de Newton-Raphson
            x_siguiente = x_actual - funcion(x_actual) / derivada(x_actual)

            # Verificar la tolerancia
            if abs(x_siguiente - x_actual) < tolerancia:
                return valores_antiguos

            valores_antiguos.append((iteracion, x_actual, x_siguiente))
            x_actual = x_siguiente
            iteracion += 1

        raise ValueError("El método de Newton-Raphson no convergió después de {} iteraciones.".format(max_iteraciones))


if __name__ == "__main__":
    app = MetodoNewtonRaphson(None)
    app.mainloop()