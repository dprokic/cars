from setuptools import setup, find_packages

setup(
    name='cars',
    version='0.0.1',

    description='Social network for car lovers',

    packages=find_packages(),

    install_requires=[
        'SQLAlchemy',
        'alembic',
        'psycopg2',
        'scrapy',
    ]

)
