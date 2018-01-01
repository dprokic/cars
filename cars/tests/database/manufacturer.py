import pytest
from cars.database import database


@pytest.fixture
def setup():
    database.init_db()
    database.create_database()
    database.upgrade_database()


def test_new_manufacturer(setup):
    manufacturer = database.get_manufacturer("Škoda")
    assert manufacturer.id == 1
