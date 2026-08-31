import random
import requests

MAX_POKEMON = 1025


def rand_poke():
    poke_num = random.randint(1, MAX_POKEMON)
    print(f"poke_num:  {poke_num}")
    return poke_num


def poke_real(poke_num):
    if poke_num <= 151:
        real = True
    else:
        real = False
    return real


def get_name(pokedex_num):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokedex_num}"
    headers = {"User-Agent": "PokeApp/1.0"}

    try:
        response = requests.get(url=url, headers=headers, timeout=10)

        # 1. Alleen aanroepen (niet printen!)
        response.raise_for_status()

        # 2. Pas daarna omzetten naar JSON
        data = response.json()
        poke_naam = data["name"]

        return poke_naam

    except requests.exceptions.RequestException as e:
        return f"Ophalen mislukt (foutmelding: {e})"


def main():
    # 1. Haal een random nummer op
    nummer = rand_poke()

    # 2. Voer de check uit
    poke_real(nummer)

    # 3. Haal de naam op en print deze
    naam = get_name(nummer).capitalize()

    print("poke_name: " + naam)


if __name__ == "__main__":
    main()