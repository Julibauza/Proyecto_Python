# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
# de cada letra en la cadena. Los espacios no deben ser considerados

Cadena = "La bicicleta tiene dos ruedas"
Diccionario_frecuencias = {}

def contar_letras (texto):
    texto = texto.lower() 
    for letra in texto:
        if letra == " " : 
            pass
        else: 
            if letra in Diccionario_frecuencias:
               Diccionario_frecuencias[letra] += 1
            else: 
                Diccionario_frecuencias [letra] = 1
    
    return Diccionario_frecuencias

print(contar_letras(Cadena))



# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

Puntaje = [102, 89, 90, 121, 45]

Duplicar_valores = list(map(lambda num: num *2, Puntaje))

print (f"El doble de cada valor de la lista es: {Duplicar_valores}") 

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

muebles = ["escritorio", "armario", "mesa", "silla"]


def palabra_contenida (milista, objetivo):
    resultados = []
    for palabra in milista:
        if objetivo in palabra:
            resultados.append(palabra)

    return resultados    

print (palabra_contenida (muebles, "rio"))
            


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

Primera_puntuacion = [100, 120, 111, 95, 60]
Segunda_puntuacion = [80, 84, 105, 70, 65]

Diferencia_valores = list(map(lambda a, b: a - b, Primera_puntuacion, Segunda_puntuacion))

print (f"La diferencia entre los valores de las listas son: {Diferencia_valores}")

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

Lista_notas = [4, 7, 9, 6.2, 10, 7.6]

def calcular_media (lista_num, nota_aprobado=5):
    suma_notas = 0
    for numero in lista_num:
        suma_notas += numero 
    media = round(suma_notas / len(lista_num), 2)
    
    if media >= nota_aprobado:
       return(media, "aprobado")  
    else:
       return(media, "suspenso")
     
print(f"La media de la lista de notas es: {calcular_media(Lista_notas)}")


# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def calcular_factorial (numero):
    if numero != 0:
        return numero * calcular_factorial (numero - 1)
    else:
        return 1
    
print (calcular_factorial(8))

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

Lista_tuplas = [("lapiz", "papel", "boligrafo"),
                ("movil", "tablet", "ordenador"),
                ("carpeta", "cuaderno") ]

Tuplas_a_strings = list(map(lambda tup: ",".join(tup), Lista_tuplas))

print (Tuplas_a_strings)


# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta
#dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.


try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    print (f"El primer número ingresado es: {numero1}, y el segundo es: {numero2}")
    
    resultado = numero1 / numero2

except ValueError:
    print(f"Por favor ingrese un número válido")

except ZeroDivisionError:
    print (f"No se puede dividir entre 0")

else: 
    print(f"La división fue exitosa! El resultado es: {round(resultado,2)}")



# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo 
# ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
# Usa la función filter()

mascotas = ["Perro", "Mapache", "Serpiente_Piton", "Gato", "Oso", "Conejo", "Cocodrilo", "Tigre"]
prohibidas = ["Mapache", "Tigre","Serpiente_Piton", "Cocodrilo", "Oso"]

def filtrar_mascotas (animal):
    def permitidas (animal):
        return animal not in prohibidas

    return list(filter(permitidas, animal)) 

mascotas_permitidas = filtrar_mascotas(mascotas)
print(f"Las mascotas permitidas en España son: {mascotas_permitidas}")

#10 . Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
#excepción personalizada y maneja el error adecuadamente.

numeros = [1, 5, 4, 8, 9, 13, 23, 14]
lista_2= []

def promedio(lista_numeros):
     if len(lista_numeros) == 0:
        return "La lista está vacía"
     suma_numeros = 0
     for numero in lista_numeros:
        suma_numeros += numero
     media = suma_numeros / len (lista_numeros)
     return (f"El promedio de la lista es: {media}")

print(promedio(numeros))
print(promedio(lista_2))

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango 
# esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.

