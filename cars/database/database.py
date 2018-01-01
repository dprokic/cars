import os
from contextlib import contextmanager

from alembic import command as alembic_command
from alembic.config import Config as AlembicConfig
from sqlalchemy import create_engine, pool
from sqlalchemy.orm import sessionmaker

from cars.database import model

ALEMBIC_CONFIG_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'alembic.ini')
ENGINE = None
SESSION = None


def upgrade_database():
    alembic_cfg = AlembicConfig(ALEMBIC_CONFIG_PATH)
    alembic_command.upgrade(alembic_cfg, "head")


def create_database():
    drop_sql = "DROP OWNED BY cars;"
    ENGINE.execute(drop_sql)
    upgrade_database()


def init_db():
    global ENGINE
    global SESSION
    if ENGINE is None:
        alembic_cfg = AlembicConfig(ALEMBIC_CONFIG_PATH)
        ENGINE = create_engine(alembic_cfg.get_main_option("sqlalchemy.url"), poolclass=pool.NullPool)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    global ENGINE
    global SESSION
    if SESSION is None:
        SESSION = sessionmaker(bind=ENGINE)
    session = SESSION()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_manufacturer(manufacturer_name):
    with session_scope() as session:
        manufacturer = session.query(model.Manufacturer).filter(
            model.Manufacturer.name == manufacturer_name).one_or_none()
        if manufacturer is None:
            manufacturer = model.Manufacturer(name=manufacturer_name)
            session.add(manufacturer)
            session.commit()
            session.refresh(manufacturer)
        return manufacturer


if __name__ == '__main__':
    upgrade_database()
    init_db()
    manufacturer = get_manufacturer("Škoda")
    print(manufacturer.id)
