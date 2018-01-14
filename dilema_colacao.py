

user_number = int(input("Dime un numero: "))

if user_number > 5:
    print("Tu numero es mayor que 5")
    print("Felicidades, jajaja")
else:
    print("Tu numero es menor")
    print("Toma un pin del Betis, campeon")



number_to_guess = 2
user_numberdos = int(input("Adivina el numero comprendido entre 1 y 10: "))
if number_to_guess == user_numberdos:
    print("Felicidades, has acertado")
else:
    print("Vaya, has fallado, intentalo de nuevo")