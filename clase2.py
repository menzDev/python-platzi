# Online Python - IDE, Editor, Compiler, Interpreter

x = 10
y = 2.54
z = 2.3E4
a = 2.3E-4
print(type(x))
print(type(y))
print(z)
print(a)

#Uso de sep
print("Nunca", "pares", "de", "aprender", sep=",")

#Uso de end
print("Nunca", end=" ")
print("pares de aprender")

#impresion en variables
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

#Uso de formato con f-strings
frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}")

#Impresión con formato específico
valor = 3.14159
print("Valor: {:.2f}".format(valor))

#Saltos de línea y caracteres especiales
print("Hola\nmundo")
print('Hola soy \'Carli\'')
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")