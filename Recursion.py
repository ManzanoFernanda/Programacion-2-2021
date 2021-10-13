#Guía de recursion Manzano Fernanda
#1
def sumatoria(n:int)->int:
    if n == 0:
        return 0
    else:
        return n + sumatoria(n-1)
print(sumatoria(3))

#2
def factorial(n:int)-> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

#3
def product(l:list)->int:
    if l == []:
        return 1
    else:
        return l[0] * product(l[1:])

print(product([5,2,6,8,3]))

#4
def length(l:list)->int:
    if l == []:
        return 0
    else:
        return 1 + length(l[:1])
    
#5
def reverse(l:list)->list:
    if l == []:
        return l
    else:
        return [l[-1]] + reverse(l[:-1])
    
print(reverse([5,2,6,8,3]))

#6
"""
drop(x:int,y:list)->list:
    if y == []:
        return x
    elif n == 0:
        return l
    else:
        
drop(3, [5,2,6,8,3])
"""
#7
global fibo
fibo = [0 for i in range(10)]
def fib(n:int)->int:
    if n <= 1:
        return 1
    elif fibo[n] != 0:
        return fibo[n]
    else:
        fibo[n] = fib(n-1) + fib(n-2)
    return fibo[n]

print(fib(2))

#8
global forma
forma = [0 for i in range(10)]
def formas(n:int)->int:
    if n == 1:
        return n
    if n == 2:
        return 2
    else:
        forma[n] = formas(n-1) + formas(n-2)
    return forma[n]

print(formas(5))

#9
"""
def par(x:int)-> bool:
    if x == 0:
        return True
    elif x / 2 == 0:
        return True
    else x / 2 != 0:
        return False
par(7)
"""