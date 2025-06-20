# for x in range(1,11):
#     print(x)

# frutas = ["manzana", "pera", "banano", "tomate", "naranja"]
# for fruta in frutas:
#     print(fruta)
   
# usuario = int(input("Hola usuario favor ingresa un numero: "))
# for z in range(1, 11):
#     print(z)
# resultado = usuario * z
# print(f"{usuario} x {z} = {resultado}")

usuario = input("ingresa cualquier texto: ")
contador = 0
for letra in usuario:
    if letra == "a": 
        contador += 1
        print("contador: ", contador)


