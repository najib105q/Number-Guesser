import random

to_guess = random.randint(0, 99)
tries = 0

print("Willkommen beim Zahlenratespiel!")
print("Ich habe mir eine Zahl zwischen 0 und 99 ausgedacht.")

while True:
    try:
        user_input = int(input("Bitte Zahl zwischen 0 und 99 eingeben: "))
        
        if not (0 <= user_input <= 99) or not isinstance(user_input, int):
            print("Fehler: Bitte eine ganze Zahl zwischen 0 und 99 eingeben")
            continue
        
        tries += 1
            
        if user_input < to_guess:
            print("Die zu erratende Zahl ist groesser!")
        elif user_input > to_guess:
            print("Die zu erratende Zahl ist kleiner!")
        elif user_input == to_guess:
            print(f"Glueckwunsch, Zahl erraten. Anzahl Versuche: {tries}")
            break
        
    except ValueError:
        print("Fehler: Das war keine gültige Zahl. Bitte versuche es erneut.")
    print("-" * 20)