# Ejercicio 1

# Crear 2 variables enteras y mostrar la suma de ambas en pantalla

num1 = 0
num2 = 0

# Código
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
print("La suma de los dos números es: ", num1 + num2)

################################


# Ejercicio 2

# Dada una variable entera, sumarle 1 y mostrar el resultado en pantalla

num = 0

# Código
num = int(input("Introduce un número: "))
print("El número introducido es: ", num)
print("El número introducido más 1 es: ", num + 1)

################################

# 3- Ingresar una cadena por teclado, para luego mostrarla en pantalla
print(input("Ingrese su nombre:"))

# 4- Dado un valor que se ingresa por teclado, mostrar el 25% de ese valor en pantalla
print (int(input("Ingrese un numero: ")) * 0.25)

# 5- Ingresar por teclado un valor entero, para asignarlo a una variable llamada temperatura. Luego ingresar una cadena para
# asignarla a una variable llamada localidad. mostrar en pantalla la leyenda en la zona .... Tenemos una temperatura de ..... (usar
# los comodines %)
# 6- Dados los lados de un cuadrado, mostrar en pantalla el valor de su superficie
# 7- Copiar y ejecutar el siguiente código, justifique la salida que se obtiene por pantalla
# CONSIDERACIONES
# Leer el orientador de la clase y haber completado la Guía No1
# numero1,numero2=0,0
# numero1=int(input("Ingresar un numero : ")) numero2=int(input("Ingresar un numero : "))
# if numero1 > numero2:
# print(f"{numero1} es mayor a {numero2}")
# else:
# if numero2 > numero1:
# print(f"{numero2} es mayor a {numero1}") else:
# print(f"{numero2} es igual a {numero1}")
# 8- Implementar un algoritmo en Python que, dados dos valores de las acciones de la empresa Techint del día 23-8-2022 y otra del día 22-8-2022 permita informar si las acciones están el alza.
# 9- Tomando el mismo caso del ejercicio anterior, cambiar el código para ingresar por teclado el valor de dos acciones de días distintos. Tomando dicha información informar si conviene comprar, vender o no reacciona.
# 1
# 10- Nos contratan para hacer una segmentación de mercados, el equipo decido usar Python para implementar una solución. El relevamiento del problema describe que al tener el dato de la edad de una persona debe informar si se encuentra entre los 18 y los 36 años.
# 11- Un estudio contable, necesita automatizar un proceso de gran importancia. Se debe discriminar los cheques que tiene tienen un importe superior a los 100.000 pesos. Para ello, debemos realizar un programa que me permita ingresar el importe del cheque. Al terminar la carga, el sistema debe informar si el importe es mayor a 100.000
# 12- Crear un programa que dado un valor entero que se ingresa por teclado, informe si el 40% del valor ingresado se encuentra dentro del rango de 10 y 42.
# 13- Sea un país en el que solo se produce dulce de leche y pan de acuerdo con los siguientes datos:
# Dulce de leche Pan Precio Cantidad Precio
# Cantidad
#              2020 21 20 10 10 2021 20 22 9 12 2022 22 21 10 11
# SE pide calcular:
# a- El PIB, para cada año tomando 2021 como año base b- Informar cual es el año con mayor valor de PIB
# Considerar
# El PIB de un año se calcula como las producciones del año valoradas a precios del año:
# PIB(2020) = 21+ 20 + 10 * 10 = El resultado debería ser 520 PIB(2021) = 20*22+ 9*12=548
# PIB(2022) = 22* 21+10*11=572





# Ejercicio 5

temperatura = 0
localidad = ""

# Código
temperatura = int(input("Introduce la temperatura: "))
localidad = input("Introduce la localidad: ")
print("La temperatura en la localidad de %s es de %d grados" % (localidad, temperatura))

# Ejercicio 6

lado1 = 0
lado2 = 0

# Código

lado1 = int(input("Introduce el primer lado: "))
lado2 = int(input("Introduce el segundo lado: "))
print("La superficie del cuadrado es: ", lado1 * lado2)

# Ejercicio 8

# Implementar un algoritmo en Python que, dados dos valores de las acciones de la empresa Techint del día 23-8-2022 y otra del día 22-8-2022 permita informar si las acciones están el alza.

valor1 = 0
valor2 = 0

# Código

valor1 = int(input("Introduce el valor de las acciones del día 23-8-2022: "))
valor2 = int(input("Introduce el valor de las acciones del día 22-8-2022: "))
if valor1 > valor2:
    print("Las acciones están en alza")
else:
    print("Las acciones no están en alza")

################################

# Ejercicio 9

# Tomando el mismo caso del ejercicio anterior, cambiar el código para ingresar por teclado el valor de dos acciones de días distintos. Tomando dicha información informar si conviene comprar, vender o no reacciona.

valor1 = 0
valor2 = 0

# Código

valor1 = int(input("Introduce el valor de las acciones del día 23-8-2022: "))
valor2 = int(input("Introduce el valor de las acciones del día 22-8-2022: "))
if valor1 > valor2:
    print("Las acciones están en alza")
    print("Convendría comprar")
elif valor1 < valor2:
    print("Las acciones no están en alza")
    print("Convendría vender")
else:
    print("Las acciones no reaccionan")
    
################################
    
# Ejercicio 10

#  Informar si dada una edad, la persona se encuentra entre los 18 ylos 36 años.

edad = 0

# Código

edad = int(input("Introduce la edad: "))
if edad >= 18 and edad <= 36:
    print("La persona se encuentra entre los 18 y los 36 años")
else:
    print("La persona no se encuentra entre los 18 y los 36 años")

################################


# 11- Un estudio contable, necesita automatizar un proceso de gran importancia. Se debe discriminar los cheques que tiene tienen un importe superior a los 100.000 pesos. Para ello, debemos realizar un programa que me permita ingresar el importe del cheque. Al terminar la carga, el sistema debe informar si el importe es mayor a 100.000
cheque = float(input("ingrese el importe del cheque"))
if cheque > 100000:
    print("el importe es mayor a 100.000")
else:
    print("el importe es inferior a 100.000")

    
# Ejercicio 12

# - Crear un programa que dado un valor entero que se ingresa por teclado, informe si el 40% del valor ingresado se encuentra dentro del rango de 10 y 42.

valor = 0

# Código

valor = int(input("Introduce un valor: "))
if valor * 0.4 >= 10 and valor * 0.4 <= 42:
    print("El 40% del valor ingresado se encuentra dentro del rango de 10 y 42")
else:
    print("El 40% del valor ingresado no se encuentra dentro del rango de 10 y 42")

################################
