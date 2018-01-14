input("Bienvenido al combate. Vas a manejar a Pikachu. Pulsa intro.")
pokemon_elegido = input("¿Contra qué Pokemon quieres combatir? Puedes elegir entre Squirtle, Charmander y Bulbasaur: ")

vida_pikachu  = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon= 8

elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasaur"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    # Este es el código del combate en sí.
    ataque_elegido = input("¿Qué ataque vamos a usar? Chispazo/Bola voltio: ")
    if ataque_elegido == "Chispazo":
        print("Efectúas un ataque de 10 de daño")
        vida_enemigo -= 10
    elif ataque_elegido == "Bola voltio":
        print("Efectúas un ataque de 12 de daño")
        vida_enemigo -= 12
    else:
        print("Vaya, te has equivocado al seleccionar el ataque")

    print("La vida de {} ahora es de {}HP".format(nombre_pokemon, vida_enemigo))

    print("{} te hace un ataque de {} de daño".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon
    print("La vida de tu Pikachu ahora es de {}HP".format(vida_pikachu))

if vida_enemigo <= 0:
     print("¡Has ganado!")
if vida_pikachu <= 0:
    print("¡Has perdido!")

print("El combate ha terminado")