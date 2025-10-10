from weerstation import weerstation
from smart_app_controller import smart_app_controller
from weather_api import huidige_temp_utrecht

def main():
    print("Welkom bij het Smart App Platform")

    while True:
        print("\nHOOFDMENU")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Huidige temperatuur in Utrecht (API)")
        print("4. Stoppen")

        try:
            keuze = input("Maak een keuze (1-4): ").strip()
        except Exception as e:
            print(f"Er ging iets mis bij het lezen van je invoer: {e}")
            continue

        if keuze == "1":
            try:
                weerstation()
            except Exception as e:
                print(f"Fout in Weerstation: {e}")

        elif keuze == "2":
            try:
                smart_app_controller()
            except FileNotFoundError:
                print("Bestand niet gevonden. Controleer bestandsnamen en pad.")
            except ValueError as e:
                print(f"Ongeldige waarde: {e}")
            except Exception as e:
                print(f"Onverwachte fout in Controller: {e}")

        elif keuze == "3":
            try:
                temp = huidige_temp_utrecht()
                print(f"Huidige temperatuur in Utrecht: {temp:.1f} °C")
            except Exception as e:
                print("Kon de temperatuur niet ophalen (internet of API probleem).")
                print(f"Technische info: {e}")

        elif keuze == "4":
            print("Tot ziens!")
            break

        else:
            print("Ongeldige keuze, kies 1 t/m 4.")

if __name__ == "__main__":
    main()