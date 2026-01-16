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

# -----------------------------------------------------------------------

print(update_highscores(Name, Score))
