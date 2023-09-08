alphabet = {
    1: "A",
    2: "B",
    3: "C",
    4: "X",
    5: "Y",
}

for key, pair in alphabet.items():
    if pair in 'AY':
        print(f"Ключ: {key} Значение:{pair}")