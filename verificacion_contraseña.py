#Ejercicio  - Verificar el largo de la contraseña
print("-------------------------------------------------------------")
print("Ejercicio 3 - Verificar el largo de la contraseña")
print("-------------------------------------------------------------")
password = input("Crea una nueva contraseña: ")
largo = len(password)
if largo < 8:
    print("Contraseña corta,debe tener 8 caracteres como mínimo, usted ingreso:",largo)
else:
    print("Contraseña creada con éxito")
