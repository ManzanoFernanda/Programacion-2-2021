from math import pi
"""
1. A  Implementar una clase llamada AlumnoMateria con las partes Constructor, operaciones y condiciones.
Constructor: nombre, nota, materia
Operaciones: imprimir datos y mostrar_estado() {libre, regular, promocional}
Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero (entre 0 y 10)
"""
"""
class AlumnoMateria:
 
    def __init__(self, nombre, nota, materia):
        self.nombre = nombre
        self.nota = nota
        self.materia = materia
        self.__condicion = ""

    def __str__(self):
        return f"{self.nombre}, {self.nota}, {self.materia}"
 
    def mostrar_estado(self)->str:
        if self.nota < 4:
            self.__condicion = "Libre"
        elif self.nota >= 7:
            self.__condicion = "Promocional"
        else:
            self.__condicion = "Regular"
        return self.__condicion
    
a = AlumnoMateria("Juan", 10, "Lengua")
#assert a.__str__() == ("Juan", 10, "Lengua")
assert a.mostrar_estado() == "Promocional"
"""

"""
1.B Implementar la clase registroAlumnoMateria() que guarde varias notas y diga si el alumno está regular, promocional o libre. Con las siguientes reglas.
	Constructor: (Nombre, Materia)
	Agregar nota: Agrega una nota al alumno en la materia
	Promedio: Devuelve el promedio de notas que tiene el alumno
	Devolver lista de notas:
	Condición: Devuelve la condición del alumno {Promocional, Regular o libre}
	Reglas: 
	  +  si saca menos de 4 de promedio , queda libre
Promocion promedio de 7 y todas las notas 6 o mas.
Sino Regular:
	Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero
"""
"""
class Registro_Alumno_Materia:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia
        self.__notas = [] 
        self.__condicion = "Regular"

    def __str__(self):
        return f"{self.nombre}, {self.__notas}, {self.materia}, {self.__condicion}"

    def Calcular_Promedio(self):
        if len(self.__notas) == 0:
            prom = 0
        else:
            prom = sum(self.__notas) / len(self.__notas)
        return prom

    def Condicion(self)->str:
        Promedio = self.Calcular_Promedio()
        if Promedio < 4:
            self.__condicion = "Libre"
        elif Promedio >= 7 and min(self.__notas) >= 6:
            self.__condicion = "Promocional"
        else:
            self.__condicion = "Regular"
        return self.__condicion
    
    def Agregar_Nota(self, nota):
        self.__notas.append(nota)

    def Mostrar_Notas(self):
        return self.__notas

a=Registro_Alumno_Materia("Juan","Lengua")
a=(4)

"""
"""
2.a A la clase punto vista en la materia agregarle el método Distancia al origen ()siendo el origen el punto (0,0). Crear un programa que use este método para imprimir en pantalla la distancia entre al origen de los puntos A, B y C.
"""
"""
class Punto:
    def __init__(self, x=0, y=0): 
        self.par = (x,y)

    def __eq__(self, otro):
        return self.par == otro.par

    def __str__(self):
        return f"{self.par}"

    def Es_Origen(self):
        return self.par == (0,0)

    def Mover(self,dx,dy):
        self.par = (self.par[0] + dx,self.par[1] + dy)
                                               
    def Distancia(self,otro):
        return (((self.par[0]-otro.par[0])**2) + ((self.par[1]-otro.par[1])**2))**(1/2)

    def Distancia_Origen(self):
        return self.Distancia(Punto(0,0))
    
a=Punto(2,3)
print(a)
a.Mover(5,5)
print(a)
print(a.Es_Origen())
b=Punto()
print(b.Es_Origen())
c=Punto(6,5)
print(c)

"""
"""
2.b Utilizando el método de distancia al origen cree una función que tome una lista de puntos y devuelva el que se encuentra más alejado del origen.
"""
"""
def Mas_Lejos(puntos:[Punto]) -> Punto:
    Distancias = [punto.Distancia_Origen() for punto in Puntos]
    Indice_Lejano = Distancias.index(max(Distancias))
    return Puntos[Indice_Lejano]
    """

