import seaborn as sns

def extract():
    """Extract the original Titanic dataset."""
    df = sns.load_dataset("titanic")
    print(f"Extracted {len(df)} rows and {len(df.columns)} columns.")
    return df
