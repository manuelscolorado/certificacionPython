#Basica
edad = 28
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Multiple condicion
autoestima_hoy = 100
if autoestima_hoy >= 90:
    print("Hoy estas muy animado")
elif autoestima_hoy >= 80:
    print("Hoy no estas tan bien pero tampoco tan mal")
elif autoestima_hoy >= 70:
    print("Hoy no estas tan bien")
else:
    print("Hoy estas fatal")

#Una sola linea
edad = 20
mensaje = "Eres mayor de edad" if edad >= 18 else "No eres mayor de edad"
print(mensaje)