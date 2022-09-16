print("Bienvenido a mi trivia sobre computación")
print("Pondremos a prueba tus conocimientos")

nombre = input("Ingresa tu nombre: ")

print(
    "Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:"
)

print("1) ¿Quién fue el creador de windows?")
print("a) Linus Torvalds")
print("b) Bill Gates")
print("c) Mark Zuckerberg")
print("d) Dennis Ritchie")

respuesta_1 = input("Tu respuesta: ")
if respuesta_1 == "b":
    print("respuesta correcta")
else:
    print("fallaste")

print("2) ¿quien fue el creador de python?")

print("a)Jhon backus")
print("b)Ada lovelace")
print("c)Short range")
print("d)Guido van rossum")

respuesta_2 = input("\nTu respuesta: ")
if respuesta_2 == "d":
    print("respuesta correcta")
else:
    print("fallaste")

print("3) ¿quien fue el precursor de la creacion de gnu Linux?")
print("a)Linus torvalds")
print("b)Ghido van rossum")
print("c)Kim dotcom")
print("d)Jean salas")

respuesta_3 = input("\nTu respuesta: ")
if respuesta_3 == "a":
    print("respuesta correcta")
else:
    print("fallaste")
print(
    "4) ¿que lenguaje de programacion fue el precursor de la mayoria de los lenguajes de programacion?"
)
print("a)Fortran")
print("b)Lisp")
print("c)Cobol")
print("d)Todas las anteriores")

respuesta_4 = input("\nTu respuesta: ")
if respuesta_4 == "d":
    print("respuesta correcta")
else:
    print("fallaste")
print("5) ¿con que lenguaje de programacion se hizo Netflix?")
print("a)Java script")
print("b)Java")
print("c)Python")
print("d)Pascal")

respuesta_5 = input("\nTu respuesta: ")
if respuesta_5 == "c":
    print("respuesta correcta")
else:
    print("fallaste")

#en la siguiente sesion agregaremos mas funcionalidades y trabajaremos las preguntas con funciones
#don´t repeat yourself
