

                
num=int(input("Ingrese el número que desee convertir: "))
if num >9:
    print("Número fuera del rango")
elif num<1:
    print("Número fuera del rango")
if num <= 3:
    print("El número en romanos es: " + num*'I')
elif num==4:
    print("El número en romanos es: IV" )
elif num>=5 and num<=8:
    print("El número en romanos es: " + 'V'+(int(num-5)*'I'))
elif num==9: 
    print("El número en romanos es: IX")
                      