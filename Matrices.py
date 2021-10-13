#1)
miLista = [1024, 3, True, 6.5] #lista 1024, si 3 esta dentro de 6.5 es verdadero
miLista.append(False) #mi lista 3 verdadera 
miLista.insert(2,4.5) #inserta a la lista el 2.4.5 
print(miLista.pop()) #vuelve a llamar a la lista
print(miLista.pop(1)) #imprime la lista con el primer elemento
miLista.pop(2) #imprime la lista, el segundo elemento de la lista
miLista.sort() #crea una nueva lista a partir de la anterior
miLista.reverse() #da vuelta la lista
print(miLista.count(6.5)) 
print(miLista.index(4.5))
miLista.remove(6.5)
del miLista[0]

#2)
"""
a=[3,3,3,3,3,3,3,3,3]
for i in range (10):
    print(a[i])
"""  
#a-¿Que pasó? SyntaxError: invalid syntax (<string>, line 1)
#b-¿en que linea esta el problema? El problema esta en la linea 1
#-Busque en internet que quiere decir ese problema y explicarlo con sus palabras. IndexError: list index out of range, tiene el rango 10 y necesita imprimir 9 elementos.
#d-Corrija el programa para que funcione
    
a=[3,3,3,3,3,3,3,3,3]
for i in range (9):
    print(a[i])

#3-
def cuantospares() :
lista.agregaritems(2,3,4,5,1,0)
lista.tamaño ()
return cuantospares()
    
#4-
lista = [2,2,3,4]

def sumaLista(lista):
    aux = 0
    for i in lista:
        aux = aux + i
    return aux
print(sumaLista(lista))

def multiplicaLista(lista):
    aux = 1
    for i in lista:
        aux = aux * i
    return aux
print(multiplicaLista(lista))

#5-
def maximoenlista (): 
   lista.agregaritems(1,0,3,4)
   lista.extraer()
   return()

#6-
lista.agregaritems[cara,kombucha,santi,tiene,jiji]
lista.agregaritems(4)
lista.filterpalabras(4) 
return()

#7-
def productoEscalar(vector1, vector2):
    producto = 0
    for i in range(len(vector1)):
        producto += vector1[i] * vector2[i]
    return producto

vector1 = (1,2)
vector2 =(3,4)

print("Producto escalar de los vectores: ", productoEscalar(vector1, vector2))

#8- 
def elimina_duplicados():
    sinduplicados = set(lista)
    return (sinduplicados)

numeros = [4,6,4,1,2,6,7,8,9,0,8,6]

print (elimina_duplicados(numeros))

#9-
def creaMatriz(n, m):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(0)
    return matriz

n = int(input("Cantidad de filas: "))
m = int(input("Cantidad de columnas: "))
p = creaMatriz(n, m)
print(p)

#10-
def filas(matriz):
    return len(matriz)

def columnas(matriz):
    return len(matriz[0])

matriz = [[1,2,3],[4,5,6]]
print("Cantidad de filas: ",filas(matriz))
print("Cantidad de columnas: ",columnas(matriz))

#11-

matriz = [[1, 3, 5],[7, 9, 10]]

def enumF(matriz):
    c=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            c=c+1
            print(c,end="")
        print()
print("Ejercicio a: ")
enumF(matriz)

def enumC(matriz):
    columna = 1
    fila = 0
    for i in range(len(matriz)):
        fila = fila + 1
        for j in range(len(matriz[0])):
            columna=columna+len(matriz)
            print(columna-((len(matriz[0]))-1),end="")
        columna = fila + 1
        print()
print("Ejericio b: ")
enumC(matriz)

#12-

def pares(matriz):
    aux = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] % 2 == 0:
                aux += 1
    return aux
  
#13-

def generarMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(0)
    return matriz

def suma(matriz1, matriz2):
    if len(matriz1) == len(matriz2):
        if len(matriz1[0]) == len(matriz2[0]):
            c = generarMatriz(len(matriz1), len(matriz1[0]))
            for i in range(len(matriz1)):
                for j in range(len(matriz1[0])):
                    c[i][j] = matriz1[i][j] + matriz2[i][j]
    return c
                    

matriz1 = [[1,2,3],[4,5,6]]
matriz2 = [[1,3,6],[5,2,4]]
print(suma(matriz1, matriz2))

#16-

def diagonal(matriz):
    aux = []
    for i in range(len(matriz)):
        aux.append(matriz[i][i])
    return aux

def sumaDiagonal():
    aux = 0
    for i in diagonal(matriz):
        aux += i
    return aux

def sumaLista(matriz):
    aux = 0
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            aux += matriz[i][j]
    return aux

matriz = [[1,2,3], [4,5,6], [5,2,4]]
print("Diagonal: ",diagonal(matriz))
print("Suma de la diagonal: ",sumaDiagonal())
print("Suma de los elementos de la matriz: ",sumaLista(matriz))

