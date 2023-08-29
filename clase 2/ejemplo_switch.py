def case1():
    return "Opcion 1"

def case2():
    return "Opcion 2"

def case3():
    return "Opcion 3"

def default_case():
    return "Opcion no valida"

#crear un diccionario que mapee casos a funciones
switch_dict = {
    "opcion1": case1,
    "opcion2": case2,
    "opcion3": case3,
}

#definir una funcion que actue como el switch
def switch_example(case):
    return switch_dict.get(case, default_case())

opcion = "opcion1"
resultado = switch_example(opcion)
print(resultado)