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

#ej4
montoBank = float(input('Digite el valor total de sus ahorros: '))

saldoFin=(montoBank * 0.015)

print('Su saldo al final sera de: {}'.format(saldoFin))

#ej5
sueldoBase = float(input('Digite su sueldo para realizar sus decuentos: '))

descLey=(sueldoBase * 0.01)
descSeguroS=(sueldoBase * 0.04)
descSeguroF=(sueldoBase * 0.005)
descCajaA=(sueldoBase * 0.05)

descTotal=(descLey+descSeguroS+descSeguroF+descCajaA)

print('Su monto total a pagar es: {}'.format(descTotal))

#ej6
palAviso = float(input('Digite el numero de palabras de su aviso: '))
centAviso = float(input('Digite el numero de centimetros de su aviso: '))
colAviso = float(input('Digite el numero de colores de su aviso: '))

palTotal=(palAviso * 20000)
centTotal=(centAviso * 15000)
colTotal=(colAviso * 25000)

montoPagar=(palTotal+centTotal+colTotal)

print('El monto a pagar por su aviso clasificado es: {}'.format(montoPagar))

#ej7
añosLab=int(input("Cuantos años tiene usted en esta empresa: "))

if añosLab==1:
    print("Su bono final es de: ", 100000)
if añosLab==0:
    print("Su bono final es de: ",0)
if añosLab>1:
    print("Su bono final es de: ",((añosLab-1)*120000)+100000)
    
#ej8
hrsTrabajadas = float(input('Digite sus horas trabajadas profe: '))

sueldoTotal = (hrsTrabajadas * 20000)
descConcepto = (sueldoTotal * 0.05)
montoPagar = (sueldoTotal - descConcepto)

print('Su descuento es: {}'.format(descConcepto))
print('Su sueldo final es: {}'.format(montoPagar))

#ej9
montoI = float(input('Digite su monto inicial: '))
montoF = float(input('Digite su monto final: '))

costoL = (montoI - montoF)
porL = (costoL * 0.20)
costoF = (costoL + porL)

print('El costo de su llamada fue: {}'.format(costoF))

#ej10
fotosRev = int(input('Digite cuantas fotos tiene su revelado: '))

precioTo = (fotosRev * 1500)
precioPo = (precioTo * 0.16)
precioFi = (precioTo + precioPo)

print('El monto que tiene que pagar por su revelado es: {}'.format(precioFi))
