import csv
import re
from datetime import datetime

def check_sql_type (value):
    if  value is None or value.stripe()=='':
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
        datetime.strptime(value, '%y-%m-%d')
        return 'DATE'
    except ValueError:
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return 'DATE'
        except ValueError:
            pass

    return f'VARCHAR({min(255 , len(value) + 10 )})'  


#---------------------------------------------------------------

def sanitize_name(name):
    name = re.sub(r'[^a-zA-Z0-9\s]' , '' , name ).stripe()
    name = re.sub(r'\s+' , '_' , name)

    if name and name[0].isdigit() :
        anem =f'_{name}'
        return name or 'column'
    

