# 1) 

class Pila:
    
    items = []
    contador = 0
    
    def estaVacia(self):
        return self.items == []
    
    def incluir(self, item):
        self.items.append(item)
    
    def extraer(self):
        return self.items.pop()
    
    def inspeccionar(self):
        return self.items[-1]
    
    def tamano(self):
        return len(self.items)
    
# 2. 


    def darVuelta(self):
        auxiliar = []
        while not self.esVacia():
            elementos.append(self.extraer())
        for i in elementos:
            self.incluir(e)
    
p = Pila()
p.incluir(4)
p.incluir(2)
p.incluir(1)
assert p.inspeccionar() == 1
assert p.items == [4, 2, 1]
assert p.extraer() == 1
assert p.inspeccionar() == 2


# 3.

class Pila:
    
    def revertir(self, pila):
        separada = pila.split()
        nuevaFrase = separada[::-1]
        print(nuevaFrase)
        
p = Pila()
pila = "Tengo sueño"
p.revertir(pila)

# 4) 

class Pila:

    def contador(self,palabra):
    
        palabra = list(palabra)
        contadorUnos = []
        contadorCeros = []
        
        for i in palabra:
            if i == "0":
                contadorCeros.append(i)
            if i == "1":
                contadorUnos.append(i)
        return len(contadorCeros) == len(contadorUnos)

p = Pila()

assert p.contador("0011") == True
assert p.contador("0001") == False

# 5) 

class Pila:

    def balanceada(self, expresion):
        aux = []
        aux2 = []
        for i in expresion:
            if i == "(":
               aux.append(i)
            if i == ")":
                aux2.append(i)
        return len(aux) == len(aux2)

p = Pila()
assert p.balanceada("()()()") == True
assert p.balanceada("()()())") == False

# 6. 

class Pila: 
    
    def balanceada_general(self, expresion):
        pila = []
        diccionario = {'{': '}', '(': ')', '[': ']'}
        
        for i in expresion:
            if i in diccionario:
                pila.append(i)
            elif len(pila) == 0 or i != diccionario[pila.pop()]:
                return False
            
        return len(pila) == 0
        

p = Pila()
assert p.balanceada_general("()") == True
assert p.balanceada_general("[](()[)]") == False
assert p.balanceada_general("()[]") == True


# 7) 

def capicua(palabra):
    palabra = list(palabra)
    nuevaPila = []
    contador = -1
    
    for letra in range(len(palabra)):
        nuevaPila.append(palabra[contador])
        contador = contador - 1
        
        if len(palabra) == len(nuevaPila):
            nuevaPila = "".join(nuevaPila)
            palabra = "".join(palabra)
            nuevaPila = nuevaPila.lower()
            palabra = palabra.lower()
            
    if nuevaPila == palabra:
        print("La palabra", palabra, "es capicua")
        return True
    else:
        print("La palabra", palabra, "no es capicua")
        return False
    
palabra = input("Ingrese una palabra: ")
capicua(palabra)

assert capicua("Ala") == True
assert capicua("Osa") == False

# 8. 

class Pila2:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def incluir(self, item):
        self.items.insert(0,item)

    def extraer(self):
        self.items.pop(0)

    def inspeccionar(self):
        return self.items[0]

    def tamano(self):
        return len(self.items)