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


def calculate_subtotal_km() -> dict[str, float]:
    """Calculate total KM driven to all shops."""
    subtotals: dict[str, float] = {
        "total_km": 0.0,
        "hanos_km": 0.0,
        "sligro_km": 0.0,
        "makro_km": 0.0,
        "horeca_plus_km": 0.0,
        "eldee_km": 0.0,
    }

    distances: dict[str, float] = {
        "hanos": 6.0 * 2,
        "sligro": 4.8 * 2,
        "makro": 9.5 * 2,
        "horeca plus": 11.8 * 2,
        "eldee": 4.3 * 2,
    }

    store_counts = count_store_visits()

    subtotals["hanos_km"] = store_counts["hanos"] * distances["hanos"]
    subtotals["sligro_km"] = store_counts["sligro"] * distances["sligro"]
    subtotals["makro_km"] = store_counts["makro"] * distances["makro"]
    subtotals["horeca_plus_km"] = (
        store_counts["horeca plus"] * distances["horeca plus"]
    )
    subtotals["eldee_km"] = store_counts["eldee"] * distances["eldee"]
    subtotals["total_km"] = (
        subtotals["hanos_km"]
        + subtotals["sligro_km"]
        + subtotals["makro_km"]
        + subtotals["horeca_plus_km"]
        + subtotals["eldee_km"]
    )
    return subtotals
