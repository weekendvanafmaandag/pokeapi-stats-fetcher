import os
import pandas as pd

CSV_FILE = "pokemon_history.csv"


def max_poke_in_db(total_count):
    """Deletes the CSV file if 10 or more Pokémon have been logged."""
    if total_count >= 10:
        if os.path.exists(CSV_FILE):
            os.remove(CSV_FILE)
            print(f"\n[Limit Reached] '{CSV_FILE}' reached 10 entries and was reset!")


def save_pokemon_data(number, name, types, is_gen1):
    # Convert list of types into a single string ("bug, poison")
    if isinstance(types, list):
        formatted_type = ", ".join(types)
    else:
        formatted_type = str(types)

    # 1. Create a dictionary for the new entry
    new_data = {
        "number": [number],
        "name": [name],
        "type": [formatted_type],
        "is_gen1": [is_gen1],
    }

    # 2. Convert to a new DataFrame
    df_new = pd.DataFrame(new_data)

    # 3. Append to existing CSV or create a new one
    if os.path.exists(CSV_FILE):
        df_existing = pd.read_csv(CSV_FILE)
        df_total = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_total = df_new

    # 4. Save to CSV without row indices
    df_total.to_csv(CSV_FILE, index=False)
    print(f"\ndata logged to '{CSV_FILE}' with pd lib!")

    # 5. Print current DataFrame and quick stats
    print("\n--- poke_dataframe ---\n")
    print(df_total)

    total_count = len(df_total)
    gen1_count = df_total["is_gen1"].sum()
    percentage = (gen1_count / total_count) * 100

    print("\n--- quick stats ---\n")
    print(f"collected: {total_count}")
    print(f"gen 1:     {gen1_count}    ({percentage:.1f}%)\n")

    # 6. Check if maximum limit is reached and clear file if needed
    max_poke_in_db(total_count)

    return df_total, total_count