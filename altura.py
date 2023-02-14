# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 12:09:32 2022

@author: andre
"""

g = 9.81
a0, v0 = input("Introduzca la altura inicial y la velocidad inicial:").split()
a0 = float(a0)
v0 = float(v0)
t = float(
    input("introduzca el valor del tiempo para el cual quieres calcular la altura:"))
y = a0+v0*t-0.5*g*t**2
print("la altura en el instante seleccionado es:", y)

"""Extra: la altura máxima
que alcanza"""
tiempo = v0/g
alt_maxima = a0+v0*tiempo-0.5*g*tiempo**2
print("la alatura máxima será entonces:", alt_maxima)
