from sqlalchemy import URL, create_engine

# Update these values to match your local MySQL setup.
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Srivalli@2006",
    "database": "titanic_db",
}

def get_engine():
    """Create a SQLAlchemy engine for the configured MySQL database."""
    url = URL.create(
        drivername="mysql+mysqlconnector",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
    )
    return create_engine(url)
