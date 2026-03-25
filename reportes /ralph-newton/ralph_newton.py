import numpy as np 
import matplotlib.pyplot as plt 
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

np.seterr(all='raise')

# iniciar con la ventana
ventana = tk.Tk()
ventana.title('Programa que encuentra la raíz de una función por el método de Newton Raphson')
ventana.geometry("700x800")

def f(x):
    # Agregamos el reemplazo de ^ por ** para evitar errores de sintaxis comunes
    formula = funcion.get().replace('^', '**')
    contexto = {
        'x': x,
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'arctan': np.arctan,
        'exp': np.exp,
        'log': np.log,
        'sqrt': np.sqrt,
        'pi': np.pi
    }
   
    return eval(formula, contexto)

funcion = tk.Entry(ventana, width=50)
funcion.pack(pady=5) 

def limpiar_graf():
    plt.clf() 
    
def grafica():
    try:
        # Si es un logaritmo, ajustamos el rango para que no truene con negativos
        if 'log' in funcion.get():
            x = np.linspace(0.1, 10, 400)
        else:
            x = np.linspace(-10, 10, 400)
            
        y = f(x)
        plt.axhline(0, color='blue', lw=0.5)
        plt.axvline(0, color='blue', lw=0.5)
        plt.plot(x, y) 
        plt.title(f'Gráfica de f(x) = {funcion.get()}')
        plt.grid()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error de Gráfica", f"No se pudo graficar: {e}")

boton_grafica = tk.Button(ventana, text='Mostrar gráfica', command=lambda: [limpiar_graf(), grafica()])
boton_grafica.pack()

# Entradas de texto
label_x = tk.Label(ventana, text='Ingrese el valor de x:')
label_x.pack()
entry_x = tk.Entry(ventana)
entry_x.pack()

label_tol = tk.Label(ventana, text='Ingrese la tolerancia:')
label_tol.pack()
entry_tol = tk.Entry(ventana)
entry_tol.pack()

label_iter = tk.Label(ventana, text='Máximo de iteraciones:')
label_iter.pack()
entry_iter = tk.Entry(ventana)
entry_iter.pack()

resultado = tk.Label(ventana, text='', fg="red")
resultado.pack(pady=5)

# Tabla
columnas = ('iteración', 'aproximación', 'error_abs', 'error_rel' )
tabla = ttk.Treeview(ventana, columns=columnas, show='headings', height=10)
for col in columnas:
    tabla.heading(col, text=col.replace('_', ' ').title())
    tabla.column(col, width=140, anchor=tk.CENTER)
tabla.pack()

def derivada(x):
    h = 1e-6
    return (f(x+h)-f(x-h)) / (2*h)
    
def newton():
    for item in tabla.get_children():
        tabla.delete(item)
    resultado.config(text='')
    
    
    try:
        x_ant = float(entry_x.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_iter.get())
        
        iteraciones = 0 
        error_abs = tol + 1
        
        temp=[]
        while error_abs > tol and iteraciones < max_iter:
            dfx = derivada(x_ant)
            
            if dfx == 0:
                resultado.config(text=f'La derivada es 0 en x = {x_ant}', fg='red')
                return
            
            x_nuevo = x_ant - (f(x_ant)/dfx)
            error_abs = abs(x_nuevo - x_ant)
            error_rel = abs(error_abs / x_nuevo) if x_nuevo != 0 else 0
                
            iteraciones += 1
            temp.append((iteraciones, f'{x_nuevo:.6f}', f'{error_abs:.2e}', f'{error_rel:.2e}'))
            x_ant = x_nuevo
            
        if error_abs <= tol:
            resultado.config(text=f'Raíz encontrada en x = {x_nuevo:.6f}', fg='green')
            for fila in temp:
                tabla.insert('', 'end',values=fila)
        else:
            resultado.config(text='Se alcanzó el máximo de iteraciones', fg='red')
    
    except ValueError:
        messagebox.showwarning("Datos Inválidos", "Usa números en x0, tolerancia e iteraciones.")
    except ZeroDivisionError:
        messagebox.showerror("Error Matemático", "División por cero detectada.")
    except NameError as e:
        messagebox.showerror("Error de Sintaxis", f"No reconozco: {e}")
    except Exception as e:
        messagebox.showerror("Error de Cálculo", f"Problema: {e}")


boton_newton = tk.Button(ventana, text='Ejecutar Newton Raphson', command=newton, bg='lightgray', font=('Arial', 10, 'bold'))
boton_newton.pack(pady=10)

ventana.mainloop()