"""
3. Crear una clase circulo: 
constructor: punto(x, y), radio; 
operaciones:diametro,  perimetro y area.
#Tomar de ejempolo la clase rectangulo
"""
"""
class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        if radio <= 0:
            raise ValueError
        else:
            self.radio = radio
    
    def Diametro(self):
        return (2*self.radio)

    def Perimetro(self):
        return (2*pi*self.radio)

    def Area(self):
        return (pi*(self.radio**2))

    def __eq__(self, otro):
        return (self.centro == otro.centro and self.radio == otro.radio)

    def Mover(self, nuevo_centro):
        self.centro = nuevo_centro
        
centro = Circulo(0, 4.5)
print(centro.Diametro())
print(centro.Perimetro())
print(centro.Area())

"""
"""
4. Definir el TAD Fracción junto con su implementación en Clases.
	En python tenemos el tipo de dato float, pero no fraccion (numeros racionales)
    Constructor: arriba, abajo
    Operaciones: mostrar: convertir el objeto en cadena para poder imprimirlo = ⅓.
    Sumar (o restar) fracciones: suma de dos fracciones (tener en cuenta el denominador común)
	Igualdad: ¿Cuando dos fracciones son equivalentes?
"""
"""
class Fraccion:
    def __init__(self, num, Den=1): 
        self.numerador = num
        if Den == 0:
            raise ZeroDivisionError("Recuerda que el denominador no puede ser 0")
        else:
            self.denominador = Den

    def __str__(self):
        return (f"{self.numerador}/{self.denominador}")
    
    def __eq__(self, otro):
        return ((self.numerador/self.denominador)==(otro.numerador/otro.denominador))

    def comun_divisor(self, a, b):
        return a if not b else self.comun_divisor(b, a%b)

    def min_com_mult(self, a, b):
        return a*b//self.comun_divisor(a, b)

    def sumar_fracciones(self, otro):
        denominador = self.min_com_mult(self.denominador, otro.denominador)
        numerador = (denominador//self.denominador*self.numerador)+(denominador//otro.denominador*otro.numerador)
        return Fraccion(numerador,denominador)
    
a=Fraccion(2,4)
b=Fraccion(1,2)
"""
"""
5. Defina un tipo abstracto de datos nuevo que ustedes quieran inventar para esto. 
Piense en un caso de uso. ¿Qué información necesito manejar? Piense un ejemplo donde podria ser util este tipo de dato que queremos inventar.
Que datos necesito para crear una variable nueva del tipo que estoy inventando y como seria el constructor
Qué operaciones debería poder hacer con este tipo de dato nuevo.
Qué condiciones deberían cumplirse en mi tipo de dato nuevo.
Para contestar estas preguntas revisen los ejemplos dados en clase y los ejercicios anteriores de la guia.
Implemente el tipo de dato nuevo mediante clases en python.
"""
"""
global lista
lista = list()

class cajaregistradora:
    codigo_barras = ""
    nombre_producto = ""
    precio = [0]
   
    def registrarproducto():
        print("Ingrese el producto")
        print("--------------------------------------------------")

        registro = cajaregistradora()

        registro.codigo_barras = input("Ingrese el codigo de barras del producto: ")
        registro.nombre_producto = input("Ingrese el nombre del producto: ")
        registro.precio = float(input("Ingrese el precio del producto: "))

        lista.append(registro)

    def verlista():
        print("Listado de productos agregados a la compra")
        print("--------------------------------------------------")

        for registro in lista:
            print(registro.codigo_barras, "-", registro.nombre_producto, "-", registro.precio)

        print("")
        print("")

    def subtotal():
        print("")

        suma_total = 0

        for registro in lista:
            suma_total += registro.precio

        print("El total de su compra es de ", "=", suma_total)

    def pago():
        print("Ingrese cuanto ha pagado el cliente: ")

        pago = float(input())
        suma_final = 0

        for registro in lista:
            suma_final += registro.precio

        if pago > suma_final:
            print("Su cambio es: ", (pago - suma_final))
        elif pago < suma_final:
            print("Le falta pagar: ", (suma_final - pago))
        elif pago == suma_final:
            print("Muchas gracias por su compra")
            print("--------------------------------------------------")

def menu():
    opcion = 0
    salir = 5

    while opcion != salir:
        print("--------------------------------------------------")
        print("Menu principal")
        print("--------------------------------------------------")
        print("1.- Registrar producto de la compra")
        print("2.- Ver lista de productos registrados")
        print("3.- Ver subtotal")
        print("4.- Ingresar pago del cliente")
        print("5.- Finalizar")
        print("--------------------------------------------------")
        opcion = input("Seleccione la accion a efectuar: ")
        print("--------------------------------------------------")

        if opcion == "1":
            cajaregistradora.registrarproducto()
        elif opcion == "2":
            cajaregistradora.verlista()
        elif opcion == "3":
            cajaregistradora.subtotal()
        elif opcion == "4":
            cajaregistradora.pago()
        elif opcion == "5":
            print("Muchas gracias por su compra")
            break

menu()
"""