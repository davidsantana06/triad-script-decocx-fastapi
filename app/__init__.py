from fastapi import FastAPI
from .routes import router


def create_app() -> FastAPI:
    app = FastAPI(
        title='TriadScript - DecoCX FastAPI',
        description='API de produtos para o projeto Hackaton da equipe TriadScript.',
        version='0.1.0'
    )
    app.include_router(router)

    return app
