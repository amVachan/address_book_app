from pydantic import BaseModel


class AddressBase(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    phone_number: int
    street: str
    city: str
    state: str
    postal_code: int
    latitude: float
    longitude: float


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True
