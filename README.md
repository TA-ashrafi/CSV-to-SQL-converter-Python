# CSV-to-SQL-converter-Python


---

# Features

- Reads CSV files and extracts headers and data  
- Sanitizes column names for SQL compatibility (removes special characters, replaces spaces with underscores)  
- Infers SQL data types (*INTEGER, FLOAT, DATE, VARCHAR*) from the first data row  
- Generates `CREATE TABLE` and `INSERT` statements  
- Handles errors (e.g., file not found, malformed CSV)  
- Optionally saves SQL output to a file  

---

# Requirements

- Python 3.x  
- Standard libraries: `csv`, `re`, `datetime`  

---

# Usage

## *Prepare your CSV file*

Ensure it has headers in the first row (e.g., `Name,Age,City`).

---

## *Update the script*

1. Open `csv_to_sql.py`  
2. Modify the CSV file path in the `main()` function to point to your file:  
   ```python
   csv_file = r"path\to\your\Sample_data.csv"

Set the desired table name in main() (default is #):
- table_name = "your_table_name"

---


## Run the script
- python csv_to_sql.py

## Output
- The script prints the generated SQL statements

- Prompts to save to a .sql file (e.g., your_table_name.sql if y is entered)

## Use the SQL
- Copy the printed SQL or use the saved .sql file in your database (e.g., MySQL, PostgreSQL)


# Example
## Input CSV (Sample_data.csv):

- Name, Age, City
- John, 25, New York
- Alice, 30,
- Bob, 45, San Francisco

## Output SQL:

CREATE TABLE my_table (
    "Name" VARCHAR(255),
    "Age" INTEGER,
    "City" VARCHAR(255)
);

- INSERT INTO my_table ("Name", "Age", "City") VALUES ('John', '25', 'New York');
- INSERT INTO my_table ("Name", "Age", "City") VALUES ('Alice', '30', NULL);
- INSERT INTO my_table ("Name", "Age", "City") VALUES ('Bob', '45', 'San Francisco');

---

# Using on GitHub
## To use this project on GitHub, follow these steps:
Clone the Repository:

- git clone https://github.com/your-username/csv-to-sql-converter.git
- cd csv-to-sql-converter


---

## Changes Needed
File Path:
- Update the csv_file path in csv_to_sql.py (line ~68) to match your CSV location:
- csv_file = r"path\to\your\csv_file.csv"
Example: If your CSV is in the project folder, use a relative path like:

Table Name:
- Change table_name (line ~70) to your desired SQL table name:
- table_name = "your_table_name"
Avoid using # — it’s a placeholder; use a valid SQL table name like employees.

CSV File:
- Place your CSV file in the project directory or update the script path to its location.

Optional:
- To change default behavior (e.g., type detection or name cleaning), modify the infer_sql_type() or sanitize_name() functions.

## Run the Script Again
- python csv_to_sql.py

---

## Notes
- The script assumes the CSV has headers in the first row
- Data types are inferred from the first data row; ensure it is representative
- The output SQL is compatible with most databases but may need tweaks for specific SQL engines
- For large CSVs, consider optimizing for performance/memory usage

---

# License
MIT License — Feel free to reuse, modify, and distribute.

## Author
- Name: Tahseen Ashrafi
- Email: tahseenashrafi29@gmail.com
- LinkedIn: https://www.linkedin.com/in/tahseen-ashrafi-489a4825a/


