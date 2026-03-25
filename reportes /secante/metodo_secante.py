import numpy as np 
import matplotlib.pyplot as plt # Corregido para coincidir con el uso de 'plt'
import tkinter as tk 
from tkinter import ttk
from numpy import sin, cos, tan, exp, log, sqrt, pi

#iniciar con la ventana
ventana=tk.Tk()
ventana.title('Programa que encuentra la raíz de funciones mediante el método de secante')
ventana.geometry("700x750")

#funcion del usuario
def f(x):
    return eval(funcion.get()) 

funcion=tk.Entry(ventana, width=50)
funcion.pack() 

#limpiar grafica
def limpiar_graf():
    plt.clf() 
    
#seccion de la creacion de la gráfica
def grafica():
    x=np.linspace(-10,10,400) 
    y=f(x)
    plt.axhline(0, color='blue', lw=0.5)
    plt.axvline(0, color='blue', lw=0.5)
    plt.plot(x, y) 
    plt.title(f'Gráfica de f(x) = {funcion.get()}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.legend(['f(x)'])
    plt.show()

#boton de la grafica
boton_grafica=tk.Button(ventana, text='Mostrar gráfica', command= lambda: [limpiar_graf(),grafica()])
boton_grafica.pack()

#Pedir el rango x0 y x1 
label_x0 = tk.Label(ventana, text='Ingrese el valor de x0:')
label_x0.pack()
entry_x0 = tk.Entry(ventana)
entry_x0.pack()
label_x1 = tk.Label(ventana, text='Ingrese el valor de x1:')
label_x1.pack()
entry_x1 =tk.Entry(ventana)
entry_x1.pack()

#Pedir la tolerancia
label_tol = tk.Label(ventana, text='Ingrese la tolerancia (debe ser un valor mayor a 0 y menor a 1):')
label_tol.pack()
entry_tol = tk.Entry(ventana)
entry_tol.pack()

#Pedir cantidad maxima de iteraciones
label_iter = tk.Label(ventana, text='Ingrese el número máximo de iteraciones:')
label_iter.pack()
entry_iter = tk.Entry(ventana)
entry_iter.pack()

resultado = tk.Label(ventana, text='', fg="red")
resultado.pack(pady=5)

#Tabla de resultados
columnas = ('iteración', 'aproximación', 'error_abs', 'error_rel' )
tabla = ttk.Treeview(ventana, columns=columnas, show='headings', height=10)
tabla.heading('iteración', text='Iteración')
tabla.heading('aproximación', text='Aproximación')
tabla.heading('error_abs', text='Error Absoluto')
tabla.heading('error_rel', text='Error Relativo')

tabla.column('iteración', width=80, anchor=tk.CENTER)
tabla.column('aproximación', width=150, anchor=tk.CENTER)
tabla.column('error_abs', width=150, anchor=tk.CENTER)
tabla.column('error_rel', width=150, anchor=tk.CENTER)
tabla.pack()

# Empezar el método de la secante
def secante():
    # limpiar la tabla por si hay un nuevo cálculo
    for item in tabla.get_children():
        tabla.delete(item)
    resultado.config(text='')
    
    try:
        x0 = float(entry_x0.get())
        x1 = float(entry_x1.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_iter.get())
    except ValueError:
        resultado.config(text='Por favor llena todos los campos con valores numéricos')
        return

    iter_count = 1
    
    while iter_count <= max_iter:
        fx0 = f(x0)
        fx1 = f(x1)
        
        # Evitar división por cero si la pendiente es horizontal
        if abs(fx1 - fx0) < 1e-15:
            resultado.config(text='Error: División por cero (pendiente horizontal)', fg='red')
            return
        
        # formula de la secante
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        
        error_absoluto = abs(x2 - x1)
        error_relativo = error_absoluto / abs(x2) if x2 != 0 else 0
        
        # Insertar en la tabla
        tabla.insert('', tk.END, values=(iter_count, f"{x2:.6f}", f"{error_absoluto:.6e}", f"{error_relativo:.6e}"))
        
        # Condición de parada
        if error_absoluto < tol:
            resultado.config(text=f"La raíz encontrada es: {x2:.6e}", fg='green')
            break
        
        # Actualización de puntos para el siguiente ciclo
        x0 = x1
        x1 = x2
        iter_count += 1
    else:
        resultado.config(text='Se alcanzó el máximo de iteraciones sin llegar a la tolerancia', fg='red')
        
# Botón para ejecutar método
boton_secante = tk.Button(ventana, text='Ejecutar método de la secante', command=secante, bg='lightgray', font=('Arial', 10, 'bold'))
boton_secante.pack(pady=10)

ventana.mainloop()