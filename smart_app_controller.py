def aantal_dagen(inputFile):
    """Tel hoeveel dagen er in het bestand staan (zonder de kopregel)"""
    try:
        with open(inputFile, "r") as f:
            regels = f.readlines()
        # Eerste regel is de kop, dus die tel ik niet mee
        return len(regels) - 1
    except FileNotFoundError:
        print("Bestand niet gevonden!")
        return 0


def auto_bereken(inputFile, outputFile):
    """Leest input bestand en schrijft berekende actuator waarden naar output bestand"""
    try:
        with open(inputFile, "r") as f:
            regels = f.readlines()
    except FileNotFoundError:
        print("Input bestand niet gevonden!")
        return

    # Open output bestand om te schrijven
    with open(outputFile, "w") as out:
        # Sla de eerste regel over
        for regel in regels[1:]:
            regel = regel.strip()
            if regel == "":
                continue
            
            # Split de regel op spaties
            delen = regel.split()
            datum = delen[0]
            num_mensen = int(delen[1])
            temp_binnen = float(delen[2])
            temp_buiten = float(delen[3])
            neerslag = float(delen[4])

            # Bereken CV ketel stand
            verschil = temp_binnen - temp_buiten
            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            # Bereken ventilatie stand
            ventilatie = num_mensen + 1
            if ventilatie > 4:
                ventilatie = 4

            # Bereken bewatering
            if neerslag < 3:
                bewatering = True
            else:
                bewatering = False

            # Schrijf naar output bestand
            out.write(f"{datum};{cv};{ventilatie};{bewatering}\n")

    print(f"Berekeningen klaar! Geschreven naar {outputFile}")


def overwrite_settings(outputFile):
    """Overschrijf een waarde in het output bestand"""
    # Lees eerst alle regels in
    try:
        with open(outputFile, "r") as f:
            regels = f.readlines()
    except FileNotFoundError:
        print("Output bestand niet gevonden! Voer eerst optie 2 uit.")
        return -1

    # Vraag welke datum
    datum = input("Welke datum wil je aanpassen (bijv. 08-10-2025)? ")
    
    # Zoek de regel met deze datum
    gevonden = False
    regel_index = -1
    for i, regel in enumerate(regels):
        if regel.startswith(datum):
            gevonden = True
            regel_index = i
            break

    if not gevonden:
        print("Datum niet gevonden!")
        return -1

    # Vraag welk systeem
    print("Kies systeem: 1=CV-ketel, 2=Ventilatie, 3=Bewatering")
    raw = input("Systeem (je mag 1/2/3 of een naam typen): ").strip().lower()

    # Sta zowel nummers als woorden toe
    if raw in ("1", "cv", "cv-ketel", "cv ketel"):
        systeem = "1"
    elif raw in ("2", "vent", "ventilatie"):
        systeem = "2"
    elif raw in ("3", "bewatering", "water", "plants", "planten"):
        systeem = "3"
    else:
        print("Ongeldig systeem!")
        return -3

    # Vraag nieuwe waarde
    nieuwe_waarde = input("Nieuwe waarde: ")

    # Haal de oude regel op en split deze
    oude_regel = regels[regel_index].strip()
    delen = oude_regel.split(";")

    # Pas de juiste waarde aan
    if systeem == "1":  # CV ketel
        try:
            waarde = int(nieuwe_waarde)
            if waarde < 0 or waarde > 100:
                print("CV ketel moet tussen 0 en 100 zijn!")
                return -3
            delen[1] = str(waarde)
        except ValueError:
            print("Ongeldige waarde!")
            return -3

    elif systeem == "2":  # Ventilatie
        try:
            waarde = int(nieuwe_waarde)
            if waarde < 0 or waarde > 4:
                print("Ventilatie moet tussen 0 en 4 zijn!")
                return -3
            delen[2] = str(waarde)
        except ValueError:
            print("Ongeldige waarde!")
            return -3

    elif systeem == "3":  # Bewatering
        if nieuwe_waarde == "0":
            delen[3] = "False"
        elif nieuwe_waarde == "1":
            delen[3] = "True"
        else:
            print("Bewatering moet 0 of 1 zijn!")
            return -3

    # Maak de nieuwe regel
    nieuwe_regel = ";".join(delen) + "\n"
    regels[regel_index] = nieuwe_regel

    # Schrijf alles terug naar het bestand
    with open(outputFile, "w") as f:
        f.writelines(regels)

    print("Waarde succesvol aangepast!")
    return 0


def smart_app_controller():
    """Hoofdmenu voor de Smart App Controller"""
    print("Welkom bij de Smart App Controller!")
    
    # Vraag bestandsnamen
    input_bestand = input("Wat is de naam van het input bestand? (bijv. input.txt): ")
    output_bestand = input("Wat is de naam van het output bestand? (bijv. output.txt): ")

    # Menu loop
    while True:
        print("\nMENU")
        print("1. Hoeveel dagen zijn er aanwezig?")
        print("2. Autobereken alle actuatoren en schrijf naar bestand")
        print("3. Overschrijf een berekende waarde")
        print("4. Stoppen")
        
        keuze = input("Maak een keuze (1-4): ")

        if keuze == "1":
            aantal = aantal_dagen(input_bestand)
            print(f"Er zijn {aantal} dagen aanwezig.")
        
        elif keuze == "2":
            auto_bereken(input_bestand, output_bestand)
        
        elif keuze == "3":
            resultaat = overwrite_settings(output_bestand)
            print(f"Resultaat code: {resultaat}")
        
        elif keuze == "4":
            print("Programma gestopt. Tot ziens!")
            break
        
        else:
            print("Ongeldige keuze, probeer opnieuw.")


if __name__ == "__main__":
    smart_app_controller()