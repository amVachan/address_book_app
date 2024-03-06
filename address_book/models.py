from sqlalchemy import Column, Integer, String, Float
from address_book.database import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email_address = Column(String, index=True, nullable=True)
    phone_number = Column(String, nullable=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String, nullable=True)
    latitude = Column(Float)
    longitude = Column(Float)
