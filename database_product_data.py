import pymysql
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")
try:
    print('Opening connection...')
    # Establish a database connection
    with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password
        ) as connection:
        print('Opening cursor...')
        cursor = connection.cursor()
        print('Inserting new record...')
        # Insert a new record
        sql = """
            INSERT INTO products (name, price)
                            VALUES (%s, %s) 
            """
        # I REMOVED ONE OF THE %S ABOVE
        
        data_values = ('Chocolate', 2.50)
        cursor.execute(sql, data_values)
        # I REMOVED THE PRICES AND THE PURCHASE DATE FROM ALL
        # Commit the record
        connection.commit()
        print('Selecting all records...')
        # Execute SQL query
        cursor.execute('SELECT name, price FROM products')
        # Fetch all the rows into memory
        rows = cursor.fetchall()
    
    
        print('Displaying all records...')
        # Gets all rows from the result
        for row in rows:
            print(f'name: {row[0]}, phone: {row[1]}')
    
        # Can alternatively get one result at a time with the below code
        # while True:
        #     row = cursor.fetchone()
        #     if row == None:
        #         break
        #     print(f'First Name: {row[0]}, Last Name: {row[1]}, Age: {row[2]}')
        print('Closing cursor...')
        # Closes the cursor so will be unusable from this point
        cursor.close()
        # The connection will automatically close here
except Exception as ex:
    print('Failed to:', ex)
# Leave this line here!
print('All done!')