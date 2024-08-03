from fastapi import FastAPI
from routers.users import user

from config.database import engine

app = FastAPI()

app.include_router(user)

@app.on_event('startup')
async def on_startup():
    print("La aplicación ha iniciado")

@app.on_event('shutdown')
async def on_shutdown():
    engine.dispose()
    print("La aplicación se está cerrando")