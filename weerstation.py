def fahrenheit(temp_celsius):
    """Zet Celsius om naar Fahrenheit"""
    return 32 + 1.8 * temp_celsius


def gevoelstemperatuur(temp_celsius, windsnelheid, vochtigheid):
    """Berekent hoe koud het aanvoelt"""
    return temp_celsius - (vochtigheid / 100) * windsnelheid


def weerrapport(temp_celsius, windsnelheid, vochtigheid):
    """Geeft een weerbericht op basis van gevoelstemperatuur en wind"""
    gevoel = gevoelstemperatuur(temp_celsius, windsnelheid, vochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def weerstation():
    """Hoofdfunctie: vraagt weerdata voor max 7 dagen"""
    temperaturen = []
    
    for dag in range(1, 8):  # dag 1 t/m 7
        # Vraag temperatuur
        temp_input = input(f"Wat is op dag {dag} de temperatuur[C]: ")
        if temp_input == "":
            print("bye")
            break

        # Vraag windsnelheid
        wind_input = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ")
        if wind_input == "":
            print("bye")
            break

        # Vraag vochtigheid
        vocht_input = input(f"Wat is op dag {dag} de vochtigheid[%]: ")
        if vocht_input == "":
            print("bye")
            break

        # Probeer de invoer om te zetten naar getallen
        try:
            temp_c = float(temp_input)
            wind = float(wind_input)
            vocht = int(vocht_input)
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")
            continue

        # Bereken Fahrenheit
        temp_f = fahrenheit(temp_c)

        # Haal weerrapport op
        rapport = weerrapport(temp_c, wind, vocht)

        # Voeg temperatuur toe aan lijst en bereken gemiddelde
        temperaturen.append(temp_c)
        gem = sum(temperaturen) / len(temperaturen)

        print(f"Het is {temp_c:.1f}C ({temp_f:.1f}F)")
        print(rapport)
        print(f"Gem. temp tot nu toe is {gem:.1f}")


if __name__ == "__main__":
    weerstation()