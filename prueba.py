import tkinter as tk
import metodos as mt
import numpy as np
import Ceros as cs
import sympy as sp


# Variable para almacenar los datos ingresados
dato_ingresado = ''

def add_placeholder(entry, placeholder):
    def clear_placeholder(event):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(fg="black")

    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", clear_placeholder)
    entry.config(fg="grey")
    

# Funciones para cambiar de interfaz 
def mostrar_interfaz_poli():
    ocultar_botones()
    interfaz_poli.pack()
    boton_volver.pack()

def mostrar_interfaz_lagrange():
    ocultar_botones()
    interfaz_lagrange.pack()
    boton_volver.pack()

def mostrar_interfaz_MC():
    ocultar_botones()
    interfaz_MC.pack()
    boton_volver.pack()
    
def mostrar_interfaz_euler1():
    ocultar_botones()
    interfaz_euler.pack()
    boton_volver.pack()

def mostrar_interfaz_rk41():
    ocultar_botones()
    interfaz_rk41.pack()
    boton_volver.pack()

def mostrar_interfaz_ceros_abiertos():
    ocultar_botones()
    interfaz_ceros_mtAbierto.pack()
    boton_ceros_newton.pack()
    boton_ceros_secante.pack()
    boton_volver.pack()

def mostrar_interfaz_ceros_cerrados():
    ocultar_botones()
    interfaz_ceros_mtCerrado.pack()
    boton_ceros_biseccion.pack()
    boton_ceros_falsa_pos.pack()
    boton_volver.pack()

def mostrar_interfaz_newton():
    ocultar_botones()
    interfaz_newton.pack()
    boton_volver.pack()

def mostrar_interfaz_secante():
    ocultar_botones()
    interfaz_secante.pack()
    boton_volver.pack()

def mostrar_interfaz_biseccion():
    ocultar_botones()
    interfaz_biseccion.pack()
    boton_volver.pack()

def mostrar_interfaz_falsa_pos():
    ocultar_botones()
    interfaz_falsa_pos.pack()
    boton_volver.pack()

def opciones_EDO1():
    ocultar_botones()
    interfaz_EDO1.pack()
    boton_euler1.pack()
    boton_rk41.pack()
    boton_volver.pack()

def opciones_interpolacion():
    ocultar_botones()
    interfaz_interpolacion.pack()
    boton_poli_simple.pack()
    boton_lagrange.pack()
    boton_MC.pack()
    boton_volver.pack()

def opciones_ceros():
    ocultar_botones()
    interfaz_Ceros.pack()
    boton_ceros_mtAbierto.pack()
    boton_ceros_mtCerrado.pack()
    boton_volver.pack()

def res_secante(secante_resultado):
    valores1 = secante_entry_f.get()#funcion
    valores2 = float(secante_entry2_x0.get())#x0
    valores3 = float(secante_entry3_x1.get())#x1
    valores4 = float(secante_entry4_tol.get())#f
    f = lambda t,y: eval(valores1)
    P,I = cs.Secante(f, valores2, valores3, valores4)
    newton_resultado.config(text=f'La raiz o el cero de la funcion usando newton es {P} y la cantidad de iteraciones en newton es {I}')

def res_falsa_pos(falsa_pos_resultado):
    valores1 = falsa_pos_entry_f.get()#funcion
    valores2 = float(falsa_pos_entry2_a.get())#x0
    valores3 = float(falsa_pos_entry3_b.get())
    valores4 = float(falsa_pos_entry4_tol.get())
    f = lambda m: eval(valores1)
    P, I = cs.falsaPos(f, valores2, valores3, valores4)
    falsa_pos_resultado.config(text=f'La raiz o el cero de la funcion usando falsa posicion es {P} y la cantidad de iteraciones en falsa posicion es {I}')

def res_biseccion(biseccion_resultado):
    valores1 = biseccion_entry_f.get()#funcion
    valores2 = float(biseccion_entry2_a.get())#x0
    valores3 = float(biseccion_entry3_b.get())
    valores4 = float(biseccion_entry4_tol.get())
    f = lambda m: eval(valores1)
    P, I = cs.Biseccion(f, valores2, valores3, valores4)
    biseccion_resultado.config(text=f'La raiz o el cero de la funcion usando biseccion es {P} y la cantidad de iteraciones en biseccion es {I}')

