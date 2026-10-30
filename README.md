# Titanic Dataset – ELT Data Pipeline

## 1. Project Overview

This project implements an **Extract, Load, Transform (ELT)** data pipeline using the Titanic passenger dataset. It demonstrates how raw data can be extracted from a source, loaded directly into a MySQL database, and subsequently transformed using SQL.

The primary objective is to demonstrate database-oriented data transformation while maintaining the original dataset separately from the processed output.

## 2. Project Objectives

- Implement an end-to-end ELT data pipeline using Python and MySQL.
- Extract and inspect the Titanic passenger dataset.
- Load raw data into a relational database.
- Perform data cleaning and transformation using SQL.
- Validate the transformed dataset.
- Understand the practical differences between ETL and ELT architectures.

## 3. Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Pipeline implementation |
| Pandas | Data manipulation and inspection |
| Seaborn | Titanic dataset source |
| MySQL | Relational database storage |
| SQL | Data transformation |
| SQLAlchemy | Python–MySQL connectivity |
| MySQL Connector | Database connection |
| Jupyter Notebook | Interactive execution and analysis |

## 4. Project Architecture

The pipeline follows the ELT architecture:

**Extract → Load → Transform**

### Stage 1: Extract

- Retrieve the Titanic dataset using Seaborn.
- Load the dataset into a Pandas DataFrame.
- Examine the dataset structure, dimensions, column names and missing values.

### Stage 2: Load

- Establish a connection between Python and MySQL.
- Load the original dataset into the database without performing the primary cleaning operations.
- Store the extracted data in the `passengers_raw` table.

### Stage 3: Transform

- Perform data cleaning and transformation directly within MySQL using SQL.
- Handle missing values.
- Convert categorical values into the required numerical representation.
- Apply the required column selection and cleaning operations.
- Store the processed output in the `passengers_transformed` table.

### Stage 4: Validate

- Verify the transformed table.
- Inspect the resulting records and data structure.
- Check missing values and record counts.
- Confirm that the expected dataset has been retained.

## 5. Project Structure

```text
ELT_Titanic/
│
├── config.py          # Database configuration
├── ELT.ipynb          # Main ELT workflow
├── extract.py         # Data extraction
├── load.py            # Loading data into MySQL
├── transform.py       # SQL-based transformation
├── validate.py        # Data validation
├── main.py            # Pipeline execution
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

## 6. Database Design

**Database Name:** `titanic_db`

The pipeline uses two tables to separate the original data from the transformed output.

| Table Name | Description |
|---|---|
| `passengers_raw` | Stores the original extracted Titanic dataset. |
| `passengers_transformed` | Stores the cleaned and transformed dataset. |

This separation preserves the source data and allows transformations to be performed independently.

## 7. Installation and Configuration

### Prerequisites

- Python installed
- MySQL Server and MySQL Workbench
- Jupyter Notebook or Visual Studio Code

### Install Dependencies

Clone or download the repository and navigate to the project directory.

```bash
pip install -r requirements.txt
```

### Configure Database Connection

Update the MySQL credentials in `config.py` according to your local database configuration.

Configure the following parameters:

- Host: `localhost`
- Username: `root`
- Password: Your MySQL password
- Database: `titanic_db`

Create the database if it does not already exist:

```sql
CREATE DATABASE titanic_db;
```

## 8. Execution

1. Open the `ELT_Titanic` project folder in Visual Studio Code.
2. Open `ELT.ipynb`.
3. Ensure the required Python dependencies are installed.
4. Verify the MySQL connection configuration.
5. Execute the notebook cells sequentially.
6. Verify the raw and transformed tables in MySQL.

## 9. Results

The ELT pipeline was successfully executed using the Titanic passenger dataset.

| Metric | Result |
|---|---:|
| Source Records | 891 |
| Records Loaded into Raw Table | 891 |
| Records in Transformed Table | 891 |
| Raw Table | `passengers_raw` |
| Final Table | `passengers_transformed` |

The final transformed dataset contains **891 records**, matching the original dataset's record count.

## 10. ETL and ELT Comparison

| Feature | ETL | ELT |
|---|---|---|
| Processing order | Extract → Transform → Load | Extract → Load → Transform |
| Transformation location | Python | MySQL |
| Data loaded | Transformed data | Raw data first |
| Database tables | `passengers` | `passengers_raw`, `passengers_transformed` |
| Main approach | Transform before storage | Transform after storage |

## 11. Conclusion

This project demonstrates the implementation of an ELT pipeline using Python, Pandas, SQL and MySQL. By loading the original dataset before performing transformations, the pipeline maintains a separate raw-data table and a transformed-data table.

The implementation provides practical experience in data extraction, relational database integration, SQL-based transformation and data validation. It also highlights the architectural differences between ETL and ELT approaches.# ELT_titanic
