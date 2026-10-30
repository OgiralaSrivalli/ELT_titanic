from sqlalchemy import text
from config import get_engine

def validate(table_name="passengers_transformed"):
    """Validate the transformed table inside MySQL."""
    engine = get_engine()
    try:
        with engine.connect() as connection:
            count = connection.execute(
                text(f"SELECT COUNT(*) FROM `{table_name}`")
            ).scalar_one()

            null_age = connection.execute(
                text(f"SELECT COUNT(*) FROM `{table_name}` WHERE age IS NULL")
            ).scalar_one()

            null_embarked = connection.execute(
                text(f"SELECT COUNT(*) FROM `{table_name}` WHERE embarked IS NULL")
            ).scalar_one()

            invalid_sex = connection.execute(
                text(f"SELECT COUNT(*) FROM `{table_name}` WHERE sex NOT IN (0, 1) OR sex IS NULL")
            ).scalar_one()

        if count == 0:
            raise ValueError("The transformed table is empty.")
        if null_age or null_embarked or invalid_sex:
            raise ValueError(
                f"Validation failed: null age={null_age}, "
                f"null embarked={null_embarked}, invalid sex={invalid_sex}"
            )

        print(f"Validation passed: {count} rows in '{table_name}'.")
        return True
    finally:
        engine.dispose()
