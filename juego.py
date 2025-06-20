import random

def jugar_piedra_papel_tijera():
    print("bienvenido al juego piedra, papel o tijera!")
    while  True:

        opciones = ["piedra", "papel", "tijera"]
        opcion_usuario = input("elige piedra, papel o tijera: ").lower()

        opcion_computadora = random.choice(opciones)
        print(f"la computadora eligio: {opcion_computadora}")


        if opcion_usuario not in opciones:

            print("Opcion no valida, vuelve a elegir las opciones mencionadas")
            continue

        if opcion_usuario == opcion_computadora:
            print("Empate")

        elif (opcion_usuario == "piedra" and opcion_computadora == "tijera") or \
            (opcion_usuario == "tijera" and opcion_computadora == "papel") or \
            (opcion_usuario == "papel" and opcion_computadora == "piedra"):
            print("Ganaste!")
        else:
            print("Perdiste!")
    
        volver_a_jugar = input("(Te interesa volver a jugar)  (si/no)")
        if volver_a_jugar == "no":
            print("Gracias por jugar!")
            break
jugar_piedra_papel_tijera