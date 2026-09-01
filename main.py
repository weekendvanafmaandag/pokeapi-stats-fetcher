import random
import requests as rq
import data_handler

MAX_POKEMON = 1025


def get_random_number():
    num = random.randint(1, MAX_POKEMON)
    print(f"poke_num:   {num}")
    return num


def check_is_gen1(num):
    return num <= 151


def fetch_pokemon_details(num):
    """Fetches both name and types in a single API call."""
    url = f"https://pokeapi.co/api/v2/pokemon/{num}"
    headers = {"User-Agent": "PokeApp/1.0"}

    try:
        response = rq.get(url=url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        name = data["name"].capitalize()
        types = [t["type"]["name"] for t in data["types"]]

        return name, types

    except rq.exceptions.RequestException as e:
        print(f"Fetch failed: {e}")
        return None, None


def get_type_effectiveness(pokemon_type):
    """Fetches damage relations for a specific type (e.g., 'fire')."""
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type.lower()}"
    headers = {"User-Agent": "PokeApp/1.0"}

    try:
        response = rq.get(url=url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Extract types that deal double damage to this type
        double_damage_from = [
            t["name"]
            for t in data["damage_relations"]["double_damage_from"]
        ]
        return double_damage_from

    except rq.exceptions.RequestException as e:
        print(f"Failed to fetch type relations: {e}")
        return []


def main():
    num = get_random_number()
    is_gen1 = check_is_gen1(num)
    name, types = fetch_pokemon_details(num)

    if name and types:
        print(f"poke_name:  {name}")
        print(f"poke_types: {', '.join(types)}")
        print(f"is_gen1:    {is_gen1}")

        # Check type weaknesses for the primary type
        weaknesses = get_type_effectiveness(types[0])
        print(f"Weak against: {', '.join(weaknesses)}")

        # Send data to data_handler.py
        # (save_pokemon_data handles saving and checks the 10-entry limit automatically)
        data_handler.save_pokemon_data(
            number=num, name=name, types=types, is_gen1=is_gen1
        )


if __name__ == "__main__":
    main()