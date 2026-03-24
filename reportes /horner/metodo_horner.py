import numpy as np 
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk 

#Configurar ventana
ventana = tk.Tk()
ventana.title('Método de Newton-Horner - Búsqueda de Raíces')
ventana.geometry("750x850")

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
style.map('Treeview', background=[('selected', '#347083')])

# --- 2. CREACIÓN DE LA INTERFAZ (Se declara antes para evitar errores del editor) ---
tk.Label(ventana, text='Ingrese los coeficientes de mayor a menor grado separados por comas\n(No olvide los ceros si falta un término. Ej: 2, -5, 3, -10):', font=('Arial', 10, 'bold')).pack(pady=(15, 5))
entry_pol = tk.Entry(ventana, width=50, font=('Arial', 12))
entry_pol.pack()

boton_grafica = tk.Button(ventana, text='Mostrar gráfica', font=('Arial', 10))
boton_grafica.pack(pady=10)

tk.Label(ventana, text='-------------------------------------------------------------------------').pack()

tk.Label(ventana, text='Punto inicial (x0):', font=('Arial', 10)).pack(pady=(5,0))
entry_x0 = tk.Entry(ventana, justify='center')
entry_x0.pack()

tk.Label(ventana, text='Tolerancia (ej: 0.0001):', font=('Arial', 10)).pack(pady=(5,0))
entry_tol = tk.Entry(ventana, justify='center')
entry_tol.pack()

tk.Label(ventana, text='Número máximo de iteraciones (ej: 100):', font=('Arial', 10)).pack(pady=(5,0))
entry_iter = tk.Entry(ventana, justify='center')
entry_iter.pack()

resultado_lbl = tk.Label(ventana, text='Esperando datos...', fg="gray", font=('Arial', 10, 'bold'))
resultado_lbl.pack(pady=10)

boton_horner = tk.Button(ventana, text='Ejecutar Método de Horner', bg='#d3d3d3', font=('Arial', 11, 'bold'))
boton_horner.pack(pady=5)

columnas = ('iteración', 'aproximación', 'error_abs', 'error_rel')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings', height=12)
for col in columnas:
    tabla.heading(col, text=col.replace('_', ' ').capitalize())
    tabla.column(col, width=150, anchor=tk.CENTER)
tabla.pack(pady=10)

# --- 3. LÓGICA MATEMÁTICA Y FUNCIONES ---
def evaluar_horner(coeficientes, x0):
    y = coeficientes[0]
    z = 0
    for i in range(1, len(coeficientes)):
        z = z * x0 + y
        y = y * x0 + coeficientes[i]
    return y, z

def grafica():
    try:
        texto = entry_pol.get()
        if not texto.strip():
            resultado_lbl.config(text="Error: El campo de coeficientes está vacío.", fg="red")
            return
            
        coefs = [float(c.strip()) for c in texto.split(',')]
        x = np.linspace(-10, 10, 400)
        
        if len(coefs) == 1:
            y = np.full_like(x, coefs[0])
        else:
            y = coefs[0]
            for c in coefs[1:]:
                y = y * x + c
            
        plt.clf()
        plt.plot(x, y, label='P(x)', color='red')
        plt.axhline(0, color='black', lw=0.8)
        plt.axvline(0, color='black', lw=0.8)
        plt.title('Gráfica del Polinomio')
        plt.grid(True)
        plt.legend()
        plt.show()
        resultado_lbl.config(text="Gráfica generada correctamente.", fg="blue")
    except Exception as e:
        resultado_lbl.config(text="Error en gráfica: Revisa el formato.", fg="red")
        print(f"Detalle del error: {e}")

def horner():
    for i in tabla.get_children():
        tabla.delete(i)
        
    try:
        texto = entry_pol.get()
        coefs = [float(c.strip()) for c in texto.split(',')]
        
        if len(coefs) == 1:
            resultado_lbl.config(text="Error: Derivada nula (la tangente es horizontal).", fg="red")
            return

        x_actual = float(entry_x0.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_iter.get())
        
        for k in range(1, max_iter + 1):
            px, dpx = evaluar_horner(coefs, x_actual)
            
            if abs(dpx) < 1e-12:
                resultado_lbl.config(text="Error: Derivada nula (la tangente es horizontal).", fg="red")
                return
                
            x_nuevo = x_actual - (px / dpx)
            error_abs = abs(x_nuevo - x_actual)
            error_rel = error_abs / abs(x_nuevo) if x_nuevo != 0 else 0
            
            tabla.insert('', 'end', values=(k, f"{x_nuevo:.6f}", f"{error_abs:.6e}", f"{error_rel:.6e}"))
            
            if error_abs < tol:
                resultado_lbl.config(text=f"¡Raíz encontrada! x = {x_nuevo:.6f}", fg="green")
                return
            
            x_actual = x_nuevo
            
        resultado_lbl.config(text="Se alcanzó el máximo de iteraciones sin converger.", fg="orange")
        
    except ValueError:
        resultado_lbl.config(text="Error: Verifica que todos los campos tengan números válidos.", fg="red")
    except ZeroDivisionError:
        resultado_lbl.config(text="Error: División por cero en los cálculos.", fg="red")

# --- 4. CONECTAR BOTONES ---
boton_grafica.config(command=grafica)
boton_horner.config(command=horner)

ventana.mainloop()