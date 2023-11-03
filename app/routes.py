from fastapi import APIRouter
from .services import get_season, get_products_by_season


router = APIRouter(prefix='/api')


@router.get('/products/{country_name}')
def products(country_name: str):
    season = get_season(country_name)
    products = get_products_by_season(season)
    return products
