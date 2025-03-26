for i in range(1,11):
    if i% 2!=0:
        print(i)
        
#2
x=1
while x<11:
    if x % 2!=0:
        print(x)
    x+=1
#Escenario1
while True:
    palabra=input("Ingresa una palabra: ")
    if palabra.lower()=="chupacabra":
        print("Has dejado el bucle con éxito")
        break

#Escenario2
palabra=input("Ingrese una palabra").upper()
vocales="AEIOU"
for letra in palabra:
    if letra in vocales:
        continue
    print(letra)