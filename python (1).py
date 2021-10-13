#Programacion 2
#Profesor = Matías Bordone
#TP N°3: [Listas] and "Strings"
#Integrantes: [Fernanda Manzano, Santiago Romero]

#Ejercicio 1
print('Ejercicio 1')
def reverse_range():
    list_1 = [0,1,2,3,4,5,6,7,8,9,10]
    list_1.reverse()
    print (list_1)
reverse_range()

#Ejercicio 2

print('Ejercicio 2')
list_2 = [1,2,3,4,5,6,7]
suma_de_lista = sum(list_2)
print (suma_de_lista)


#Ejercicio 3

print('Ejercicio 3')
lista_3 = [1,2,3,4]
i = 0
prod = 1
while i < len(lista_3):
    prod = prod * lista_3[i]
    i += 1
    
print (prod)

#Ejercicio 4

print('Ejercicio 4')
def longitud():
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    total = 0

    for dia in dias:
        total += 1

    print(total)
longitud()


#Ejercicio 5
print('Ejercicio 5')
def es_vocal (c):
    if c == "a" or c == "e" or c == "i" or c == "o" or c== "u":
        return True

    elif c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
        return True

    return False

caracter = input("Introduce un Caracter () ")
print(es_vocal(caracter))

#Ejercicio 6
print('Ejercicio 6')
def intercambiar_dos():
    primeraPalabra = input("Ingrese la primera palabra [] ")
    segundaPalabra = input("Ingrese la segunda palabra [] ")
    primerCaracter = primeraPalabra[0]
    segundoCaracter = segundaPalabra[0]
    lista1= list (primeraPalabra)
    lista2= list (segundaPalabra)
    lista1[0] = segundoCaracter
    lista2[0] = primerCaracter
    palabraFinal = "".join(lista1) + " " + "".join(lista2)
    print (palabraFinal)
intercambiar_dos()

#Ejercicio 7
print('Ejercicio 7')
def dar_vuelta():
    palabra  = 'hola'
    reverso = palabra[::-1]
    print (reverso)
dar_vuelta()

#Ejercicio 8
print('Ejercicio 8')
def es_palindromo():
    palabra = "oso"

    if str(palabra) == str(palabra)[::-1]:
        print(True)
    else:
        print(False)
es_palindromo()
    
# #Ejercicio 9
print('Ejercicio 9')
def elementos_comunes(lista1, lista2):  
    tf = False
    for x in numeros_1:
        for i in numeros_2:
            if i == x:
             tf = True            
    return tf

numeros_1 = [0,30,1]
numeros_2 = [2,7,8,9]

resultado = elementos_comunes(numeros_1, numeros_2)
print (resultado)

#Ejercicio 10
print('Ejercicio 10')
def generar_n_caracteres(n, char):
    r = n * char
    print (r)
    
generar_n_caracteres(10, "n")

#Ejercicio 11
print('Ejercicio 11')
def procedimiento(lista, caracter='*'):
    for e in lista:
       print (caracter * e)
lista=[1,3,9,20,4,6]
procedimiento (lista)
print()

    
        
    

      
      
    

 
 
 

    



