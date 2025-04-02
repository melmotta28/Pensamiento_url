"""n=int(input("Tamaño array: "))
m=int(input("Múltiplos: "))
salida=[]
for i in range (0,n):
    salida.append (i*m)
print(salida)

#2
cant=int(input("Ingrese el tamaño de los arreglos"))
nombres=[]
longg=[]
for i in range (cant):
    nombre=input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)
    longg.append(len(nombre))
print(nombres)
print(longg)"""

#Escenario1
cli=int(input("Ingrese la cantidad de clientes: "))
cal=[]
print("Excelente: 5 \nMuy bueno: 4 \nBuena: 3 \nRegular: 2 \nMala: 1")
for i in range (cli):
   
    res=int(input("Ingrese la calificación de 1 a 5: "))
    cal.append(res)
cont5=cal.count(5)
cont4=cal.count(4)
cont3=cal.count(3)
cont2=cal.count(2)
cont1=cal.count(1)
print(f"Calificaron excelente {cont5} veces")
print(f"Calificaron muy bueno {cont4} veces")
print(f"Calificaron bueno {cont3} veces")
print(f"Calificaron regular {cont2} veces")
print(f"Calificaron mala {cont1} veces")
frec=max(cal)
print(f"La respuesta más frecuente fue {frec}")
prom=sum(cal)/cli
print(f"El promedio es {prom}")
men=[ev for ev in cal if ev < prom]
porc=(len(men)/cli)*100
print(f"Menores al promedio {porc}")
