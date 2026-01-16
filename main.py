import random

def pick_random_number(bereik):
    random.randint(1, bereik)

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
    print("3) moeilijk (10 pogingen, nummer tussen 1 en 1000)")

    choice = get_value("", int)

    if choice == 1:
        pogingen = 10
        bereik = 100
    elif choice == 2:
        pogingen= 6
        bereik = 100
    elif choice == 3:
        pogingen = 10
        bereik= 1000

    return pogingen, bereik
    
def update_highscores(name, score, filename="highscores.txt"):
    try:
        with open(filename, "r") as f:
            scores = []
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    n, s = parts
                    scores.append((n, int(s)))
    except FileNotFoundError:
        scores = []

    scores.append((name, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    with open(filename, "w") as f:
        for n, s in scores:
            f.write(f"{n} {s}\n")

    return scores


