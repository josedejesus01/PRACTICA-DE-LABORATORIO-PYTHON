# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:50:55 2020

@author: JOSE
"""

def factorial(n):# se define el metodo factorial
    if n == 1:#se hace uso de un if para la condicion
        return 1#base
    else:
        return n*factorial(n-1)#es el metodo recursivo
    
print ( factorial(7))#imprime el mensaje para realizar la ooeracion
 
 
