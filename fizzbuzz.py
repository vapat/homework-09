print("Hallo!")

zahl = int(input("Wähle eine Zahl zwischen 1 und 100: "))

for zahl in range(1, zahl+1):
    if zahl % 3 == 0:
        print("fizz")
    elif zahl % 5 == 0:
        print("buzz")
    elif zahl % 3 == 0 and zahl % 5 == 0:
        print("fizzbuzz")
    else:
        print(zahl)