def res_newton(newton_resultado):  
    #x = sp.symbols('x')
    valores1 = newton_entry.get()#funcion
    valores2 = float(newton_entry2.get())#x0
    valores3 = float(newton_entry3.get())#tol
    f = lambda x: eval(valorf)
    P,I = cs.newtonR(f, valores2, valores3)
    newton_resultado.config(text=f'La raiz o el cero de la funcion usando newton es {P} y la cantidad de iteraciones en newton es {I}')

def res_MC(MC_resultado):
    valor1 = MC_entry.get()
    valores1 = [float(x) for x in valor1.split(",")]
    valor2 = MC_entry2.get()
    valores2 = [float(x) for x in valor2.split(",")]
    xd = np.array(valores1)
    yd = np.array(valores2)
    P, X = mt.MC(xd, yd)
    MC_resultado.config(text=f'El polinomio interpolante es P(x) = {X}')

def res_euler(euler_resultado):
    valorf = euler_entry3_f.get()
    valora = float(euler_entry_a.get())
    valorb = float(euler_entry2_b.get())
    valor_h = float(euler_entry5_h.get())
    valor_co = float(euler_entry4_co.get())
    

   
    f = lambda t,y: eval(valorf)
    t, eu = mt.Euler(f, valora, valorb, valor_h, valor_co)
    euler_resultado.config(text=f'El polinomio interpolante es P(x) = {eu}')
    

def res_rk41(rk41_resultado):
    valorf = rk41_entry3_f.get()
    valora = float(rk41_entry_a.get())
    valorb = float(rk41_entry2_b.get())
    valor_h = float(rk41_entry5_h.get())
    valor_co = float(rk41_entry4_co.get())
    f = lambda t,y: eval(valorf)
    t, rk = mt.Runge(f, valora, valorb, valor_h, valor_co)
    rk41_resultado.config(text=f'El polinomio interpolante es P(x) = {rk}')
    

def res_lagrange(lg_resultado):
    valor1 = lg_entry.get()
    valores1 = [float(x) for x in valor1.split(",")]
    valor2 = lg_entry2.get()
    valores2 = [float(x) for x in valor2.split(",")]
    xd = np.array(valores1)
    yd = np.array(valores2)
    P = mt.Pol_Lagrange(xd, yd)
    lg_resultado.config(text=f'El polinomio interpolante es P(x) = {P}')


def res_poli(resultado, lbl_aproximacion):
    valor1 = entry.get()
    valores1 = [float(x) for x in valor1.split(",")]
    xd = np.array(valores1)
    valor2 = entry2.get()
    valores2 = [float(x) for x in valor2.split(",")]
    yd = np.array(valores2)
    #xd = np.array([0,0.6,0.9])
    #yd = np.array([1, 1.264911, 1.378404])
    P, X = mt.poli_simple(xd, yd)
    resultado.config(text=f'El polinomio interpolante es P(x) = {X}')
    entry_aprox.pack()
    boton_aproximar = tk.Button(interfaz_poli, text="Resolver polinomio", command=lambda: aprox_poli(P, lbl_aproximacion))
    boton_aproximar.pack()
    lbl_aproximacion.pack()

def aprox_poli(P, lbl_aproximacion):
    aprox_valor = float(entry_aprox.get())
    lbl_aproximacion.config(text=f'El polinomio interpolante es P(x) = {P(aprox_valor)}')
    
def mostrar_interfaz2():
    ocultar_botones()
    interfaz_EDO1.pack()
    boton_volver.pack()

def mostrar_interfaz3():
    ocultar_botones()
    #interfaz3.pack()
    boton_volver.pack()

def mostrar_interfaz4():
    ocultar_botones()
    interfaz4.pack()
    boton_volver.pack()


def volver_al_menu():
    interfaz_falsa_pos.pack_forget()
    interfaz_biseccion.pack_forget()
    interfaz_secante.pack_forget()
    interfaz_ceros_mtCerrado.pack_forget()
    interfaz_ceros_mtAbierto.place_forget()
    interfaz_euler.pack_forget()
    interfaz_rk41.pack_forget()
    interfaz_EDO1.pack_forget()
    interfaz_MC.pack_forget()
    interfaz_lagrange.pack_forget()
    interfaz_interpolacion.pack_forget()
    interfaz_poli.pack_forget()
    interfaz_EDO1.pack_forget()
    interfaz_ceros_mtAbierto.pack_forget()
    interfaz_Ceros.pack_forget()
    interfaz_newton.pack_forget()
    interfaz4.pack_forget()
    boton_volver.pack_forget()
    mostrar_botones()

