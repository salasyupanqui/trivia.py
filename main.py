import random
import time

puntaje = random.randint(0, 10)
# colores
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

puntaje = 0
iniciar_trivia = True
intentos = 0

print(BLUE + "Bienvenido a mi trivia sobre computación")
print("Pondremos a prueba tus conocimientos")
print("\ntienes", puntaje, "puntos\n")

nombre = input(GREEN + "\n Ingresa tu nombre: \n ")

print(
    BLUE, "\n Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n",
    RESET)
#tiempo-muerto
print(".....................3")
print(".....................2")
print(".....................1")
time.sleep(0.8)

print(YELLOW + "1) ¿Quién fue el creador de windows?")
print("a) Linus Torvalds")
print("b) Bill Gates")
print("c) Mark Zuckerberg")
print("d) Dennis Ritchie")

respuesta_1 = input(CYAN + "Tu respuesta: ")
while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_1 == "b":
    puntaje += 10
    print("respuesta correcta tienes:", nombre, "!")
    print("llevas", puntaje, "puntos")
else:
    print("fallaste")
    puntaje_menor = str(-5)
    print("ahora tienes: " + puntaje_menor + "puntos")
    print("intenta la siguiente ronda")
print("Cargando...\n")
time.sleep(1)

print(YELLOW + "2) ¿quien fue el creador de python?")

print("a)Jhon backus")
print("b)Ada lovelace")
print("c)Short range")
print("d)Guido van rossum")

respuesta_2 = input(CYAN + "\nTu respuesta: ")
while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_2 == "d":
    print("respuesta correcta")
else:
    print("fallaste")
    puntaje_menor = str(-5)
    print("ahora tienes: " + puntaje_menor + "puntos")
    print("Next")

time.sleep(1)

print(YELLOW + "3) ¿quien fue el precursor de la creacion de gnu Linux?")
print("a)Linus torvalds")
print("b)Ghido van rossum")
print("c)Kim dotcom")
print("d)Jean salas")

respuesta_3 = input(CYAN + "\nTu respuesta: ")
while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_3 == "a":
    print("respuesta correcta")
else:
    print("fallaste")
    puntaje_menor = str(-5)
    print("ahora tienes: " + puntaje_menor + "puntos")
    print("bueno a la otra sera")
time.sleep(1)
print(
    YELLOW +
    "4) ¿que lenguaje de programacion fue el precursor de la mayoria de los lenguajes de programacion?"
)
print("a)Fortran")
print("b)Lisp")
print("c)Cobol")
print("d)Todas las anteriores")

respuesta_4 = input(CYAN + "\nTu respuesta: ")
while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_4 == "d":
    print("respuesta correcta")
else:
    print("fallaste")
    puntaje_menor = str(-5)
    print("ahora tienes: " + puntaje_menor + "puntos")
    print("intenta la siguiente ronda")
time.sleep(1)
print(YELLOW + "5) ¿con que lenguaje de programacion se hizo Netflix?")
print("a)Java script")
print("b)Java")
print("c)Python")
print("d)Pascal")

respuesta_5 = input(CYAN + "\nTu respuesta: ")
while respuesta_5 not in ("a", "b", "c", "d"):
    respuesta_5 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_5 == "c":
    print("respuesta correcta")
else:
    print("fallaste")

if respuesta_5 == "c":
    print("ganaste eres un genio")
    fila = int(6)
    y = 0
    while y >= fila:
        z = 0
        while z < y:
            print("+", end="")
        print("")
        y = y + 1

else:
    print("confie en ti y asi me fallaste")
    print("vuelve a intentar")
    puntaje_menor = str(-5)
    print("ahora tienes: " + puntaje_menor + "puntos")
    print("Sera para el otro año")


def a():
    volver = input("introduce si quieres volveer: ")
    while volver == "si" or volver == "s":
        volver = 1
        print(
            "intente que el codigo sea un bucle pero no pude lo siento chicos "
        )
        print("Me encantaria que me echasen una mano")
        print("gracias")

        a()


a()