from dataclasses import dataclass

@dataclass
class Person:
    firstname: str = None
    lastname: str = None
    city: str = None
    country: str = None
    email: str = None
    phone: str = None
    address: str = None