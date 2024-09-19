# import mysql.connector
# import pandas as pd
# from database.db_config import DB_CONFIG

# def fetch_data_from_db(query):
#     """Fetch data from the database based on a SQL query."""
#     try:
#         conn = mysql.connector.connect(
#             host=DB_CONFIG['host'],
#             user=DB_CONFIG['user'],
#             password=DB_CONFIG['password'],
#             database=DB_CONFIG['database']
#         )
#         df = pd.read_sql(query, conn)
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return None
#     finally:
#         conn.close()
#     return df

# def clean_column_names(df):
#     """Clean column names to be valid SQL identifiers."""
#     df.columns = [f"`{col.replace(' ', '_').replace('-', '_').replace('/', '_')}`" for col in df.columns]
#     return df

# def infer_sql_type(col):
#     """Infer SQL column type based on the pandas Series dtype."""
#     if pd.api.types.is_integer_dtype(col):
#         return "INT"
#     elif pd.api.types.is_float_dtype(col):
#         return "FLOAT"
#     else:
#         return "VARCHAR(255)"

# def create_table_from_df(cursor, table_name, df):
#     """Create a table based on the DataFrame's structure."""
#     df = clean_column_names(df)  # Clean column names
#     columns = ', '.join([f"{col} {infer_sql_type(df[col])}" for col in df.columns])
#     create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})"
#     cursor.execute(create_table_query)

# def insert_data_to_db(data, table_name):
#     conn = mysql.connector.connect(
#         host=DB_CONFIG['host'],
#         user=DB_CONFIG['user'],
#         password=DB_CONFIG['password'],
#         database=DB_CONFIG['database']
#     )
#     cursor = conn.cursor()

#     # Create table if it doesn't exist
#     create_table_from_df(cursor, table_name, data)

#     # Insert data into table
#     for _, row in data.iterrows():
#         sql = f"INSERT INTO `{table_name}` ({', '.join(data.columns)}) VALUES ({', '.join(['%s'] * len(row))})"
#         try:
#             cursor.execute(sql, tuple(row))
#         except mysql.connector.Error as err:
#             print(f"Error inserting data: {err}")

#     conn.commit()
#     cursor.close()
#     conn.close()



# *******************************************************************************************************************************************


import mysql.connector
import pandas as pd
from database.db_config import DB_CONFIG

def fetch_data_from_db(query):
    """Fetch data from the database based on a SQL query."""
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        df = pd.read_sql(query, conn)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        conn.close()
    return df

def clean_column_names(df):
    """Clean column names to be valid SQL identifiers."""
    df.columns = [f"`{col.replace(' ', '_').replace('-', '_').replace('/', '_')}`" for col in df.columns]
    return df

def infer_sql_type(col):
    """Infer SQL column type based on the pandas Series dtype."""
    if pd.api.types.is_integer_dtype(col):
        return "INT"
    elif pd.api.types.is_float_dtype(col):
        return "FLOAT"
    else:
        return "VARCHAR(255)"

def create_table_from_df(cursor, table_name, df):
    """Create a table based on the DataFrame's structure."""
    df = clean_column_names(df)  # Clean column names
    columns = ', '.join([f"{col} {infer_sql_type(df[col])}" for col in df.columns])
    create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})"
    cursor.execute(create_table_query)

def insert_data_to_db(data, table_name):
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )
    cursor = conn.cursor()

    # Create table if it doesn't exist
    create_table_from_df(cursor, table_name, data)

    # Insert data into table
    for _, row in data.iterrows():
        sql = f"INSERT INTO `{table_name}` ({', '.join(data.columns)}) VALUES ({', '.join(['%s'] * len(row))})"
        try:
            cursor.execute(sql, tuple(row))
        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")

    conn.commit()
    cursor.close()
    conn.close()

def execute_sql(query):
    """Execute a SQL query and return the result as a DataFrame."""
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
            # Fetch the column names for the result
            columns = [desc[0] for desc in cursor.description]
            return pd.DataFrame(result, columns=columns)
        else:
            conn.commit()
            return f"Query executed successfully: {query}"
    except mysql.connector.Error as err:
        return f"Error executing SQL: {err}"
    finally:
        cursor.close()
        conn.close()
