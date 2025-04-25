import time

def gn(sn, att, st):
    if att == 0:
        print("¡Se acabaron los intentos! El número era:", sn)
        return
    
    ug = int(input("Ingresa tu intento: "))  
    
    if ug == sn:
        et = time.time() - st
        print("¡Felicidades! Adivinaste el número.")
        print(f"Te tomó {et:.2f} segundos.")
        return
    elif ug < sn:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")
    
    print(f"Te quedan {att - 1} intentos.")
    gn(sn, att - 1, st)

sn = 80 

print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print("¡Buena suerte!")

st = time.time()

gn(sn, 5, st)
