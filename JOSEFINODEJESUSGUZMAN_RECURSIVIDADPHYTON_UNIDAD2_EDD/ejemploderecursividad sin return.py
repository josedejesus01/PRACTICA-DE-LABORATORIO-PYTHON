# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:08:09 2020

@author: JOSE
"""


def jugar(intento=1):#se define nuestro metodo jugar con un metodo intento
    respuesta = input("¿De qué color es una naranja? ") #se introduce el metodo de entrada con mensaje a ejecutar
    if respuesta != "naranja":  # se hace el uso de una condicional
        if intento < 3:#se asigan el numero a iterar
            print ("\nFallaste! Inténtalo de nuevo")#se manda a imprimir el mensaje
            intento += 1           #se itera el numero
            jugar(intento)  # Llamada recursiva   
        else:         
            print( "\nPerdiste!")# se manda a impreimir el mensaje de nuevo a ejecutar
    else:         
        print ("\nGanaste!")# se imprime el mensaje de que la ejecucion sea verdadera
jugar()# se imprime el metodo jugar para realizar la operacion
   

            
