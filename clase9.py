# text = "hola mundo"

# iterador = iter(text)

# for itera in iterador:
#     print(itera)



# colores = ("amarillo", "azul", "rojo")

# iterador = iter(colores)
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))

#Diccionario

informacion = {
    "Nombre" : "Jose",
    "Apellido" : "Mendoza-Puentes",
    "Nacimiento" : "21-01-08",
    "Ciudad-Pais" : "caracas-peru"
}

iterador = iter(informacion.items())

for clave, valor in iterador:
    print(f"{clave}: {valor}")