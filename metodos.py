import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')

def poli_simple(xdata, ydata):
    N= len(xdata)#Declaramos el grado del polinomio (graod o longitud del ydata o x data)
    M = np.zeros([N,N])#Declaramos la matriz
    for i in range(N):
        M[i,0]=1
        for j in range(1, N): #desde la segunda columna  hasta el grado del polinomio
            M[i,j] = M[i,j-1] * xdata[i]
    a_i = np.linalg.solve(M, ydata)
    P = 0
    for i in range(N):
        P=P+a_i[i]*x**i
    print('El polinomio interpolante es P(x)= ', P)
    return sp.lambdify(x, P), P


def Pol_Lagrange(xdata, ydata):
  N = len(xdata)
  P = 0
  for i in range(N):
    T = 1
    for j in range(N):
      if (j != i):
        T = T* (x-xdata[j])/(xdata[i] - xdata[j])
    P = P + T*ydata[i]
    P = sp.expand(P) #Para poner bonito y entendible el polinomio
  print("El polinomio es", P)
  return P

def MC(xd, yd):
  m = len(xd)
  sx = sum(xd)
  sx2 = sx**2
  sy = sum(yd)
  sxy = sum(xd*yd)
  scx = sum(xd**2)
  a0 = ((sy * scx) - (sx*sxy)) / ((m * scx) - sx2)
  a1 = (m*sxy - sx*sy) / (m*scx - sx2)
  print(a0)
  print(a1)
  expression = f'y = {a0:.4f} + {a1:.4f} * x'
  P = lambda x: a0 + a1 *x

  return P, expression




def Runge(f, a, b, h, co):
  n = int((b-a)/h)
  t = np.linspace(a, b, n+1)
  rk = [co]
  for i in range(n):
    k1 = h*f(t[i], rk[i])
    k2 = h*f(t[i]+h/2, rk[i] + 1/2*k1)
    k3 = h*f(t[i]+h/2, rk[i] + 1/2*k2)
    k4 = h*f(t[i+1], rk[i]+k3)
    rk.append(rk[i]+1/6*(k1+2*k2+2*k3+k4))

  return t, rk

def Euler(f, a, b, h, co):
  n = int((b-a)/h)
  t = np.linspace(a, b, n+1)
  eu = [co]
  for i in range(n):
    eu.append(eu[i]+h*f(t[i], eu[i]))
  return t, eu


def Trapecio(f, a, b, n):
  h=(b-a)/n
  s= 0
  for i in range(1, n):
    s += f(a+i*h)
  Int = (h/2) * (f(a)+ 2*s+f(b))
  print('La integral por trapecio es', Int)
  return Int

def sims13(f, a, b, n):
  if (n%2==0):
    sp = 0
    si = 0
    h = (b-a)/n
    for i in range(1, n):
      if (i%2==0):
        sp+=f(a+i*h)
      else:
        si+=f(a+i*h)
      Int = (h/3)*(f(a)+4*si+2*sp+f(b))
    print('La integral por medio de simpson 1/3 es', Int)
    return Int
  else:
    var = 'No se  puede calcular la integral por este metodo. N DEBE SER PAR.'
    return var


def sims38(f, a, b, n):
  if (n%3==0):
    sm3 = 0
    sn = 0
    h = (b-a)/n
    for i in range(1, n):
      if (i%3==0):
        sm3+=f(a+i*h)
      else:
        sn+=f(a+i*h)
      Int = (3*h/8)*(f(a)+3*sn+2*sm3+f(b))
    print('La integral por medio de simpson 1/8 es', Int)
    return Int
  else:
    var = 'No se  puede calcular la integral por este metodo. N DEBE SER MULTIPLO DE 3.'
    return var
    #print('No se  puede calcular la integral por este metodo. N DEBE SER MULTIPLO DE 3.')


# def euler_ED2(f,a,b,h,co):
#     n=int((b-a)/h)
#     t=np.linspace(a,b,n+1)
#     S=[co]
#     for i in range(n):
#         S.append(S[i]+h*f(t[i],S[i]))      
#     return t,np.array(S)

def euler_ED2(expression1, expression2, a, b, h, co):
    f1 = lambda t, u: eval(expression1.replace("v", "u[1]").replace("x", "u[0]"))
    f2 = lambda t, u: eval(expression2.replace("v", "u[1]").replace("x", "u[0]"))

    n = int((b - a) / h)
    t = np.linspace(a, b, n + 1)
    eu = [co]
    for i in range(n):
        u_i = eu[i]
        t_i = t[i]
        f_i = np.array([f1(t_i, u_i), f2(t_i, u_i)])
        eu.append(eu[i] + h * f_i)
    return t, eu

def rk42_ED2(expression1, expression2, a, b, h, var):
    f1 = lambda t, u: eval(expression1.replace("v", "u[1]").replace("x", "u[0]"))
    f2 = lambda t, u: eval(expression2.replace("v", "u[1]").replace("x", "u[0]"))

    n = int((b - a) / h)
    t = np.linspace(a, b, n + 1)
    w = [var]

    for i in range(n):
        k1 = h * np.array([f1(t[i], w[i]), f2(t[i], w[i])])
        k2 = h * np.array([f1(t[i] + h/2, w[i] + k1[0]/2), f2(t[i] + h/2, w[i] + k1[1]/2)])
        k3 = h * np.array([f1(t[i] + h/2, w[i] + k2[0]/2), f2(t[i] + h/2, w[i] + k2[1]/2)])
        k4 = h * np.array([f1(t[i + 1], w[i] + k3[0]), f2(t[i + 1], w[i] + k3[1])])
        w.append(w[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4))

    w = np.array(w)
    return t, w

def f(f1, f2, t, u):
  x = u[0] # x = Posición
  v = u[1] #v = velocidad
  f1_ = f1
  f2_ = f2
  return np.array([f1_, f2_])