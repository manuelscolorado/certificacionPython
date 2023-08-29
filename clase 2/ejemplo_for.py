#iterar listas
""" frutas = ["manzana", "banana", 'cereza']

for fruta in frutas:
    print(fruta) """

#iterar cadenas
""" mi_cadena = "Hola, mundo!"

for caracter in mi_cadena:
    print(caracter) """

#iterar rango de numero
""" for numero in range(1, 6): #esto imprimirá del 1-5
    print(numero) """

#iterar diccionarios
mi_diccionario = {"a":1, "b":2, "c":3}

#iterar claves
""" for clave in mi_diccionario:
    print(clave) """

#iterar valores
"""for valor in mi_diccionario.values():
    print(valor) """

#iterar pares clave-valor
""" for clave, valor in mi_diccionario.items():
    print(clave, valor) """

#iterar sobre Enumerate
""" mi_lista = ['a', 'b', 'c']
for indice, valor in enumerate(mi_lista):
    print(f"Indice: {indice}, Valor: {valor}") """

nombres = ['juan', 'maria', 'carlos']
edades = [30, 25, 35]

for nombre, edad in zip(nombres, edades):
    print(f"Nombre: {nombre}, Edad: {edad}")