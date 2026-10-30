from sqlalchemy import text
from config import get_engine

def transform():
    """Transform data inside MySQL after it has been loaded (ELT)."""
    engine = get_engine()

    sql = """
    CREATE TABLE passengers_transformed AS
    WITH age_ranked AS (
        SELECT
            age,
            ROW_NUMBER() OVER (ORDER BY age) AS rn,
            COUNT(*) OVER () AS cnt
        FROM passengers_raw
        WHERE age IS NOT NULL
    ),
    median_age AS (
        SELECT AVG(age) AS median_age
        FROM age_ranked
        WHERE rn IN (
            FLOOR((cnt + 1) / 2),
            FLOOR((cnt + 2) / 2)
        )
    ),
    embarked_mode AS (
        SELECT embarked
        FROM passengers_raw
        WHERE embarked IS NOT NULL
        GROUP BY embarked
        ORDER BY COUNT(*) DESC
        LIMIT 1
    )
    SELECT
        r.survived,
        r.pclass,
        CASE
            WHEN r.sex = 'male' THEN 0
            WHEN r.sex = 'female' THEN 1
            ELSE NULL
        END AS sex,
        COALESCE(r.age, m.median_age) AS age,
        r.sibsp,
        r.parch,
        r.fare,
        COALESCE(r.embarked, (SELECT embarked FROM embarked_mode)) AS embarked,
        r.`class`,
        r.who,
        r.adult_male,
        r.alive,
        r.alone
    FROM passengers_raw AS r
    CROSS JOIN median_age AS m
    """

    try:
        with engine.begin() as connection:
            connection.execute(text("DROP TABLE IF EXISTS passengers_transformed"))
            connection.execute(text(sql))
        print("SQL transformation completed. Created 'passengers_transformed'.")
    finally:
        engine.dispose()
