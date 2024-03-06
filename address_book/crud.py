from sqlalchemy.orm import Session
from address_book.models import Address
from address_book.schemas import AddressCreate

from geopy.distance import geodesic


def create_address(db: Session, address: AddressCreate):
    db_address = Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def get_address(db: Session, address_id: int):
    return db.query(Address).filter(Address.id == address_id).first()


def update_address(db: Session, address_id: int, address_data: AddressCreate):
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address:
        for key, value in address_data.dict().items():
            setattr(db_address, key, value)
        db.commit()
        db.refresh(db_address)
        return db_address
    else:
        return None


def delete_address(db: Session, address_id: int):
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address:
        db.delete(db_address)
        db.commit()

        return True
    else:
        return False


def get_addresses_within_distance(db: Session, latitude: float, longitude: float, distance: float):
    target_location = (latitude, longitude)
    addresses = db.query(Address).all()

    filtered_addresses = []

    for address in addresses:
        address_loctaion = (address.latitude, address.longitude)
        if geodesic(target_location, address_loctaion).kilometers <= distance:
            filtered_addresses.append(address)

    return filtered_addresses
