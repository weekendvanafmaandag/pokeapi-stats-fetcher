import os
import pandas as pd

CSV_FILE = "pokemon_history.csv"


def save_pokemon_data(number, name, is_gen1):
    # gets poke_data and puts it from dict to dataframe
    # create a dictionary for the new poke
    new_data = {"number": [number], "name": [name], "is_gen1": [is_gen1]}

    # convert naar nieuw dataframe met pd lib
    df_new = pd.DataFrame(new_data)

    # 3. append csv file or create a new one
    if os.path.exists(CSV_FILE):
        df_existing = pd.read_csv(CSV_FILE)
        df_total = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_total = df_new

    # 4. save to CSV without row indices
    df_total.to_csv(CSV_FILE, index=False)
    print(f"\ndata logged to '{CSV_FILE}' with pd lib!")

    # 5. print current DataFrame and quick stats
    print("\n---  poke_dataframe ---\n")
    print(df_total)

    total_count = len(df_total)
    gen1_count = df_total["is_gen1"].sum()
    percentage = (gen1_count / total_count) * 100

    print("\n--- quick stats ---\n")
    print(f"collected: {total_count}")
    print(f"gen 1:     {gen1_count}    ({percentage:.1f}%)\n")

    return df_total