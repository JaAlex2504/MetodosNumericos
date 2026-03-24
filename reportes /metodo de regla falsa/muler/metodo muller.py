import numpy as np 
import matplotlib.pyplot as plt 
import tkinter as tk 
from tkinter import ttk
from numpy import sin, cos, tan, exp, log, sqrt, pi

# Iniciar con la ventana
ventana = tk.Tk()
ventana.title('Programa - Método de Müller (Según apuntes)')
ventana.geometry("700x850")

def f(x):
    try:
        # Permite que eval reconozca las funciones de numpy y la variable x
        return eval(funcion.get(), {"np": np, "sin": sin, "cos": cos, "tan": tan, "exp": exp, "log": log, "sqrt": sqrt, "pi": pi, "x": x}) 
    except (ValueError, TypeError, ZeroDivisionError, KeyError):
        return 0

# Interfaz: Entrada de función
tk.Label(ventana, text="Ingrese la función f(x):", font=('Arial', 10, 'bold')).pack(pady=5)
funcion = tk.Entry(ventana, width=50)
funcion.pack() 

# Limpiar gráfica
def limpiar_graf():
    plt.clf() 
    
#Grafica
def grafica():
    try:
        x_vals = np.linspace(-10, 10, 400) 
        y_vals = f(x_vals)
        plt.axhline(0, color='black', lw=1)
        plt.axvline(0, color='black', lw=1)
        plt.plot(x_vals, y_vals, color='red', label='f(x)') 
        plt.title(f'Gráfica de f(x) = {funcion.get()}')
        plt.grid(True, linestyle='--')
        plt.legend()
        plt.show()
    except (ValueError, TypeError, ZeroDivisionError, KeyError):
        resultado.config(text="Error al graficar", fg="red")

# Botón de la gráfica
boton_grafica = tk.Button(ventana, text='Mostrar gráfica', command=lambda: [limpiar_graf(), grafica()])
boton_grafica.pack(pady=5)

# Entradas para x0, x1, x2, tol e iteraciones
def crear_campo(texto, default):
    tk.Label(ventana, text=texto).pack()
    ent = tk.Entry(ventana)
    ent.insert(0, default)
    ent.pack()
    return ent

entry_x0 = crear_campo('Ingrese x0:', ' ')
entry_x1 = crear_campo('Ingrese x1:', ' ')
entry_x2 = crear_campo('Ingrese x2:', ' ')
entry_tol = crear_campo('Tolerancia:', ' ')
entry_iter = crear_campo('Máximo de iteraciones:', ' ')

resultado = tk.Label(ventana, text='', font=('Arial', 10, 'bold'))
resultado.pack(pady=5)

# Tabla de resultados
columnas = ('iteración', 'aproximación', 'error_abs')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings', height=10)
tabla.heading('iteración', text='Iteración')
tabla.heading('aproximación', text='Aproximación (x3)')
tabla.heading('error_abs', text='Error Absoluto')
tabla.pack(pady=10)

# método de muller
def muller():
    for item in tabla.get_children():
        tabla.delete(item)
    
    try:
        x0 = float(entry_x0.get())
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_iter.get())
    except ValueError:
        resultado.config(text='Error: Ingrese valores numéricos válidos', fg='red')
        return

    iter_count = 1
    
    while iter_count <= max_iter:
       
        c = f(x2)
        h1 = x1 - x2
        h2 = x0 - x2
        e0 = f(x0) - c
        e1 = f(x1) - c
        w = (h1 * (h2**2)) - (h2 * (h1**2))
        
        if w == 0:
            resultado.config(text='Error: w es cero (división imposible)', fg='red')
            break
            
        #Calcular coeficientes a y b
        a = (e0 * h1 - e1 * h2) / w
        b = (e1 * (h2**2) - e0 * (h1**2)) / w
        
        # Usamos 0j para que el determinante pueda ser un complejo tambien
        discriminante = np.sqrt(b**2 - 4*a*c + 0j)
        
        # Elegir el signo para tener el mayor denominador 
        den_pos = b + discriminante
        den_neg = b - discriminante
        denominador = den_pos if abs(den_pos) > abs(den_neg) else den_neg
        
        if denominador == 0:
            resultado.config(text='Error: Denominador es cero', fg='red')
            break
            
        dx = -2 * c / denominador
        x3 = x2 + dx
        
        #Cálculo del error
        error_abs = abs(dx)
        error_rel = error_abs / abs(x3) if abs(x3) != 0 else 0
        
        # limpiar la parte imaginaria si es casi 0
        txt_3 = f'{x3.real :.6f}' if abs(x3.imag) < 1e-10 else f'{x3:.4f}'
        
        tabla.insert('', tk.END, values=(iter_count, txt_3, f'{error_abs:.6e}',f'{error_rel:.6e}'))
        
        if error_abs < tol:
            resultado.config(text=f"Raíz encontrada: {txt_3}", fg='green')
            return
        
        x0, x1, x2 = x1, x2, x3
        iter_count += 1
        
    resultado.config(text='Fin del proceso', fg='blue')

# Botón para ejecutar
boton_muller = tk.Button(ventana, text='Ejecutar Método de Muller', command=muller, bg='#2196F3', fg='white', font=('Arial', 10, 'bold'))
boton_muller.pack(pady=10)

ventana.mainloop()