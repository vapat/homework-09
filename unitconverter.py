print("hallo! hier kannst du kilometer in meilen umrechnen.")

km = int(input("gib bitte die km zahl ein: "))
print(km * 0.621371, "meilen")

print("möchtest du noch etwas umrechnen? Ja / Nein")

antwort = input(" ")

while antwort != "Nein":
    km = int(input("gib bitte die km zahl ein: "))
    print(km * 0.621371, "meilen")

    print("möchtest du noch etwas umrechnen? Ja / Nein")
    antwort = input(" ")

    if antwort == "Nein":
        print("auf wiedersehen")
        break