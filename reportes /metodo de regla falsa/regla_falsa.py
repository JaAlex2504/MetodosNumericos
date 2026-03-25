#Programa para hacer aproximaciones de raices mediante el metodo de la regla falsa

import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk 
#importar funciones de numpy para que eval las reconozca directo
from numpy import sin, cos, tan, exp, log, sqrt, pi

#empezar abriendo la ventana 
#crear la ventana de tkinter
ventana = tk.Tk()
ventana.title('Porgrama para encontrar las raíces de un polinomio mediante el método de regla falsa')
ventana.geometry("700x700")

#Aqui le pido al usuario que ingrese la función

def f(x):
    #usar las funciones importadas de numpy arriba
    return eval(funcion.get())

funcion=tk.Entry(ventana, width=50)
funcion.pack()


#antes de mostrar la gráfica hay que limiarla por si se ingresa una nueva ecuación
def limpiar_grafica():
    plt.clf()

#Hacer la gráfica de la función
def grafica():
    #ajustar el rango de x para ver mejor la funcion
    x = np.linspace(-10, 10, 400)
    y = f(x)
    plt.plot(x,y, label='f(x)')
    plt.axhline(0, color='blue', lw=0.5)
    plt.axvline(0, color='blue', lw=0.5)
    plt.title(f'Gráfica de f(x) = {funcion.get()}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.legend()
    plt.show()
    
#hacer el boton de la gráfica para mostrarla
boton_grafica = tk.Button(ventana, text='Mostrar gráfica', command=lambda: [limpiar_grafica(), grafica()])
boton_grafica.pack()

#Pedir valores de a y b
label_a = tk.Label(ventana, text='Ingrese el valor de a:')
label_a.pack()
entry_a = tk.Entry(ventana)
entry_a.pack()
label_b = tk.Label(ventana, text='Ingrese el valor de b:')
label_b.pack()
entry_b =tk.Entry(ventana)
entry_b.pack()

#Pedir la tolerancia
label_tol = tk.Label(ventana, text='Ingrese la tolerancia (debe ser un valor mayor a 0 y menor a 1):')
label_tol.pack()
entry_tol = tk.Entry(ventana)
entry_tol.pack()

#Pedir el número máximo de iteraciones
label_iter = tk.Label(ventana, text='Ingrese el número máximo de iteraciones:')
label_iter.pack()
entry_iter = tk.Entry(ventana)
entry_iter.pack()

resultado = tk.Label(ventana, text='', fg="red")
resultado.pack(pady=5)

#tabla de iteraciones 
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


#empezar el método de regla falsa
def reg_falsa():
    #limpiar la tabla por si hay un nuevo polinomio
    for item in tabla.get_children():
        tabla.delete(item)
    resultado.config(text='')
    
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_iter.get())
             
    except ValueError:
        resultado.config(text='Por favor llena todos los campos con valores numérics')
        return
    
    #checar que haya cambio de signo
    if f(a) * f(b) > 0:
        resultado.config(text='Error: f(a) y f(b) deben tener signos opuestos')
        return
    
    iter_count = 1
    c_viejo = 0
    
    # Implementar el algoritmo de regla falsa aquí
    while iter_count <= max_iter:
        #aplicar formula de la posicion falsa
        c = b - (f(b)*(b-a)) / (f(b)-f(a))
        
        if iter_count > 1:
            error_absoluto = abs(c-c_viejo)
            error_relativo = error_absoluto / abs(c) if c != 0 else float('inf')
            
            err_abs_str = f"{error_absoluto:.6e}"
            err_rel_str = f"{error_relativo:.6e}"
            
        else:
            err_abs_str = '---'
            err_rel_str = '---'
            
        tabla.insert('', tk.END, values= (iter_count, f"{c:.6e}", err_abs_str, err_rel_str))
        
        #si ya estamos cerca de la raiz nos salimos
        if abs(f(c)) < tol:
            resultado.config(text=f"La raíz encontrada es: {c:.6e}", fg='green')
            break 
        
        if f(c) * f(a) < 0:
            b = c 
        else:
            a = c 
            
        #actualizar el c_viejo para el error del siguiente ciclo
        c_viejo = c 
        iter_count += 1
        
    else: 
        resultado.config(text='Se alcanzó el máximo de iteraciones sin llegar a la tolerancia', fg='red')
        
 
#botón para ejecutar método
boton_reg_falsa = tk.Button(ventana,text='Ejecutar método de regla falsa', command=reg_falsa, bg='lightgray', font=('Arial', 10, 'bold'))
boton_reg_falsa.pack()
#x**x - 100, x=3.59
ventana.mainloop()