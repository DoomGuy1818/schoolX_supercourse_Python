p1, p2 = input().split(" ")

p1 = p1.lower()
p2 = p2.lower()


if (p1 == "камень" and p2 == "ножницы") or (p1 == "ножницы" and p2 == "бумага") or (p1 == "бумага" and p2 == "камень"):
    print("игрок 1 победил")

elif (p1 == "ножницы" and p2 == "камень") or (p2 == "ножницы" and p1 == "бумага") or (p2 == "бумага" and p1 =="камень"):
    print("игрок 2 победил")

elif (p1 == "камень" and p2 == "камень") or (p1 == "ножницы" and p2 == "ножницы") or (p1 == "бумага" and p2 == "бумага"):
    print("дружеская ничья :)")

else:
    print("Чел, что ты высрал вообще?..")
