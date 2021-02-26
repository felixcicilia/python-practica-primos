#el comienzo en python

#print ("hello fucking world")

#PRACTICA 1 DETERMINAR SI UN NUMERO ES PAR O IMPAR

#numero = int(input("Ingresa un numero : "))
#if numero % 2 == 0:
#    print("el numero es par")
#    exit(0)
#print("el numero es impar")

#PRACTICA 2 - determina si un numero es primo: 

#numero = int(input("ingresa el numero primo : "))
# if numero % 1 == 0 and numero % numero == 0:
#     print("el numero es primo")
#     exit(0)
# print("el numero no es primo")

#PRACTICA 3 - determina si un numero es primo: con "FOR"

#for numero_en_la_lista in range(2, numero - 1 ):
#    if numero % numero_en_la_lista == 0:
#        print('no es primo')
#        exit(0)
#print('es primo')


#PRACTICA 4 - determina si un numero es primo: con "WHILE"

m = int(2);
band = "V";

numero = int(input("ingresa el numero primo : "))

while ((band == "V") and (m < numero)):
        if((numero % m) == 0):
            band = "F";
        else:
            m = m + 1;
if (band == "V"):
        print("el numero es primo")
else:
        print("el numero no es primo")