#Ejercicio 1
print ('Ejercicio [1]')

print ('Hola Mundo')

#Ejercicio 2
print ('Ejercicio [2]')

a = input("Introduce el primer número: ")
b = input("Introduce el segundo número: ")

sumarab = float(a)+float(b)
print("La suma es de: ", sumarab)


#Ejercicio 3
print ('Ejercicio [3]')

numeros = []  
for i in range(2):
  numero = float(input("Introduce el número: "))
  numeros.append(numero) 

mayor = numeros[0] 

for numero in numeros:
    if numero > mayor:
        mayor = numero
print("El numero mayor es: ", mayor)


#Ejercicio 4
print ('Ejercicio [4]')

max_de_tres = []

for i in range(3):
  numero = float(input("Introduce el número : "))
  max_de_tres.append(numero)

mayor = numeros[0]
for numero in max_de_tres:
    if numero > mayor:
        mayor = numero
        
print("El Numero Mayor es: ", mayor)

#Ejercicio 5
print ('Ejercicio [5]')

def entre0y10():
    numero = int(input("Ingrese el Numero {}: "))
    if numero < 11 and numero > 0:
        return True
    else:
        return False
        
print(entre0y10())

#Ejercicio 6
print ('Ejercicio [6]')

def entreAyB():
    A = int(input("Ingrese el Primer Nuemero: "))
    B = int(input("Ingrese el Segundo Numero: "))
    C = int(input("Ingrese el Tercer Numero: "))

    if C > A and C < B:
        return True
    else:
        return False

print(entreAyB())

#Ejercicio 7
print ('Ejercicio [7]')

def uno_al_cien_While():
    numero = 0
    while numero <= 100:
        print(numero)
        numero += 1
        
uno_al_cien_While()

#Ejercicio 8
print ('Ejercicio [8]')

def entreAyB():
    C = int(input("Ingrese un Numero: "))
    
    if C >= 11 and C <= 20:
        print("Un Mensaje")
    if C >= 21 and C <= 30:
        print("Otro Mensaje")
    else:
        print("Otro Mas")

entreAyB()

#Ejercicio 9
print ('Ejercicio [9]')

def uno_al_cien_For():
    numero = 0
    for i in range(100):
        numero += 1
        print(numero)
 
uno_al_cien_For()

#Ejercicio 10
print ('Ejercicio [10]')

def es_Par():
    a = int(input("ingrese el numero: "))
    if a % 2 == 0:
        print(True)
    else:
        print(False)

es_Par()

#Ejercicio 11
print ('Ejercicio [11]')

def es_Par():
    i = 0
    while i <= 100:
        if i % 2 == 0:
            print(i)
            i += 1
        else:
            i += 1
es_Par()

#Ejercicio 12
print ('Ejercicio [12]')

def numero_Entre5y10():
    import random
    print(random.randrange(1, 10))
    
numero_Entre5y10()
