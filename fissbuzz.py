"""Programa que imprime Fizz si un numero es multiplo de 3,
imprime Buzz si es Multiplo de 5 y fizzbuzz si es multiplo de 3 y 5"""

#pseudocodigo:
#iniciar una variable llamada "a" en 1
#while mientras que a sea menor a 101:
#dividir el numero por 5 y 3 si es TRUE imprimir fizzbuzz
#si es divisible por 5 y da 0 imprimir BUZZ
#si es divisible por 3 y da 0 imprimir FIZZ
#despues del if a la variable "a" sumarle 1 

a = 1
while a < 101:
    if a % 5 == 0 and a % 3 == 0:
        print "fizzbuzz"
    elif a % 5 == 0:
        print "buzz"
    elif a % 3 == 0:
        print "fizz"
    else:
        print a
    a = a +1
