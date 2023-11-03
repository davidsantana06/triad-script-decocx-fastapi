from typing import Dict, List
import json

from . constants import PRODUCTS_PATH, SEASONS_PATH


def get_season(country_name: str) -> List[str]:
    with open(SEASONS_PATH, 'r', encoding='utf-8') as seasons_file:
        seasons: Dict[str, str] = json.load(seasons_file)

    return seasons.get(country_name)


def get_products_by_season(season: str) -> List[Dict[str, object]]:
    with open(PRODUCTS_PATH, 'r', encoding='utf-8') as products_file:
        products: List[Dict[str, object]] = json.load(products_file)

    return [product for product in products if season in product['seasons']]
