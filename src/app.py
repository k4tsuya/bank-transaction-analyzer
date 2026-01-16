"""Main application logic for KM declaration."""

import csv

bank_data = []

# NOTE: The path is based on the CWD's execution path from main.py.
with open("./bank_data.csv") as f:
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


def count_shop_visits() -> dict[str, int]:
    """Count visits to each store in the shop list."""
    store_count: dict[str, int] = {
        "Hanos": 0,
        "Sligro": 0,
        "Makro": 0,
        "Horeca-Plus": 0,
        "Eldee": 0,
    }

    # item[9] contains the carrier terminal name.
    for item in bank_data:
        if item[9] == hanos:
            store_count["Hanos"] += 1
        elif item[9] == sligro:
            store_count["Sligro"] += 1
        elif item[9] == makro:
            store_count["Makro"] += 1
        elif item[9] == horeca_plus:
            store_count["Horeca-Plus"] += 1
        elif item[9] == eldee:
            store_count["Eldee"] += 1

    return store_count


def shop_distance() -> dict[str, float]:
    """Calculate the round-trip distance to each shop."""
    roundtrip = 2

    distance: dict[str, float] = {
        "Hanos": round(6.0 * roundtrip),
        "Sligro": round(4.8 * roundtrip),
        "Makro": round(9.5 * roundtrip),
        "Horeca-Plus": round(11.8 * roundtrip),
        "Eldee": round(4.3 * roundtrip),
    }

    return distance
