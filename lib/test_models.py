import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev

# Setup an in-memory SQLite database for testing
@pytest.fixture(scope="module")
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # Create tables
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_create_company(session):
    new_company = Company(name="TestCo", founding_year=2020)
    session.add(new_company)
    session.commit()
    
    company_in_db = session.query(Company).filter_by(name="TestCo").first()
    assert company_in_db is not None
    assert company_in_db.founding_year == 2020

def test_create_dev(session):
    new_dev = Dev(name="Alice")
    session.add(new_dev)
    session.commit()

    dev_in_db = session.query(Dev).filter_by(name="Alice").first()
    assert dev_in_db is not None
    assert dev_in_db.name == "Alice"
