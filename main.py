from fastapi import FastAPI
from users import router
from db import Base, engine

""""""
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)