try: 
    edad = int(input("Ingrese su edad: "))

except ValueError:
    print("Por favor ingrese un número válido")   
    
else: 

    if edad < 0 or edad > 120:
        print("Edad fuera del rango válido")
    else: 
        print(f"Su edad es: {edad}")



#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

Frase = "No voy en tren, voy en avión"

Lista_long_palabras = (list(map(lambda palabra: len(palabra), Frase.split())))

print (Lista_long_palabras)


#13 . Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
#  Las letras no pueden estar repetidas .Usa la función map()

set_letras = {"A", "H", "m", "v", "L", "y"}

Lista_de_tuplas = list(map(lambda letra:(letra.upper(), letra.lower()), set_letras))

print(Lista_de_tuplas)



#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter ()

Condimentos = ["Sal", "Pimienta", "Pimenton", "Oregano", "Tomillo"]

def empieza_P (condimento): 
    return condimento[0].upper() == "P"

print (f"Las palabras de la lista que empiezan con P son: {(list(filter(empieza_P, Condimentos)))}")

#15. Crea una función lambda que sume 3 a cada número de una lista dada

numeros = [1, 5, 4, 8, 9, 13, 23, 14]

Sumar_3 = list(map(lambda num: num + 3, numeros))

print (Sumar_3)


#16 . Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras
#  que sean más largas que n. Usa la función filter()

Texto = "La sal no sala y el azúcar no endulza"
n = 4

def longitud_palabras (texto, n):
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


print(f"Las palabras del texto con más de {n} letras son: {(longitud_palabras(Texto, n))}")


# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 
# quinientos setenta y dos 572. Usa la función reduce()

from functools import reduce

digitos = [1, 9, 9, 3, 5]

Unir_digitos = int(reduce(lambda num1, num2: str(num1)+str(num2), digitos))

print(f"Los digitos de la lista corresponden al número: {Unir_digitos}")


  
# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) 
# y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

info_estudiantes = [
    {"nombre": "Juan", "edad": 22, "calificacion": 60  },
    {"nombre": "Lucia", "edad": 24, "calificacion": 80  },
    {"nombre": "Pedro", "edad": 27, "calificacion": 95  },
    {"nombre": "Jana", "edad": 25, "calificacion": 90  }
    ]

print(list(filter(lambda estudiante: estudiante ["calificacion"]>= 90, info_estudiantes)))


# 19. Crea una función lambda que filtre los números impares de una lista dada.

lista_numeros = [1, 5, 4, 8, 9, 13, 23, 14]

print(f"Los numeros impares de la lista son: {(list(filter(lambda num: num %2 != 0, lista_numeros)))}")


# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

lista = [8, "Mesa", 45, "Silla", "Cocina", 11]

print(list(filter(lambda elemento: type(elemento) == int, lista)))

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda ()

calcular_cubo = lambda num: num ** 3

print (calcular_cubo(3))


# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()

from functools import reduce

numeros = [1,2,3,4]

def multiplicar (num1, num2):
    return num1 * num2

print (reduce(multiplicar, numeros))

print(reduce (lambda num1, num2: num1 * num2, numeros))


# 23. Concatena una lista de palabras.Usa la función reduce()

palabras = ["Una", "frase", "de", "palabras", "unidas"]

Formar_frase = reduce(lambda palabra1, palabra2: palabra1 + " " + palabra2, palabras)

print(f"El resultado de concatenar las palabras de mi lista es: {Formar_frase}")


# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() 

gastos = [10, 210, 45, 120, 50, 25]

Diferencia_gastos = reduce(lambda num1, num2: num1 - num2, gastos)

print (f"La diferencia total de los valores es: {Diferencia_gastos}")


# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

cadena_de_texto = "Azul y amarillo forman verde"

def contar_caracteres (cadena):
    return len (cadena.replace(" ", ""))

print (f"Los caracteres de la cadena de texto, sin contar espacios, son: {contar_caracteres(cadena_de_texto)}")



# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.


Calcular_resto = lambda num1, num2: num1 % num2

print(Calcular_resto(10, 3))

# 27. Crea una función que calcule el promedio de una lista de números.

Lista_A = [10, 14, 8, 17, 23, 2]

def calcular_promedio(lista):
     suma_numeros = 0
     for numero in lista:
        suma_numeros += numero
     media = suma_numeros / len (lista)
     return (f"El promedio de la lista es: {media}")


print(calcular_promedio (Lista_A))

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

herramientas = ["tornillo", "tuerca", "llave", "tornillo", "pinza", "tuerca"]

def primer_duplicado (lista):
    for palabra in lista:
        if lista.count(palabra) > 1: 
            return palabra

print(primer_duplicado(herramientas))



# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

texto = "ventana"

def enmascarar (variable): 
    texto = str (variable)
    return "#" * (len(texto) - 4) + texto[-4:]

print(enmascarar(texto))
        


# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.


def anagrama (palabra1, palabra2):
    original1 = palabra1
    original2 = palabra2
    
    palabra1=list(palabra1.lower())
    palabra2=list(palabra2.lower())
    
    palabra1.sort()
    palabra2.sort()
    
    if palabra1 == palabra2:
       return(f"Las palabras {original1} y {original2} son anagramas")
    else: 
        return("Las palabras indicadas no son anagramas")


print(anagrama("Roma", "amor"))


# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. 
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
 
def lista_nombres ():
  lista = input("Ingrese una lista de nombres separados por comas: ")
  nombre = input("Ingrese el nombre que desea buscar: ")
  
  lista = [n.strip() for n in lista.split(",")]

  if nombre in lista:
        print(f"El nombre {nombre} ha sido encontrado en su lista")
  else: 
    raise Exception (f"El nombre {nombre} no ha sido encontrado en la lista")


print(lista_nombres())


# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del 
# empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

empleado1 = "Juan Perez"
empleado2 = "Juan Gonzalez"
lista_empleados = ["Francisca Gonzalez", "Jose Luis Rodriguez", "Juan Perez", "Lourdes Gomez"]


def puesto_empleado (nombre, lista):
    for i, n in enumerate(lista):
        if n == nombre:
           return(f"El puesto de {nombre} en la lista es: {i} ")
 
    return(f"{nombre} no trabaja aquí")
    

print(puesto_empleado(empleado1, lista_empleados))
print(puesto_empleado(empleado2, lista_empleados))


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

Notas_1 = [60, 45, 74, 89, 98]
Notas_2 = [50, 41, 25, 58, 88]

Sumar_listas = list(map(lambda a, b: a + b, Notas_1, Notas_2))

print(f"La suma de los elementos correspondientes de las listas son: {(Sumar_listas)}") 


# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
       #Código a seguir:
       #1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
       #2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
       #3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
       #4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
       #5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
       #6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
   #Caso de uso:
     #1. Crear un árbol.
     #2. Hacer crecer el tronco del árbol una unidad.
     #3. Añadir una nueva rama al árbol.
     #4. Hacer crecer todas las ramas del árbol una unidad.
     #5. Añadir dos nuevas ramas al árbol.
     #6. Retirar la rama situada en la posición 2.
     #7. Obtener información sobre el árbol.   




class Arbol:
    def __init__ (self):

        self.tronco = 1
        self.ramas = []

    
    def crecer_tronco(self):
        self.tronco = self.tronco + 1
         
    def nueva_rama (self):
        self.ramas.append(1)  
    
    def crecer_ramas (self):
        for i, rama in enumerate(self.ramas):
            self.ramas[i] = self.ramas[i] + 1

    def quitar_rama (self, pos):
        self.ramas.pop(pos)

    def info_arbol (self):
        return (f"La longitud del tronco es {self.tronco}, tiene {len(self.ramas)} rama/s y las longitudes de las ramas son: {self.ramas}")
        


