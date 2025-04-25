def parimpar(n):
    if n%2==0: 
        print("Es par")
    else:
        print("Es impar")
num=int(input("Ingrese un número"))
parimpar(num)
#2
def sumaa(lista):
    return sum(lista)
nums=input("Ingrese una lista de números separados por una coma")
evt=[int(x) for x in nums.split(',')]
print("La suma es= ", sumaa(evt))
#3
def cntregr(n):
    if n>=0:
        print(n)
        cntregr(n-1)
strt=int(input("Ingrese el número para iniciar la cuenta regresiva"))
cntregr(strt)
#4
def ascd(n, act=1):
    if act>n:
        return
    print(act)
    ascd(n, act+1)
n=int(input("Ingrese el número tope"))
ascd(n)
#5
def sumun(n):
    if n==1:
        return n
    return n+sumun(n-1)
n=int(input("Ingresa el número tope para la suma"))
print("La suma es: ", sumun(n))
#6
def fact(n):
    if n==0 or n==1:
        return 1 
    return n * fact(n-1)
n=int(input("Ingresa un número para calcular el factorial"))
print(f"El factorial de {n} es: {fact(n)}")
#7
def min(lista):
    if not lista[1:]:
        return lista[0]
    menor=min(lista[1:])
    return lista[0] if lista[0]<menor else menor
entrada=input("Ingresa números separados por coma")
lista=[int(x) for x in entrada.split(',')]
print(min(lista))

