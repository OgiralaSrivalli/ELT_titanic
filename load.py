from config import get_engine

def load(df, table_name="passengers_raw"):
    """Load the original, untransformed dataset into MySQL."""
    df = df.copy()

    # MySQL does not understand pandas category dtype; store categories as text.
    for col in df.select_dtypes(include=["category"]).columns:
        df[col] = df[col].astype("object")

    engine = get_engine()
    try:
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False,
            chunksize=500,
        )
        print(f"Loaded {len(df)} raw rows into MySQL table '{table_name}'.")
    finally:
        engine.dispose()
