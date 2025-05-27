#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Company, Dev, Freebie, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)  # just in case tables aren't created

    session = Session(engine)

    # Add some companies
    company1 = Company(name="Coffee Co", founding_year=1999)
    company2 = Company(name="Tech Corp", founding_year=2010)

    # Add some developers
    dev1 = Dev(name="Alice")
    dev2 = Dev(name="Bob")

    session.add_all([company1, company2, dev1, dev2])
    session.commit()

    # Add some freebies
    freebie1 = Freebie(item_name="Coffee Mug", value=10, company=company1, dev=dev1)
    freebie2 = Freebie(item_name="T-Shirt", value=20, company=company2, dev=dev2)
    freebie3 = Freebie(item_name="Sticker Pack", value=5, company=company2, dev=dev1)

    session.add_all([freebie1, freebie2, freebie3])
    session.commit()

    print("Seed data added.")
