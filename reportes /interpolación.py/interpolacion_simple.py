# Este programa realiza interpolación simple utilizando el método de gauss-jorden para resolver el sistema de ecuaciones lineales generado por los puntos de interpolación.
import numpy as np
import tkinter as tk
from tkinter import messagebox, scrolledtext

# generar ventana
ventana = tk.Tk()
ventana.title(
    "Programa para realizar interpolación simple utilizando el método de gauss-jordan"
)
ventana.geometry("600x700")

# lista para almacenar las entradas de la matriz
entradas_matriz = []

# crear frame para la tabla
frame_tabla = tk.Frame(ventana)
frame_tabla.pack(pady=10)

# crear área de texto para mostrar resultados
resultado_text = scrolledtext.ScrolledText(ventana, width=60, height=10)
resultado_text.pack(pady=10)

# crear botones
entry = tk.Entry(ventana, width=20)
entry.pack(pady=5)


def generar_interfaz_matriz():
    global entradas_matriz

    # limpiar la interfaz de la matriz
    for widget in frame_tabla.winfo_children():
        widget.destroy()
    entradas_matriz = []

    try:
        valor_n = entry.get().lower().replace(" ", " ")
        n = int(valor_n.split("x")[0]) if "x" in valor_n else int(valor_n)

        if n < 2:
            messagebox.showwarning(
                "Atención", "Los puntos de interpolación deben ser al menos 2."
            )
            return

        # encabezados
        for j in range(n):
            tk.Label(frame_tabla, text=f"x{j + 1}", font=("Arial", 9, "bold")).grid(
                row=0, column=j
            )
            tk.Label(frame_tabla, text="f(x)", font=("Arial", 9, "bold")).grid(
                row=0, column=n
            )
            for i in range(n):
                fila = []
                for j in range(n + 1):
                    e = tk.Entry(frame_tabla, width=9, justify="center")
                    e.grid(row=i + 1, column=j, padx=2, pady=2)
                    fila.append(e)
                entradas_matriz.append(fila)
    except ValueError:
        messagebox.showerror("Error", "Escriba un tamaño válido (ej: 3 o 3x3).")


def resolver_gauss_jordan():
    try:
        n = len(entradas_matriz)
        tol = 1e-10

        matriz_datos = []
        for fila_widgets in entradas_matriz:
            fila_datos = []
            for widget in fila_widgets:
                valor_entrada = widget.get()
                if valor_entrada.strip() == "":
                    messagebox.showerror(
                        "Error", "Por favor, complete todas las entradas de la matriz."
                    )
                    return
                try:
                    valor = float(valor_entrada)
                    fila_datos.append(valor)
                except ValueError:
                    messagebox.showerror(
                        "Error", "Por favor, ingrese solo números en la matriz."
                    )
                    return
            matriz_datos.append(fila_datos)
            matriz_datos = np.array(matriz_datos)

            # aplicar el método de gauss-jordan para resolver el sistema de ecuaciones
            for i in range(n):
                max_row_index = np.argmax(np.abs(matriz_datos[i:, i])) + i
                if abs(matriz_datos[max_row_index, i]) < tol:
                    messagebox.showerror("Error", "El sistema no tiene solución única.")
                    return
                matriz_datos[[i, max_row_index]] = matriz_datos[[max_row_index, i]]

                for j in range(i + 1, n):
                    factor = matriz_datos[j, i] / matriz_datos[i, i]
                    matriz_datos[j] = matriz_datos[j] - factor * matriz_datos[i]

                    # obtener la solución del sistema de ecuaciones
                    soluciones = np.zeros(n)
                    for i in range(n - 1, -1, -1):
                        soluciones[i] = (
                            matriz_datos[i, -1]
                            - np.dot(matriz_datos[i, i + 1 : n], soluciones[i + 1 : n])
                        ) / matriz_datos[i, i]

                        # mostrar la solución en un cuadro de texto
                        resultado_text.delete(1.0, tk.END)
                        resultado_text.insert(tk.END, "Soluciones:\n")
                        for i in range(n):
                            resultado_text.insert(
                                tk.END, f"x{i + 1} = {soluciones[i]:.4f}\n"
                            )
    except ValueError:
        messagebox.showerror("Error", "Escriba un tamaño válido (ej: 3 o 3x3).")
