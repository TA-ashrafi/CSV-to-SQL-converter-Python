import csv
import re
from datetime import datetime

def infer_sql_type(value):
    """Infer SQL data type based on the value."""
    if value is None or value.strip() == '':
        return 'VARCHAR(255)'
    
    try:
        int(value)
        return 'INTEGER'
    except ValueError:
        pass
    
    try:
        float(value)
        return 'FLOAT'
    except ValueError:
        pass
    
    try:
        datetime.strptime(value, '%Y-%m-%d')
        return 'DATE'
    except ValueError:
        try:
            datetime.strptime(value, '%d/%m/%Y')
            return 'DATE'
        except ValueError:
            pass
    
    return f'VARCHAR({min(255, len(value) + 10)})'

def sanitize_name(name):
    """Sanitize column names for SQL compatibility."""
    name = re.sub(r'[^a-zA-Z0-9\s]', '', name).strip()
    name = re.sub(r'\s+', '_', name)
    if name and name[0].isdigit():
        name = f'_{name}'
    return name or 'column'

def csv_to_sql(csv_file_path, table_name='#'):    # make sure that u enterd a file name 
    """Convert CSV file to SQL CREATE TABLE and INSERT statements."""
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)
            
            sanitized_headers = [sanitize_name(header) for header in headers]
            first_row = next(csv_reader, None)
            column_types = []
            
            if first_row:
                column_types = [infer_sql_type(value) for value in first_row]
            else:
                column_types = ['VARCHAR(255)' for _ in headers]
            
            columns_def = [
                f'"{col}" {col_type}' 
                for col, col_type in zip(sanitized_headers, column_types)
            ]
            create_table = f'CREATE TABLE {table_name} (\n    '
            create_table += ',\n    '.join(columns_def)
            create_table += '\n);'
            
            insert_statements = []
            if first_row:
                values = [
                    'NULL' if val.strip() == '' else f"'{val.replace('\'', '\'\'')}'"
                    for val in first_row
                ]
                insert = f'INSERT INTO {table_name} ({", ".join(f'"{col}"' for col in sanitized_headers)}) '
                insert += f'VALUES ({", ".join(values)});'
                insert_statements.append(insert)
                
                for row in csv_reader:
                    values = [
                        'NULL' if val.strip() == '' else f"'{val.replace('\'', '\'\'')}'"
                        for val in row
                    ]
                    insert = f'INSERT INTO {table_name} ({", ".join(f'"{col}"' for col in sanitized_headers)}) '
                    insert += f'VALUES ({", ".join(values)});'
                    insert_statements.append(insert)
            
            sql_output = [create_table]
            if insert_statements:
                sql_output.append('\n-- Insert statements')
                sql_output.extend(insert_statements)
            
            return '\n'.join(sql_output)
            
    except FileNotFoundError:
        return f"Error: File '{csv_file_path}' not found."
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    csv_file =    # HERE u can change your path Of sample_data.csv 
    table_name = '#'  # Here u can give name of table 
    
    sql_statements = csv_to_sql(csv_file, table_name)
    print("\nGenerated SQL Statements:\n")
    print(sql_statements)
    
    save = input("\nSave to SQL file? (y/n): ").lower() == 'y'
    if save:
        output_file = f"{table_name}.sql"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(sql_statements)
        print(f"SQL statements saved to {output_file}")

if __name__ == "__main__":
    main()
