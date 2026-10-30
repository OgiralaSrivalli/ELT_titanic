from extract import extract
from load import load
from transform import transform
from validate import validate

def main():
    raw_df = extract()
    load(raw_df)
    transform()
    validate()
    print("ELT pipeline completed successfully.")

if __name__ == "__main__":
    main()