# Función para ocultar los botones del menú
def ocultar_botones():
    boton_ceros_biseccion.pack_forget()
    boton_ceros_falsa_pos.pack_forget()
    boton_ceros_newton.pack_forget()
    boton_ceros_secante.pack_forget()
    boton_ceros_mtAbierto.pack_forget()
    boton_ceros_mtCerrado.pack_forget()
    boton_rk41.pack_forget()
    boton_euler1.pack_forget()
    boton_MC.pack_forget()
    boton_lagrange.pack_forget()
    boton_interfaz_interpolacion.pack_forget()
    boton_poli_simple.pack_forget()
    boton_interfaz2.pack_forget()
    boton_interfaz3.pack_forget()
    boton_interfaz4.pack_forget()

# Función para mostrar los botones del menú
def mostrar_botones():
    boton_interfaz_interpolacion.pack()
    boton_interfaz2.pack()
    boton_interfaz3.pack()
    #boton_interfaz4.pack()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Menú con Interfaz Cambiable")
ventana.geometry("400x300")
# Crear botones del menú
boton_interfaz_interpolacion = tk.Button(ventana, text="Interpolación", command=opciones_interpolacion) #boton interfaz 1
boton_interfaz2 = tk.Button(ventana, text="Ecucaciones Diferenciales de Orden 1", command=opciones_EDO1)
boton_interfaz3 = tk.Button(ventana, text="Ceros", command=opciones_ceros)
boton_interfaz4 = tk.Button(ventana, text="Interfaz 4", command=mostrar_interfaz4)

# Crear botón para volver atrás
boton_volver = tk.Button(ventana, text="Volver al Menú", command=volver_al_menu)
boton_volver.pack_forget()

# Coloca los botones del menú en la ventana
mostrar_botones()

# Interfaz 1 - INTERPOLACION
interfaz_interpolacion = tk.Frame(ventana)
boton_poli_simple = tk.Button(interfaz_interpolacion, text="Polinomio simple", command=mostrar_interfaz_poli)
boton_lagrange = tk.Button(interfaz_interpolacion, text="Metodo de Lagrange", command=mostrar_interfaz_lagrange)
boton_MC = tk.Button(interfaz_interpolacion, text="Metodo de Minimos", command=mostrar_interfaz_MC)
interfaz_interpolacion.pack_forget()

###################################

#Interfaz - INTERPOLACION POLINOMIAL
interfaz_poli = tk.Frame(interfaz_interpolacion)
label_dato = tk.Label(interfaz_poli, text="Por favor ingrese sus datos: ")
entry = tk.Entry(interfaz_poli)
entry2 = tk.Entry(interfaz_poli)
entry_aprox = tk.Entry(interfaz_poli)

#Label de la solución
resultado= tk.Label(interfaz_poli, text="")
lbl_aproximacion = tk.Label(interfaz_poli, text= "")

#botón para resolver el polinomio
boton_resolver = tk.Button(interfaz_poli, text="Resolver polinomio", command=lambda: res_poli(resultado, lbl_aproximacion))


# Posicionar elementos en la interfaz 1
label_dato.pack()
entry.pack()
entry2.pack()
boton_resolver.pack()
resultado.pack()

interfaz_poli.pack_forget()
################################################

# Interfaz INTERPOLACION LAGRANGE

interfaz_lagrange = tk.Frame(interfaz_interpolacion)
lg_label_dato = tk.Label(interfaz_lagrange, text="Por favor ingrese sus datos: ")
lg_entry = tk.Entry(interfaz_lagrange)
lg_entry2 = tk.Entry(interfaz_lagrange)
lg_resultado= tk.Label(interfaz_lagrange, text="")

#botón para resolver el polinomio
lg_boton_resolver = tk.Button(interfaz_lagrange, text="Resolver polinomio", command=lambda: res_lagrange(lg_resultado))

lg_label_dato.pack()
lg_entry.pack()
lg_entry2.pack()
lg_boton_resolver.pack()
lg_resultado.pack()
interfaz_lagrange.pack_forget()
##################################################

#Interfaz MC 

interfaz_MC = tk.Frame(interfaz_interpolacion)
MC_label_dato = tk.Label(interfaz_MC, text="Por favor ingrese sus datos: ")
MC_entry = tk.Entry(interfaz_MC)
MC_entry2 = tk.Entry(interfaz_MC)
MC_resultado= tk.Label(interfaz_MC, text="")

#botón para resolver el polinomio
MC_boton_resolver = tk.Button(interfaz_MC, text="Resolver polinomio", command=lambda: res_MC(MC_resultado))

MC_label_dato.pack()
MC_entry.pack()
MC_entry2.pack()
MC_boton_resolver.pack()
MC_resultado.pack()
interfaz_MC.pack_forget()


