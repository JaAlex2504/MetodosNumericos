import numpy as np
import tkinter as tk
from tkinter import messagebox, scrolledtext

ventana = tk.Tk()
ventana.title('Programa para resolver sistemas de ecuaciones mediante Gauss-Jordan')
ventana.geometry('600x700')


entradas_matriz = []


def generar_interfaz_matriz():
    global entradas_matriz
    
    for widget in frame_tabla.winfo_children():
        widget.destroy()
    entradas_matriz = []
    
    try:
        valor_n = entry_n.get().lower().replace(" ", "")
        n = int(valor_n.split('x')[0]) if 'x' in valor_n else int(valor_n)

        if n < 2:
            messagebox.showwarning("Atención", "Las ecuaciones deben tener mínimo 2 incógnitas.")
            return

        # Encabezados
        for j in range(n):
            tk.Label(frame_tabla, text=f"x{j+1}", font=('Arial', 9, 'bold')).grid(row=0, column=j)
        tk.Label(frame_tabla, text="Resultado", font=('Arial', 9, 'bold')).grid(row=0, column=n)

        for i in range(n):
            fila = []
            for j in range(n + 1):
                e = tk.Entry(frame_tabla, width=9, justify='center')
                e.grid(row=i+1, column=j, padx=2, pady=2)
                fila.append(e)
            entradas_matriz.append(fila)
            
        btn_resolver.config(state='normal')
        
    except ValueError:
        messagebox.showerror('Error', 'Escriba un tamaño válido (ej: 3 o 3x3).')

def resolver_gauss_jordan():
    try:
        n = len(entradas_matriz)
        tol = 1e-10
        
        # Lectura de datos
        matriz_datos = []
        for fila_widgets in entradas_matriz:
            fila_valores = []
            for w in fila_widgets:
                val = w.get().replace(",", ".")
                fila_valores.append(float(val) if val else 0.0)
            matriz_datos.append(fila_valores)
        
        M = np.array(matriz_datos, dtype=float)
        
        # Proceso de Gauss-Jordan
        for j in range(n):
            fila_pivote = np.argmax(abs(M[j:n, j])) + j
            if abs(M[fila_pivote, j]) < tol:
                messagebox.showerror("Error", "El sistema no tiene solución única.")
                return
            
            M[[j, fila_pivote]] = M[[fila_pivote, j]]
            M[j] = M[j] / M[j, j]
            
            for i in range(n):
                if i != j:
                    M[i] = M[i] - M[i, j] * M[j]

        #Resultado final 
        txt_resultados.config(state='normal')
        txt_resultados.delete(1.0, tk.END)
        txt_resultados.insert(tk.END, "SOLUCIÓN DEL SISTEMA:\n", "titulo")
        txt_resultados.insert(tk.END, "-"*30 + "\n")
        
        for i in range(n):
            # Formato x1 = valor
            txt_resultados.insert(tk.END, f" x{i+1} = ", "negrita")
            txt_resultados.insert(tk.END, f"{M[i, -1]:.4f}\n", "valor")
        
        txt_resultados.config(state='disabled')

    except ValueError:
        messagebox.showerror("Error", "Asegúrate de llenar todos los campos con números.")

def limpiar_todo():
    entry_n.delete(0, tk.END)
    for widget in frame_tabla.winfo_children():
        widget.destroy()
    txt_resultados.config(state='normal')
    txt_resultados.delete(1.0, tk.END)
    btn_resolver.config(state='disabled')

#Controles
controles = tk.Frame(ventana)
controles.pack(pady=10)

tk.Label(controles, text='Tamaño de la matriz:').grid(row=0, column=0, padx=5)
entry_n = tk.Entry(controles, width=8, justify='center')
entry_n.grid(row=0, column=1, padx=5)

tk.Button(controles, text="Generar matriz", command=generar_interfaz_matriz).grid(row=0, column=2, padx=5)
tk.Button(controles, text="Limpiar", command=limpiar_todo).grid(row=0, column=3, padx=5)

frame_tabla = tk.Frame(ventana)
frame_tabla.pack(pady=10)

btn_resolver = tk.Button(ventana, text="RESOLVER", command=resolver_gauss_jordan, 
                         state='disabled', font=('Arial', 10, 'bold'), width=20, height=2)
btn_resolver.pack(pady=15)



# Panel de Resultados
tk.Label(ventana, text='RESULTADOS:', font=('Arial', 9, 'bold')).pack()
txt_resultados = tk.Text(ventana, width=40, height=10, font=('Arial', 11))

# Configuración de estilos de texto
txt_resultados.tag_config("titulo", foreground="blue", font=('Arial', 12, 'bold'))
txt_resultados.tag_config("negrita", font=('Arial', 11, 'bold'))
txt_resultados.tag_config("valor", foreground="green")

txt_resultados.pack(pady=10)
txt_resultados.config(state='disabled')

ventana.mainloop()