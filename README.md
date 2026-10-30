# Titanic ELT

## Pipeline
Extract (Seaborn) -> Load raw data (MySQL) -> Transform (SQL) -> Validate.

## Setup
1. Install dependencies: `python -m pip install -r requirements.txt`
2. Create the database in MySQL: `CREATE DATABASE titanic_db;`
3. Update `config.py` with your MySQL username and password.
4. Use MySQL 8.0+ (CTEs and window functions are used).
5. Run `python main.py` or execute `ELT.ipynb`.

Output tables: `passengers_raw` and `passengers_transformed`.
