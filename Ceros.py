import numpy as np
import sympy as sp



def Biseccion(f,a,b,tol):
    if (f(a)*f(b)>0):
        print ("La funcion f no cumple el teoreoma de valor intermedio, busque otro intervalo")
    else:
        i=0
        while(np.abs(b-a)>tol):
            c=(a+b)/2
            if (f(a)*f(c)>0):
                a=c
            else:
                b=c
            i=i+1
        print("La raiz o el cero de la funcion usando biseccion es ", c)
        print("La cantidad de iteraciones usando biseccion es ", i)
        return c,i
    return 

def falsaPos(f,a,b,tol):
    if (f(a)*f(b)>0):
        print ("La funcion f no cumple el teoreoma de valor intermedio, busque otro intervalo")
    else:
        c=a-((f(a)*(a-b))/(f(a)-f(b)))
        i=0
        while(np.abs(f(c))>tol):
            c=a-((f(a)*(a-b))/(f(a)-f(b)))
            if (f(a)*f(c)>0):
                a=c
            else:
                b=c
            i=i+1
        print("La raiz o el cero de la funcion usando falsa posicion es ", c)
        print("La cantidad de iteraciones en falsa posicion es", i)
    return c,i

x=sp.symbols("x")

def newtonR(f_,xo,tol):
    x = sp.symbols("x")
    f = eval(f_)
    df=sp.diff(f,x)
    new=x-f/df
    new=sp.lambdify(x,new)
    x1=new(xo)
    i=1
    while(np.abs(x1-xo)>tol):
        xo=x1
        x1=new(xo)
        i+=1
    print ("La raiz de la funcion usando Newton es", x1)
    print("La cantidad de iteraciones usando Newton es", i)
    return x1, i
    
def Secante(f,xo,x1,tol):
    x2=x1-(f(x1)*(xo-x1)/(f(xo)-f(x1)))
    i=1
    while(np.abs(x2-x1)>tol):
        xo=x1
        x1=x2
        x2=x1-(f(x1)*(xo-x1)/(f(xo)-f(x1)))
        i+=1
    print("La raiz de la funcion usando Secante es", x2)
    print("El numero de iteraciones usandos Secante es", i)
    return x2, i