arbol1 = Arbol()
arbol1.crecer_tronco()
arbol1.nueva_rama()
arbol1.crecer_ramas()
arbol1.nueva_rama()
arbol1.nueva_rama()
arbol1.quitar_rama(2)
print(arbol1.info_arbol())



# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta 
#corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
#agregar dinero al saldo.
   #Código a seguir:
      #1.Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante el método True y False .
      #2.Implementar retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
      #3.Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
    #Lanzará un error en caso de no poder hacerse.
      #4.Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
 #Caso de uso:
#1.Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#2.Agregar 20 unidades de saldo de "Bob".
#3.Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#4.Retirar 50 unidades de saldo a "Alicia".

class Usuario_banco:
    def __init__(self, nombre, saldo, cuenta_corriente):
          self.nombre = nombre
          self.saldo = saldo
          self.cuenta_corriente = cuenta_corriente

    def retirar_dinero (self, monto_retirar):
        if self.cuenta_corriente: 
           if monto_retirar > self.saldo: 
               return "El monto ingresado excede el saldo disponible"
           elif 0 < monto_retirar <= self.saldo:
               self.saldo -= monto_retirar
               return "Retiro realizado con éxito"
           else: 
               return "Ingrese un monto válido"
        else: 
            return(f"El usuario {self.nombre} no tiene cuenta corriente en el Banco")
        
    def transferir_dinero (self, otro_usuario, monto_transferir):
        if self.cuenta_corriente and otro_usuario.cuenta_corriente:
            if monto_transferir <= 0:
                return "El monto a transferir debe ser mayor a 0"
            elif monto_transferir > otro_usuario.saldo:
                return "El saldo de la cuenta de origen no es suficiente"
            elif monto_transferir <= otro_usuario.saldo:
                otro_usuario.saldo -= monto_transferir
                self.saldo += monto_transferir
                return "Transferencia realizada con éxito"
        else: 
            return "El/los usuario/s no tiene/n cuenta corriente en el Banco"    

    def agregar_dinero (self, monto_agregar):
        if self.cuenta_corriente:
           if monto_agregar > 0:
              self.saldo += monto_agregar
              return "Operación realizada con éxito"
           else: 
              return "El monto ingresado no es válido"
        else: 
            return(f"El usuario {self.nombre} no tiene cuenta corriente en el Banco")
        

alicia = Usuario_banco("Alicia", 100, True)
bob = Usuario_banco("Bob", 50, True)

print(bob.agregar_dinero(20))
print(alicia.transferir_dinero(bob, 80))
print(alicia.retirar_dinero(50))

print(f"Saldo Alicia: {alicia.saldo}")
print(f"Saldo Bob: {bob.saldo}")


# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , 
#contar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir 
# primero y llamar dentro de la función procesar_texto
   #Código a seguir:
      #1. Crear una función contar_palabras para contar el número de veces que 
      # aparece cada palabra en el texto. Tiene que devolver un diccionario.
      #2.Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva .
         #Tieneque devolver el texto con el remplazo de palabras.
      #3.Crear una función eliminar_palabra para eliminar una palabra del texto. 
          # Tiene que devolver el texto con la palabra eliminada.
      #4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un 
          # número de argumentos variable según la opción indicada.
   #Caso de uso:
#Comprueba el funcionamiento completo de la función procesar_texto

from collections import Counter
import string

cadena = "En casa de herrero, cuchillo de palo"

def contar_palabras(texto):
    texto = texto.lower() 
    
    for p in string.punctuation:
        texto = texto.replace(p, "") 
    
    palabras = texto.split()     

    return dict(Counter(palabras))



def reemplazar_palabra (texto_original, palabra_anterior, palabra_nueva):
    texto_nuevo = texto_original.replace(palabra_anterior, palabra_nueva)
    return texto_nuevo



