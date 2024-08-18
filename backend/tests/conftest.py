import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from sqlalchemy.exc import OperationalError


# this is to include backend dir in sys.path so that we can import from db,main.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import Base, get_db
from main import app



def pytest_addoption(parser):
    parser.addoption(
        "--dburl", 
        action="store",
        default="sqlite:///./test_db.db", 
        help="Database URL to use for tests.",
    )


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    db_url = session.config.getoption("--dburl")
    try:
        # Attempt to create an engine and connect to the database.
        engine = create_engine(
            db_url,
            poolclass=StaticPool,
        )
        connection = engine.connect()
        connection.close()  # Close the connection right after a successful connect.
        print("Database connection successful........")
    except OperationalError as e:
        print(f"Failed to connect to the database at {db_url}: {e}")
        pytest.exit(
            "Stopping tests because database connection could not be established."
        )


@pytest.fixture(scope="session")
def db_url(request):
    """Fixture to retrieve the database URL."""
    return request.config.getoption("--dburl")


@pytest.fixture(scope="function")
def db_session(db_url):
    """Create a new database session with a rollback at the end of the test."""
    # Create a SQLAlchemy engine
    engine = create_engine(
        db_url,
        poolclass=StaticPool,
    )

    # Create a sessionmaker to manage sessions
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create tables in the database
    Base.metadata.create_all(bind=engine)
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def test_client(db_session):
    """Create a test client that uses the override_get_db fixture to return a session."""

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="function")
def jobs_endpoint():
    return "/api/jobs/"


@pytest.fixture(scope="function")
def locations_endpoint():
    return "/api/locations/"


@pytest.fixture(scope="function")
def all_data_vancancy_payload():
    """Generate a vancancy."""
    return {
        "id": 123,
        "company_name": "ABC Corporation",
        "title": "Software Engineer",
        "salary": "100000",
        "location": "New York",
        "speciality": "Python",
        "internship": True,
        "remote": False,
        "url": "https://example.com/job",
        "description": "This is a job description.",
    }

@pytest.fixture(scope="function") 
def required_data_vancancy_payload():
    """Generate a vancancy."""
    return {
    "title": "Software Engineer",
    "speciality": "Python"
}

@pytest.fixture(scope="function")
def validation_error_payload():
    """Generate a vancancy with error."""
    return {
        "title": None,
        "salary": 4545
    }
