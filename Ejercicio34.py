entrada=input("Ingrese una oración")
palabra=entrada.split()
print("Primer palabra:", {palabra[0]}, " última palabra: ", {palabra[-1]})

espacios=input("Ingrese una oración")
print(" ".join(espacios.split()))

correo=input("Ingrese un correo electrónico")
dominio=(correo.split('@')[-1])
print(dominio)

arc=input("Ingrese el tipo de archivo")
print(arc.endswith('pdf'))

orden=input("Ingrese una oración")
print(" ".join(orden.split()[::-1]))

bus=input("¿Qué es lo que desea?").lower()
if "canción" in bus:
    print("""¡Hola, bebé! ¿Como has estado? Tal vez no sepas quién habla 
    O tal vez, lo hayas olvidado. 
    Bebé, yo no soy tan malo Bebé, sabes que te amo""")
elif "poema" in bus: 
    print("Cada vez que pienso en ti, / se enciende mi corazón, / y al sentir que estás aquí, / me invade la emoción")
elif "carta" in bus:
    print("A tu lado me siento completamente seguro, valioso y querido")
elif "dicho" in bus:
    print("Ir viento en popa: significa que algo marcha bien.")
elif "refrán" or "refran" in bus:
    print("No es oro todo lo que reluce. Algo que parece muy bueno puede no serlo si se conoce en profundidad.")