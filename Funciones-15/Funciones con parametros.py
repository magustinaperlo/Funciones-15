#FUNCIONES CON PARAMETROS:

a = int(input("insertar termino cubico: "))
b = int(input("insertar termino cuadratico: "))
c = int(input("insertar termino lineal: "))
d = int(input("insertar termino independiente: "))
x = int(input("insertar varible:"))
pi = 3.14
r = int(input("insertar radio:"))
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Funcion Cubica
def funcionCubica(a,b,c,d,x):

    y= a*(x**3) + b*(x**2) + c*x + d

    return y


# Funcion cuadratica
def funcionCuadratica(b,c,d,x):

    y= b*(x**2) + c*x + d

    return y


# Funcion lineal
def funcionLineal(x,c,d):
    y= c*x + d

    return y


# Sacar area de circulo
def areaDeCirculo(r):
    area = pi* (r**2)
    return area

# Union de 2 conjuntos previamente establecidos
def union_de_conjuntos(conjunto_1, conjunto_2):
    union = conjunto_1.union(conjunto_2)
    return union


print(funcionCubica(a,b,c,d,x))

print(funcionCuadratica(b,c,d,x))

print(funcionLineal(c,d,x))

print(areaDeCirculo(r))

print(union_de_conjuntos(conjunto_a, conjunto_b))

#sugerencia:

import math

# Funciones con parámetros:

a = int(input("Insertar término cúbico: "))
b = int(input("Insertar término cuadrático: "))
c = int(input("Insertar término lineal: "))
d = int(input("Insertar término independiente: "))
x = int(input("Insertar variable: "))
pi = math.pi
r = int(input("Insertar radio: "))
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Función cúbica
def funcionCubica(a, b, c, d, x):
    y = a * (x ** 3) + b * (x ** 2) + c * x + d
    return y

# Función cuadrática
def funcionCuadratica(b, c, d, x):
    y = b * (x ** 2) + c * x + d
    return y

# Función lineal
def funcionLineal(x, c, d):
    y = c * x + d
    return y

# Calcular área de círculo
def areaDeCirculo(r):
    area = pi * (r ** 2)
    return area

# Unión de 2 conjuntos previamente establecidos
def union_de_conjuntos(conjunto_1, conjunto_2):
    union = conjunto_1.union(conjunto_2)
    return union

print(funcionCubica(a, b, c, d, x))
print(funcionCuadratica(b, c, d, x))
print(funcionLineal(x, c, d))
print(areaDeCirculo(r))
print(union_de_conjuntos(conjunto_a, conjunto_b))

