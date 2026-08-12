#área  y perímetro de un círculo

#se importa la librería Math para diponer de la función PI

import math
print("Calcular el área y perímetro de un círculo.")
print(" ")

#nos permite leer datos del radio ingresados por el usuario
 
print("Ingrese el radio del circulo: ")
radio = float(input())

#formula para calcular area
# PI * r * r
#para agregar la funcion PI en python se agrega math.pi
#para elevar un número a una potencia se agrega math.pow y se agrega la variable y el subindice indica el numero al que se desea elevar dicha potencia


area = math.pi * math.pow(radio,2)

#formula para calcular perímetro
perimetro = 2 * math.pi * radio

print(" ")
print(f"El area del círculo es: {area:.2f} cm2.")
print(" ")
print(f"El perímetro del círculo es: {perimetro:.2f} cm.")
print(" ")
