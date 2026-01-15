"""Simple KM declaration script."""

import csv

bank_data = []

with open("bank_data.csv") as f:
    data = csv.reader(f)
    bank_data: list[list[str]] = list(data)


hanos: str = "Hanos Heerlen"
sligro: str = "Sligro ZB 5032"
makro: str = "Makro Nuth"
horeca_plus: str = "Horeca-Plus Nuth"
eldee: str = "BCK*Eldee Pak Pak"

shop_list: list[str] = [
    hanos,
    sligro,
    makro,
    horeca_plus,
    eldee,
]


def count_store_visits() -> dict[str, int]:
    """Count visits to each store in the shop list."""
    store_counts: dict[str, int] = {
        "hanos": 0,
        "sligro": 0,
        "makro": 0,
        "horeca plus": 0,
        "eldee": 0,
    }

    # item[9] contains the carrier terminal name.
    for item in bank_data:
        if item[9] == hanos:
            store_counts["hanos"] += 1
        elif item[9] == sligro:
            store_counts["sligro"] += 1
        elif item[9] == makro:
            store_counts["makro"] += 1
        elif item[9] == horeca_plus:
            store_counts["horeca plus"] += 1
        elif item[9] == eldee:
            store_counts["eldee"] += 1

    return store_counts


count_store_visits()


def print_shop_visits() -> None:
    """Print all bank data entries for visits to shops in the shop list."""
    for item in count_store_visits():
        print(
            f"{item.title()}: {count_store_visits()[item]}",
        )


print_shop_visits()
