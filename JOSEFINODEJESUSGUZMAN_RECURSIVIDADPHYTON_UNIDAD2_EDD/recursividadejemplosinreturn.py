# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:56:15 2020

@author: JOSE
"""

def imprimepir(n):# se define nuestro metodo
    if n<=1:#se hace la recursion de un if
        print ("*")#se imprime el mensaje 
    else:
        
        
        print("*"*n)#se imprime el mensaje con el valor de la variable n
        imprimepir(n-1) # se resta el numero introducido hasta que llegue menos uno

imprimepir(4)#se asigna un valor  a ejecutar