####################################################
# Interfaz 2  EDO 1 EULER Y RK4

interfaz_EDO1 = tk.Frame(ventana)
boton_euler1 = tk.Button(interfaz_EDO1, text="Metodo de Euler", command=mostrar_interfaz_euler1)
boton_rk41 = tk.Button(interfaz_EDO1, text="Metodo de Runge-Kutta", command=mostrar_interfaz_rk41)
interfaz_EDO1.pack_forget()

######################################################

# Interfaz Runge-Kutta
interfaz_rk41 = tk.Frame(interfaz_EDO1)
rk41_label_dato = tk.Label(interfaz_rk41, text="Por favor ingrese sus datos: ")
rk41_entry_a= tk.Entry(interfaz_rk41, fg="grey")
add_placeholder(rk41_entry_a, "Introduce a")
rk41_entry2_b = tk.Entry(interfaz_rk41)
add_placeholder(rk41_entry2_b, "Introduce b")
rk41_entry3_f = tk.Entry(interfaz_rk41)
add_placeholder(rk41_entry3_f, "Introduce la función")
rk41_entry4_co = tk.Entry(interfaz_rk41)
add_placeholder(rk41_entry4_co, "Introduce co")
rk41_entry5_h = tk.Entry(interfaz_rk41)
add_placeholder(rk41_entry5_h, "Introduce h")
rk41_resultado= tk.Label(interfaz_rk41, text="")


#botón para resolver el polinomio
rk41_boton_resolver = tk.Button(interfaz_rk41, text="Resolver polinomio", command=lambda: res_rk41(rk41_resultado))

rk41_label_dato.pack()
rk41_entry3_f.pack()
rk41_entry_a.pack()
rk41_entry2_b.pack()
rk41_entry5_h.pack()
rk41_entry4_co.pack()
rk41_boton_resolver.pack()
rk41_resultado.pack()
interfaz_rk41.pack_forget()
#########################

# INTERFAZ EULER 
interfaz_euler = tk.Frame(interfaz_EDO1)
euler_label_dato = tk.Label(interfaz_euler, text="Por favor ingrese sus datos: ")
euler_entry_a= tk.Entry(interfaz_euler, fg="grey")
add_placeholder(euler_entry_a, "Introduce a")
euler_entry2_b = tk.Entry(interfaz_euler)
add_placeholder(euler_entry2_b, "Introduce b")
euler_entry3_f = tk.Entry(interfaz_euler)
add_placeholder(euler_entry3_f, "Introduce la función")
euler_entry4_co = tk.Entry(interfaz_euler)
add_placeholder(euler_entry4_co, "Introduce co")
euler_entry5_h = tk.Entry(interfaz_euler)
add_placeholder(euler_entry5_h, "Introduce h")
euler_resultado= tk.Label(interfaz_euler, text="")


#botón para resolver el polinomio
euler_boton_resolver = tk.Button(interfaz_euler, text="Resolver polinomio", command=lambda: res_euler(euler_resultado))

euler_label_dato.pack()
euler_entry3_f.pack()
euler_entry_a.pack()
euler_entry2_b.pack()
euler_entry5_h.pack()
euler_entry4_co.pack()
euler_boton_resolver.pack()
euler_resultado.pack()
interfaz_euler.pack_forget()

######################################
# Interfaz 3 - Ceros 
interfaz_Ceros = tk.Frame(ventana)
boton_ceros_mtAbierto = tk.Button(interfaz_Ceros, text="Metodo Abierto", command=mostrar_interfaz_ceros_abiertos)
boton_ceros_mtCerrado = tk.Button(interfaz_Ceros, text="Metodo de Cerrado", command=mostrar_interfaz_ceros_cerrados)
interfaz_Ceros.pack_forget()

#####################################
# Interfaz metodos abiertos
interfaz_ceros_mtAbierto = tk.Frame(interfaz_Ceros)
boton_ceros_newton = tk.Button(interfaz_ceros_mtAbierto, text="Metodo de Newton", command=mostrar_interfaz_newton)
boton_ceros_secante = tk.Button(interfaz_ceros_mtAbierto, text="Metodo de Secante", command=mostrar_interfaz_secante)
interfaz_ceros_mtAbierto.pack_forget()