def eliminar_palabra (texto_original, palabra_a_borrar):
    texto_original = texto_original.lower()

    for p in string.punctuation:
        texto_original = texto_original.replace(p, "")

    palabras = texto_original.split()    
    palabras.remove(palabra_a_borrar.lower())
    return " ".join(palabras)

def procesar_texto (texto, opcion, *args):
    if opcion == "contar":
       return contar_palabras (texto)
    elif opcion == "reemplazar":
        return reemplazar_palabra (texto, args[0], args [1])
    elif opcion == "eliminar":
        return eliminar_palabra (texto, args[0])
    else: 
        return"Opción no válida"
   


print(procesar_texto(cadena, "contar"))
print(procesar_texto(cadena, "reemplazar", "palo", "madera"))
print(procesar_texto(cadena, "eliminar", "herrero"))


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

hora = input("Por favor ingrese la hora actual (HH:MM)")
partes = hora.split(":")

if len(partes) == 2: 

    h = int(partes[0])
    m = int(partes[1])

    if 0 <= h <= 23 and 0 <= m <= 59:
      if 0 <= h < 6:
       print ("Es de noche")
      elif 6 <= h < 17:
       print ("Es de día")
      else: 
       print ("Es la tarde")
    else: 
        print("Hora o minutos fuera de rango")
else: 
    print("Formato incorrecto")

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
#Las reglas de calificación son:
# 0  69 insuficiente
# 70  79 bien
# 80  89 muy bien
# 90  100 excelente

nombre1 = "Jose"
Nota1 = 87

nombre2 = "Maria"
nota2 = 70

nombre3 = "Francisco"
nota3 = 45


def calificacion_texto (nota):
    if 0 <= nota <= 69:
       return "INSUFICIENTE"
    elif 70 <= nota <=79: 
        return "BIEN" 
    elif 80 <= nota <= 89: 
        return "MUY BIEN"
    elif 90 <= nota <= 100:
        return "EXCELENTE"
    else: 
        return "Nota inválida"
        

print (f"La nota de {nombre1} es: {calificacion_texto(Nota1)}")     
print (f"La nota de {nombre2} es: {calificacion_texto(nota2)}") 
print (f"La nota de {nombre3} es: {calificacion_texto(nota3)}")  


# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", 
# "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura)

import math

forma1 = "rectangulo"
datos1 = (5, 3)

forma2 = "triangulo"
datos2 = (6, 2)

forma3 = "circulo"
datos3 = (3,)


def calcular_area (figura, datos):
    if figura == "rectangulo":
        area = round(datos [0] * datos[1],2)
    elif figura == "triangulo":
        area = round((datos[0] * datos[1]) / 2,2)
    elif figura == "circulo":
        area = round(math.pi * (datos[0] ** 2),2)
    else: 
        return "Figura no reconocida"
   
    return(f"El area del {figura} es: {area} cm²")

print(calcular_area(forma1, datos1))
print(calcular_area(forma2, datos2))
print(calcular_area(forma3, datos3))


#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
#monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
   #1. Solicita al usuario que ingrese el precio original de un artículo.
   #2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
   #3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
   #4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido 
      # (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
   #5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
   #6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python


precio_original = int(input("Por favor ingrese el precio original del articulo"))
cupon_descuento = input("¿Tiene cupón de descuento? Responda si o no").lower()

if cupon_descuento == "si":
    valor_cupon = int(input("Ingrese el valor del cupón"))
    if 0 < valor_cupon <= precio_original: 
        precio_final = precio_original - valor_cupon
        print(f"El precio final del articulo con el descuento aplicado es: {precio_final}€")
    
    elif valor_cupon > precio_original:
        precio_final = 0
        resto_cupon = valor_cupon - precio_original
        print(f"El precio final del articulo es: {precio_final}€, y en su cupón de descuento aún tiene: {resto_cupon}€")

    else:
        print("El valor ingresado es incorrecto")

else: 
    print(f"El precio final del articulo es: {precio_original}€")        






