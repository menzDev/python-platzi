# informacion = {"nombre": "Jose Tomas",
#                 "Apellido": "Mendoza Puentes",
#                 "Apodos": "che",
#                 "Altura": 1.71,
#                 "Edad": 17}
# print(informacion)

# claves = informacion.keys()
# print(claves)

# valores = informacion.values()
# print(valores)

datos = {"Jose Tomas":{"Apellido": "Mendoza Puentes",
                "Apodos": "che",
                "Altura": 1.71,
                "Edad": 17,
                "Nacimiento": "Enero-21-2008",
                "Ciudad": "Medellin",
                "Barrio": "Nuevo-Occidente",
                "Pais-Ciudad": "Venezuela-Maracaibo"},
                #------
       "Yolamis":{"Apellido": "Puentes Chiquinquira",
                "Apodos": "Yola",
                "Altura": 1.62,
                "Edad": 43,
                "Nacimiento": "Julio-31-1981",
                "Ciudad-Residiente": "Medellin",
                "Barrio": "Nuevo-Occidente",
                "Nacimiento-Pais-Ciudad": "Venezuela-Maracaibo"}
                            }
print(datos["Jose Tomas"])
print(datos["Yolamis"])