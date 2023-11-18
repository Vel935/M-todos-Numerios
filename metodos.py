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


