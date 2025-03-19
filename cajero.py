saldo=3000
cont=1
inte=3
print("Su saldo es de: "+str(saldo))
while cont<=3:
    retiro=int(input("Ingrese el monto a retirar: "))
    if retiro<saldo:
        saldo-=retiro
        print("Retiro exitoso, saldo actual: "+str(saldo))
    elif retiro==0:
        break
    elif retiro==saldo:
        print("Retiro total exitoso, gracias por su uso.")
        break
    elif retiro>saldo:
        inte-=1
        if inte>0:
            print("Saldo Insuficiente, intentos restantes: "+str(inte))
        else:
            print("Ya no tiene más intentos")
            break
        