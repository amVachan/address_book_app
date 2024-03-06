
from fastapi import FastAPI
from address_book.endpoints import router

app = FastAPI()

app.include_router(router, prefix="/addresses", tags=["addresses"])
