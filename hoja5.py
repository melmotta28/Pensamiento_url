consa=int(input("Ingrese la cantidad de consumo de agua en base a metros cúbicos: "))
habt=int(input("Ingrese la cantidad de habitantes en el apartamento: "))
if consa<15:
    print("La tarifa es de Q5 por metros cúbicos")
elif consa>=15 and consa<=30:
    if habt>3:
        print("La tarifa es de Q4 por metros cúbicos")
    elif habt==3:
        print("La tarifa es de Q4.5 por metros cúbicos")
    else:
        print("La tarifa es de Q5 por metros cúbicos")
elif consa>30:
    if habt>5:
        print("La tarifa es de Q3.5 por metro cúbico")
    elif habt % 2==0:
        print("La tarifa es de Q4 por metro cúbico")
    else:
        print("La tarifa es de Q4.2 por metro cúbico")
        
yr=int(input("Ingrese el año de su vehículo: "))
pl=int(input("Ingrese número de placa: "))
if yr>2001:
    if pl%10== 0 or pl%10== 2 or pl%10== 4 or  pl%10== 6 or pl%10== 8:
        print("No circula los lunes")
    elif pl%10==1 or pl%10== 3 or pl%10== 5 or pl%10== 7 or pl%10== 9:
        print("No circula los viernes")
if yr % 2==0:
    print("Restricción adicional, los sábados circula hasta medio día")
if yr<2001:
    print("ADVERTENCIA: Debe darle mantenimiento obligatorio a su vehículo")