#####################################
# Interfaz metodos Cerrados
interfaz_ceros_mtCerrado = tk.Frame(interfaz_Ceros)
boton_ceros_biseccion = tk.Button(interfaz_ceros_mtCerrado, text="Metodo de Biseccion", command=mostrar_interfaz_biseccion)
boton_ceros_falsa_pos = tk.Button(interfaz_ceros_mtCerrado, text="Metodo de Falsa Posición", command=mostrar_interfaz_falsa_pos)
interfaz_ceros_mtCerrado.pack_forget()
#####################################

# Metodo de Biseccion

interfaz_biseccion = tk.Frame(interfaz_ceros_mtCerrado)
biseccion_label_dato = tk.Label(interfaz_biseccion, text="Por favor ingrese sus datos: ")
biseccion_entry_f = tk.Entry(interfaz_biseccion)
biseccion_entry2_a = tk.Entry(interfaz_biseccion)
biseccion_entry3_b = tk.Entry(interfaz_biseccion)
biseccion_entry4_tol = tk.Entry(interfaz_biseccion)
biseccion_resultado= tk.Label(interfaz_biseccion, text="")

#botón para resolver el polinomio
biseccion_boton_resolver = tk.Button(interfaz_biseccion, text="Resolver polinomio", command=lambda: res_biseccion(biseccion_resultado))

biseccion_label_dato.pack()
biseccion_entry_f.pack()
biseccion_entry2_a.pack()
biseccion_entry3_b.pack()
biseccion_entry4_tol.pack()
biseccion_boton_resolver.pack()
biseccion_resultado.pack()
interfaz_biseccion.pack_forget()

########################
# Metodo de Falsa Posición

interfaz_falsa_pos = tk.Frame(interfaz_ceros_mtCerrado)
falsa_pos_label_dato = tk.Label(interfaz_falsa_pos, text="Por favor ingrese sus datos: ")
falsa_pos_entry_f = tk.Entry(interfaz_falsa_pos)
falsa_pos_entry2_a = tk.Entry(interfaz_falsa_pos)
falsa_pos_entry3_b = tk.Entry(interfaz_falsa_pos)
falsa_pos_entry4_tol = tk.Entry(interfaz_falsa_pos)
falsa_pos_resultado= tk.Label(interfaz_falsa_pos, text="")

#botón para resolver el polinomio
falsa_pos_boton_resolver = tk.Button(interfaz_falsa_pos, text="Resolver polinomio", command=lambda: res_falsa_pos(falsa_pos_resultado))

falsa_pos_label_dato.pack()
falsa_pos_entry_f.pack()
falsa_pos_entry2_a.pack()
falsa_pos_entry3_b.pack()
falsa_pos_entry4_tol.pack()
falsa_pos_boton_resolver.pack()
falsa_pos_resultado.pack()
interfaz_falsa_pos.pack_forget()

########################

# Metodo de newton

interfaz_newton = tk.Frame(interfaz_ceros_mtAbierto)
newton_label_dato = tk.Label(interfaz_newton, text="Por favor ingrese sus datos: ")
newton_entry = tk.Entry(interfaz_newton)
newton_entry2 = tk.Entry(interfaz_newton)
newton_entry3 = tk.Entry(interfaz_newton)
newton_resultado= tk.Label(interfaz_newton, text="")

#botón para resolver el polinomio
newton_boton_resolver = tk.Button(interfaz_newton, text="Resolver polinomio", command=lambda: res_newton(newton_resultado))

newton_label_dato.pack()
newton_entry.pack()
newton_entry2.pack()
newton_entry3.pack()
newton_boton_resolver.pack()
newton_resultado.pack()
interfaz_newton.pack_forget()

########################

# Metodo de secante 


interfaz_secante = tk.Frame(interfaz_ceros_mtAbierto)
secante_label_dato = tk.Label(interfaz_secante, text="Por favor ingrese sus datos: ")
secante_entry_f = tk.Entry(interfaz_secante)
secante_entry2_x0 = tk.Entry(interfaz_secante)
secante_entry3_x1 = tk.Entry(interfaz_secante)
secante_entry4_tol = tk.Entry(interfaz_secante)
secante_resultado = tk.Label(interfaz_secante, text="")

#botón para resolver el polinomio
secante_boton_resolver = tk.Button(interfaz_secante, text="Resolver polinomio", command=lambda: res_secante(secante_resultado))

secante_label_dato.pack()
secante_entry_f.pack()
secante_entry2_x0.pack()
secante_entry3_x1.pack()
secante_entry4_tol.pack()
secante_boton_resolver.pack()
secante_resultado.pack()
interfaz_secante.pack_forget()

###################################################

# Interfaz 4
interfaz4 = tk.Label(ventana, text="Interfaz 4")
interfaz4.pack_forget()

ventana.mainloop()

