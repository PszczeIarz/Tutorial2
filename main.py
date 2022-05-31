definicje = {}

while(True):
    print("1: Dodaj definicje")
    print("2: Znajdź definicje")
    print("3: Usuń definicję")
    print("4: Zakończ")

    wybor = input("Co chcesz zrobić")

    if (wybor == "1"):
        klucz = input("Podaj klucz (słowo) do definicji: ")
        definicja = input("Podaj definicje: ")
        definicje[klucz] = definicja
        print("Definicja została pomyślnie dodana")

    elif (wybor == "2"):
        klucz = input("Czego szukasz?: ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie znaleziono definicji o nazwie ", klucz)
    elif (wybor == "3"):
        klucz = input("Jaką definicję chcesz usunąć? ")
        if klucz in definicje:
            del(definicje)
            print("Definicja została pomyślnie usunięta ", klucz)
        else:
            print("Nie znaleziino twojej definicji ", klucz)
    elif (wybor == "4"):
        print("No to pa")
        break
    else:
        print("Podałeś coś po za zakresu")

