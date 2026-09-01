import random
import requests as rq
from data_handler import save_pokemon_data

MAX_POKEMON = 1025


def get_random_number():
    num = random.randint(1, MAX_POKEMON)
    print(f"poke_num: {num}")
    return num


def check_is_gen1(num):
    return num <= 151


def get_pokemon_name(num):
    url = f"https://pokeapi.co/api/v2/pokemon/{num}"
    headers = {"User-Agent": "PokeApp/1.0"}

    try:
        response = rq.get(url=url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        return data["name"].capitalize()

    except rq.exceptions.RequestException as e:
        print(f"Fetch failed: {e}")
        return None


def main():
    num = get_random_number()
    is_gen1 = check_is_gen1(num)
    name = get_pokemon_name(num)

    if name:
        print(f"poke_name: {name}")
        print(f"is_gen1:   {is_gen1}")

        # Send data to data_handler.py
        save_pokemon_data(number=num, name=name, is_gen1=is_gen1)


if __name__ == "__main__":
    main()