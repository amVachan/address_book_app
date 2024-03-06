from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from address_book.crud import create_address, get_address, update_address, delete_address, get_addresses_within_distance
from address_book.database import SessionLocal, engine
from address_book.schemas import AddressCreate, Address
from address_book import models


models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_new_address(address: AddressCreate, db: Session = Depends(get_db)):
    return create_address(db, address)


@router.get("/{address_id}", response_model=Address)
def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = get_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found.")

    return db_address


@router.put("/{address_id}", response_model=Address)
def update_existing_address(address_id: int, address: AddressCreate, db: Session = Depends(get_db)):
    db_address = update_address(db, address_id, address)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found.")

    return db_address


@router.delete("/{address_id}")
def delete_existing_address(address_id: int, db: Session = Depends(get_db)):
    success = delete_address(db, address_id)
    if not success:
        raise HTTPException(status_code=404, detail="Address not found.")

    return {"message": "Address deleted successfully."}


@router.post("/within_distance")
def get_addresses_within_given_distance(latitude: float, longitude: float, distance: float, db: Session = Depends(get_db)):
    addresses = get_addresses_within_distance(
        db, latitude, longitude, distance)
    return addresses
