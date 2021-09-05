# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:56:28 2021

@author: riber
"""
#Calcule el valor de Y indicando paso a paso como llegó al resultado

#1. y = ( (5+2-5)^2 * 5+8/2 -30 ) / 2 * 5 -3
y = ( (5+2-5)**2 * 5+8/2 - 30 )  / 2 * 5 - 3 
print("1. Se resuelve el parentesis: ")
print("Esto es igual a: ", (5+2-5)**2)
print("2. Se multiplica la expresión :")
print("Esto es igual a: ", 45+8/2-30)
print("3. Se resta: -15-3")
print("El resultado es: ", y)

#2. z=5
#n=3
#m= z-n
#y = (( (z+2-n)^2 * m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3

#3. z=5
#n=( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3
#m= z^2*3+n
#y = ((( (z+2-n)^2 x m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4

#Realizar los algoritmos que den solución a la problemática presentada 
#en los siguientes ejercicios:

#ej1
def masa(presion, volumen, temperatura):
    
    return (presion * volumen) / (0.37 * (temperatura + 460))

presion = float(input('Digite la presion:'))
volumen = float(input('Digite el volumen:'))
temperatura = float(input('Digite la temperatura:'))

masaT = masa(presion, volumen, temperatura)

print('La masa calculada es: {}'.format(masaT))

#ej2
def puls(edad):
    
    return (200-edad)/10

edad = int(input('Escriba su edad: '))

pulsTotal = puls(edad)

print('Sus pulsaciones cada 10 segundos son: {}'.format(pulsTotal))

#ej3
per1 = float(input('Persona 1 digite su inversión: '))
per2 = float(input('Persona 2 digite su inversión: '))
per3 = float(input('Persona 3 digite su inversión: '))

totalInv=(per1+per2+per3)

per1Inv=((per1/totalInv)*100)
per2Inv=((per2/totalInv)*100)
per3Inv=((per3/totalInv)*100)

print('El porcentaje de la persona 1 es: {}'.format(per1Inv))
print('El porcentaje de la persona 2 es: {}'.format(per2Inv))
print('El porcentaje de la persona 3 es: {}'.format(per3Inv))
