from os import path


ROOT_DIR = path.abspath(
    path.join(
        path.dirname(__file__),
        '..'
    )
)
DATABASE_DIR = path.join(ROOT_DIR, 'database')
PRODUCTS_PATH = path.join(DATABASE_DIR, 'products.json')
SEASONS_PATH = path.join(DATABASE_DIR, 'seasons.json')
