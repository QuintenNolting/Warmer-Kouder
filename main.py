import random

def pick_random_number(bereik):
    random_number = random.randint(1, bereik)
    return random_number

def get_value(text, data_type):
    while True:
        try:
            return data_type(input(text))
        except:
            print("Dit is een incorrect datatype, probeer het opnieuw!")

def pick_difficulty():
    print("Welkom bij Warmer-Kouder.")
    print("Raad welk nummer het is terwijl wij je vertellen of het warmer of kouder is.")
    print("Op welke difficulty wil je spelen?")
    print("1) makkelijk (10 pogingen, nummer tussen 1 en 100)")
    print("2) normaal (6 pogingen, nummer tussen 1 en 100)")
    print("3) moeilijk (15 pogingen, nummer tussen 1 en 1000)")

    choice = get_value("", int)

    if choice == 1:
        pogingen = 10
        bereik = 100
    elif choice == 2:
        pogingen= 6
        bereik = 100
    elif choice == 3:
        pogingen = 15
        bereik= 1000

    return pogingen, bereik

def input_number(pogingen, random_number):
    iteration = 0
    while True:
        iteration += 1

        if iteration > pogingen:
            print(f"je hebt geen guesses meer... het goede nummer was {random_number}")
            return iteration

        guess = get_value(f"Wat is je {iteration + 1}e guess?: ", int)

        if guess < random_number:
            print("Die guess was koud... het nummer is hoger")
        elif guess > random_number:
            print("Die guess was warm... het nummer is lager")
        else:
            print("Je hebt het goed!!")
            return iteration
