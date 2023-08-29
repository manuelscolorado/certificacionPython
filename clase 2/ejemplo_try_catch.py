try:
    resultado = 10 / "hola"
except Exception as e:
    print("Error:", e)
else:
    print("la division fue exitosa")
finally:
    print("Finalizado")