#FUNCIONES SIN PARAMETROS

def saludo():
    print ("Hola mundo!")

def abecedario():
        print("a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\nñ\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz")

def formulaResolvente():
        print("          -------------- ")
        print("         /               ")
        print("-b +- \_/ (b)^2 - 4.a.c  ")
        print("-------------------------")
        print("           2.a           ")
    
def dibujo():
        print("       ___________________________________________ ")
        print("      |   ::  ::     ::     ::           ::       |")
        print("      |   ::  ::   ::  ::   ::         :: ::      |")
        print("      |   ::::::  ::    ::  ::        ::   ::     |")
        print("      |   ::  ::   ::  ::   ::       :::::::::    |")
        print("      |   ::  ::     ::     ::::::  ::       ::   |")
        print("      |___________________________________________|")

def funcionUnion():
    conjunto1 = set(input("Ingrese los elementos del primer conjunto separados por espacios: ").split())
    conjunto2 = set(input("Ingrese los elementos del segundo conjunto separados por espacios: ").split())

    union = conjunto1|conjunto2
    return union

print(saludo())

print(abecedario()) 

print(formulaResolvente())

print(dibujo())   

resultado = funcionUnion()
print("La unión de los conjuntos es:", resultado)

