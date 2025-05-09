def convertir_a_numero():
    text = input("Ingrese un texto para convertir a número: ")
    try:
        num = float(text)
        print("Número convertido:", num)
    except ValueError:
        print("Error: El texto no es un número válido.")

def abrir_archivo():
    nombre = input("Ingrese el nombre del archivo: ")
    try:
        with open(nombre, "r") as f:
            print("Contenido del archivo:")
            print(f.read())
    except FileNotFoundError:
        print("Error: El archivo no existe.")

def calculadora_division():
    try:
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador: "))
        print("Resultado:", a / b)
    except ValueError:
        print("Error: Entrada no válida, debe ingresar números.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

def acceder_lista():
    datos = input("Ingrese los elementos de la lista separados por comas: ").split(",")
    lista = [x.strip() for x in datos]
    try:
        index = int(input("Ingrese el índice al que desea acceder: "))
        print("Elemento en el índice:", lista[index])
    except IndexError:
        print("Error: Índice fuera de rango.")
    except ValueError:
        print("Error: Índice no válido.")

def ingresar_edad():
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            raise ValueError
        print("Edad ingresada:", edad)
    except ValueError:
        print("Error: Edad no válida.")

print("1. Convertir texto a número")
convertir_a_numero()

print("\n2. Abrir archivo")
abrir_archivo()

print("\n3. Calculadora división")
calculadora_division()

print("\n4. Acceder a una lista por índice")
acceder_lista()

print("\n5. Ingreso de edad")
ingresar_edad()
