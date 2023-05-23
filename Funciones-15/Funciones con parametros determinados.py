#FUNCIONES CON PARAMETROS PREDETERMINADOS

titulo= ""

#Funcion que subraya una frase ingresada
def subrayar(titulo,subrayado="_"):
      titulo = input ("Ingrese titulo: ")
      print (titulo)
      print (subrayado*len(titulo))
     
#Funcion que determina el area de un triangulo
def areaTriangulo(base=2, altura=2):
      print("El area del triangulo es de: ")
      resultado= (base*altura)/2
      return (resultado) 


#Funcion que determina el area de un rectangulo
def areaRectangulo(base=2, altura=2):
    print("El area del rectangulo es de: ")
    return base * altura

#Funcion que imprime por pantalla una lista de numeros predeterminados
def imprimirLista(numeros=[]):
    print("Su lista de numeros es la siguiente: ")
    for numero in numeros:
        print(numero)


# Funcion que comprueba si un número es par
def numeroPar(numero=0):
    return numero % 2 == 0

#sugerencias : 
funcion1: 
def subrayar(titulo, subrayado="_"):
    print(titulo)
    print(subrayado * len(titulo))

titulo = input("Ingrese título: ")
subrayar(titulo)

funcion2:
def areaTriangulo(base=2, altura=2):
          print("El área del triángulo es de:")
          resultado = (base * altura) / 2
    return resultado

print(areaTriangulo(5, 6))


funcion3:
def areaRectangulo(base=2, altura=2):
    print("El área del rectángulo es de:")
    return base * altura

area = areaRectangulo(5, 6)
print(area)

funcion4:
def imprimirLista(numeros=[]):
    print("Su lista de números es la siguiente:")
    for numero in numeros:
        print(numero)

imprimirLista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

      
funcion5:
def numeroPar(numero=0):
    return numero % 2 == 0

print(numeroPar(5))
      






subrayar(titulo)

print(areaTriangulo(5,6))

area = areaRectangulo(5, 6)
print(area)

imprimirLista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print (numeroPar(10))
