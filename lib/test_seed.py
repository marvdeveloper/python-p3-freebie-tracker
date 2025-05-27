# lib/test_seed.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Base

@pytest.fixture(scope="module")
def session():
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_companies_exist(session):
    companies = session.query(Company).all()
    assert len(companies) > 0
    assert any(c.name == "Coffee Co" for c in companies)
    assert any(c.name == "Tech Corp" for c in companies)

def test_devs_exist(session):
    devs = session.query(Dev).all()
    assert len(devs) > 0
    assert any(d.name == "Alice" for d in devs)
    assert any(d.name == "Bob" for d in devs)
