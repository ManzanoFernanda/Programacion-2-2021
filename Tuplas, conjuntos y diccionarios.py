#Definir varias tuplas e imprimir sus elementos.

Tupla1 =('Casa')
Tupla2 =('Auto')
Tupla3 =('Perro')
print (Tupla1, Tupla2, Tupla3)


#Definir una función que tome una lista y devuelva el mayor y el menor en una tupla
def max_min():
    numeros = (3,-1,6,22)
    maximo = numeros[0]
    minimo = numeros[0]
    
    for i in numeros:
        if (i > maximo):
            maximo = i
        if (i < minimo):
            minimo = i
    
    return(maximo,minimo)
max_min()


#En el bloque principal del programa definir un diccionario que almacene los nombres de países como clave y como valor la cantidad de habitantes. Valores a guardar:
#Implementar una procedimiento para mostrar cada clave y valor.
#Implementar una función que tome el diccionario, calcule la poblacion total de latinoamerica y devuelva el valor (pista, usar un for para recorrer el diccionario)

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

paises=paises = {'Brasil':210147125,
              'Colombia':50372424,
              'Argentina':44938712,
              'Perú':32131400,
              'Venezuela':28670000,
              'Chile':19107216,
              'Ecuador':17300000,
              'Bolivia':11383940,
              'Paraguay':7152703,
              'Uruguay':3529140,
              'Guyana':761000,
              'Surinam':524000,
              'Guayana-Francesa':187000
              }
imprimir(paises)

total = sum(paises.values())
print('Poblacion total de Latinoamerica: ', total,'habitantes')


#Hacer un programa, que tome dos listas, las convierta en conjuntos y conteste si tiene los mismos elementos.

lista1=[1,2,3,15,20,40,54,23,98,60]
lista2=[3,1,7,95,42,40,9,15,6]

conjunto1=set(lista1)
conjunto2=set(lista2)

mismosElementos = (lista1) == (lista2)

print (mismosElementos)

#Hacer un programa, que tome dos listas, las convierta en conjuntos y devuelva los elementos de l1 que no están en l2

lista1=[1,2,3,15,20,40,54,23,98,60]
lista2=[3,1,7,95,42,40,9,15,6]

conjunto1=set(lista1)
conjunto2=set(lista2)

diferenciaLista1yLista2= conjunto1 - conjunto2

print(diferenciaLista1yLista2)






            


