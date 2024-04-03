import pymysql
import os
import csv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

# Defining data structures

product_list = ['banana', 'coke'] 
courier_list = ['jack']
order_list = []
order_status_list = ['Preparing', 'Shipped', 'Delivered']
orders_menu = ['Jack']
orders = []

def db_connection(test_connection):
    
    # Load environment variables from .env file
        if test_connection is None:
            try:
                load_dotenv()
                host_name = os.environ.get("mysql_host")
                database_name = os.environ.get("mysql_db")
                user_name = os.environ.get("mysql_user")
                user_password = os.environ.get("mysql_pass")
                test_connection = pymysql.connect(
                    host=host_name, database=database_name,
                    user=user_name, password=user_password
                )
                # test_connection.cursor = test_connection.cursor()
            except Exception as ex:
                print(f"Connection failed. Error: {ex}")
                raise SystemExit(ex)
        return test_connection








              
def closeconnection_function(close_connection):
    try:
        if isinstance(close_connection, pymysql.Connection):
            # close the cursor
            close_connection.cursor.close()
            # The connection will close here
            close_connection.close()
    except Exception as ex:
            print('Failed to:', ex)
    
    
    


def menu_option():
    option = input ("Enter the choice: ")
    return option

# def add_product():
    item = input("Enter item to add to the list: ")
    product_list.append(item)
    print(f"{item} added to the list.")
    
def add_product():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()
            print('Inserting new record...')
            
            item = input("Enter the name of the new product: ")
            price = float(input("Enter the price of the new product: "))
            
            # Insert a new record
            sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
            data_values = (item, price)
            cursor.execute(sql, data_values)
            
            # Commit the record
            connection.commit()
            print('Record inserted successfully!')
            
            print('Selecting all records...')
            # Execute SQL query
            cursor.execute('SELECT id, name, price FROM products')
            # Fetch all the rows into memory
            rows = cursor.fetchall()
            
            # Write fetched data to CSV file
            with open('products.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                # Write header
                csv_writer.writerow(['ID', 'Name', 'Price'])
                # Write rows
                csv_writer.writerows(rows)
                
            print('Data written to products.csv successfully!')
            
            print('Displaying all records...')
            # Display fetched data
            for row in rows:
                print(f'ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
            
            print('Closing cursor...')
            # Closes the cursor so it will be unusable from this point
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to add product:', ex)

# Leave this line here!
print('All done!')
    
# def add_product():
   # try:
      #

# Leave this line here!
# print('All done!')
    
#THE ABOVE FUNCTION PERSISTS MY DATA TO MYSQL :)

def remove_product():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()
            
            # Fetch all products from the database
            cursor.execute('SELECT id, name FROM products')
            products = cursor.fetchall()
            
            if products:
                print('Available Products:')
                for idx, product in enumerate(products, start=1):
                    print(f"{idx}. {product[1]}")
                
                item_index = int(input("Enter the index of the product you want to remove: ")) - 1
                
                if 0 <= item_index < len(products):
                    product_id = products[item_index][0]
                    
                    # Remove the selected product from the database
                    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
                    connection.commit()
                    
                    print("Product removed successfully!")
                    
                    # Update products.csv file
                    with open('products.csv', 'r', newline='') as csv_file:
                        reader = csv.reader(csv_file)
                        rows = list(reader)

                    with open('products.csv', 'w', newline='') as csv_file:
                        writer = csv.writer(csv_file)
                        for row in rows:
                            if str(product_id) not in row:
                                writer.writerow(row)
                        
                    print("Entry removed from products.csv file.")
                else:
                    print("Invalid index!")
            else:
                print("No products available to remove.")
            
            print('Closing cursor...')
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to remove product:', ex)

# Leave this line here!
print('All done!')
    
 
def display_products():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()
            print('Selecting all records...')
            # Execute SQL query to select all products
            cursor.execute('SELECT id, name, price FROM products')
            # Fetch all the rows into memory
            products = cursor.fetchall()

            if products:
                print('Displaying all products...')
                # Display the products
                for product in products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")
            else:
                print("No products available.")
            
            print('Closing cursor...')
            # Closes the cursor so it will be unusable from this point
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to:', ex)

# Leave this line here!
print('All done!')


def update_product():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()
            
            # Fetch all products from the database
            cursor.execute('SELECT id, name, price FROM products')
            products = cursor.fetchall()
            
            if products:
                print('Available Products:')
                for idx, product in enumerate(products, start=1):
                    print(f"{idx}. {product[1]} - Price: {product[2]}")
                
                item_index = int(input("Enter the index of the product you want to update: ")) - 1
                
                if 0 <= item_index < len(products):
                    product_id = products[item_index][0]
                    new_name = input("Enter the new name for the product: ")
                    new_price = float(input("Enter the new price for the product: "))
                    
                    # Update the selected product in the database
                    cursor.execute("UPDATE products SET name = %s, price = %s WHERE id = %s", (new_name, new_price, product_id))
                    connection.commit()
                    
                    print("Product updated successfully!")
                    
                    # Convert the products tuple to a list to update the desired item
                    products_list = list(products)
                    # Update the product in the list
                    products_list[item_index] = (product_id, new_name, new_price)
                    # Convert the list back to a tuple
                    products = tuple(products_list)
                    
                    # Rewrite data to the CSV file after updating the product
                    with open('products.csv', 'w', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        # Write header
                        csv_writer.writerow(['ID', 'Name', 'Price'])
                        # Write updated rows
                        csv_writer.writerows(products)
                    
                else:
                    print("Invalid index!")
            else:
                print("No products available to update.")
            
            print('Closing cursor...')
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to update product:', ex)

# Leave this line here!
print('All done!')

# Leave this line here!

def add_courier():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()
            print('Inserting new record...')
            
            name = input("Enter the name of the new courier: ")
            phone = input("Enter the phone number of the new courier: ")
            
            # Insert a new record
            sql = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
            data_values = (name, phone)
            cursor.execute(sql, data_values)
            
            # Commit the record
            connection.commit()
            print('Record inserted successfully!')
            
            print('Selecting all records...')
            # Execute SQL query
            cursor.execute('SELECT name, phone FROM couriers')
            # Fetch all the rows into memory
            rows = cursor.fetchall()
        
            print('Displaying all records...')
            # Gets all rows from the result
            for row in rows:
                print(f'Name: {row[0]}, Phone: {row[1]}')
            
            print('Closing cursor...')
            # Closes the cursor so it will be unusable from this point
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to:', ex)
        
def view_couriers():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()
            
            print('Selecting all records...')
            # Execute SQL query
            cursor.execute('SELECT id, name, phone FROM couriers')
            # Fetch all the rows into memory
            rows = cursor.fetchall()
        
            if rows:
                print('Displaying all records...')
                # Gets all rows from the result
                for row in rows:
                    print(f'ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')
            else:
                print("No couriers available.")
            
            print('Closing cursor...')
            # Closes the cursor so it will be unusable from this point
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to:', ex)

# Leave this line here!
print('All done!')

def remove_courier():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()

            # Fetch all couriers from the database
            cursor.execute('SELECT id, name FROM couriers')
            couriers = cursor.fetchall()

            if couriers:
                print('Available Couriers:')
                for idx, courier in enumerate(couriers, start=1):
                    print(f"{idx}. {courier[1]}")

                courier_index = int(input("Enter the index of the courier you want to remove: ")) - 1

                if 0 <= courier_index < len(couriers):
                    courier_id = couriers[courier_index][0]

                    # Remove the selected courier from the database
                    cursor.execute("DELETE FROM couriers WHERE id = %s", (courier_id,))
                    connection.commit()

                    print("Courier removed successfully!")
                else:
                    print("Invalid index!")
            else:
                print("No couriers available to remove.")

            print('Closing cursor...')
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to remove courier:', ex)

# Leave this line here!
print('All done!')

# Leave this line here!
print('All done!')


        #item = int(input("Enter the index of the item you want to update? for example, coke 0, banana 1, etc"))
       # new_item = input("Enter the name of the new item?")
        #product_list[item] = new_item
        #print(f"{new_item} has been added to the list")
        
import pymysql

def place_order():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()
            print('Inserting new record...')
            
            # Get input from the user
            customer_name = input("Enter customer name: ")
            customer_address = input("Enter the customer address: ")
            customer_phone = input("Enter customer phone number: ")
            items = input("Enter the items you would like to order (separated by comma): ").split(',')
            courier_id = input("Enter the courier ID: ")
            status_id = input("Enter an id")
            # Set a default value for status_id
              # Assuming 'Preparing' status
            
            # Insert a new record
            sql = """
                INSERT INTO orders 
                (customer_name, customer_address, customer_phone, courier_id, status_id, items)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            items_str = ','.join(items)  # Convert list to comma-separated string
            data_values = (customer_name, customer_address, customer_phone, courier_id, status_id, items_str)
            
            # Execute the SQL query
            cursor.execute(sql, data_values)
            
            # Commit the record
            connection.commit()
            print('Order placed successfully!')
            
            # Prepare the order dictionary
            order = {
                'customer_name': customer_name,
                'customer_address': customer_address,
                'customer_phone': customer_phone,
                'courier_id': courier_id,
                'status_id': status_id,
                'items': items,
                
            }
            
            print('Closing cursor...')
            # Closes the cursor so it will be unusable from this point
            cursor.close()
            # The connection will automatically close here
            
            return order
    except Exception as ex:
        print('Failed to place order:', ex)
        return None

# Leave this line here!
print('All done!')

def remove_order():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()

            # Fetch all orders from the database
            cursor.execute('SELECT id, customer_name FROM orders')
            orders = cursor.fetchall()

            if orders:
                print('Available Orders:')
                for idx, order in enumerate(orders, start=1):
                    print(f"{idx}. {order[1]}")

                order_index = int(input("Enter the index of the order you want to remove: ")) - 1

                if 0 <= order_index < len(orders):
                    order_id = orders[order_index][0]

                    # Remove the selected order from the database
                    cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
                    connection.commit()

                    print("Order removed successfully!")
                else:
                    print("Invalid index!")
            else:
                print("No orders available to remove.")

            print('Closing cursor...')
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to remove order:', ex)


def load_orders():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()
            print('Selecting all records...')
            # Execute SQL query to select all orders
            cursor.execute('SELECT * FROM orders')
            # Fetch all the rows into memory
            rows = cursor.fetchall()
        
            if rows:
                print('Displaying all records...')
                # Display the orders
                for row in rows:
                    print(f"ID: {row[0]}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone: {row[3]}, Items IDs: {row[4]}, Courier ID: {row[5]}, Items: {row[6]}\n")
            else:
                print("No orders available.")
            
            print('Closing cursor...')
            # Closes the cursor so it will be unusable from this point
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to load orders:', ex)

# Leave this line here!
print('All done!')

def load_order_status():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()
            print('Selecting all records...')
            # Execute SQL query to select all order statuses
            cursor.execute('SELECT * FROM order_status')
            # Fetch all the rows into memory
            rows = cursor.fetchall()
        
            if rows:
                print('Displaying all records...')
                # Display the order statuses
                for row in rows:
                    print(f"ID: {row[0]}, Status: {row[1]}")
            else:
                print("No order statuses available.")
            
            print('Closing cursor...')
            # Closes the cursor so it will be unusable from this point
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to load order status:', ex)

# Leave this line here!
print('All done!')


# def place_order():
           # customer_name = input("Enter customer name: ")
           # customer_address = input("Enter the customer address: ")
           # customer_phone = input("Enter customer phone number: ")
           # customer_item = input("Enter the item you would like to order:")
           # customer_courier = input("Enter the courier name")
           # order = {
               # 'customer_name':customer_name,
               # 'customer_address':customer_address,
               # 'customer_phone':customer_phone,
               # 'customer_item':customer_item,
               # 'customer_courier':customer_courier,
               # 'status':'PREPARING'
           # }
            
           # orders.append(order)
           # print("Order placed successfully!")
            
def view_orders():
            if not orders:
                print("No orders available")
            else:
                print("Orders:")
                for order in orders:
                    print(order)
                    

def add_order_status():
    try:
        print('Opening connection...')
        # Establish a database connection
        with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        ) as connection:
            print('Opening cursor...')
            cursor = connection.cursor()
            print('Inserting new record...')
            
            # Get input from the user
            id = int(input("Enter the ID of the order: "))
            orderstatus = input("Enter the order status: ")
            
            # Insert a new record
            sql = """
                INSERT INTO order_status 
                (id, orderstatus)
                VALUES (%s, %s)
            """
            data_values = (id, orderstatus)
            cursor.execute(sql, data_values)
            
            # Commit the record
            connection.commit()
            print('Order status added successfully!')
            
            print('Closing cursor...')
            # Closes the cursor so it will be unusable from this point
            cursor.close()
            # The connection will automatically close here
    except Exception as ex:
        print('Failed to add order status:', ex)

# Leave this line here!
print('All done!')

 #def update_order_status():
   # print("Orders:")
   # for i, order in enumerate(orders):
    #    print(f"{i}. {order['customer_name']} - {order['status']}")
    # order_index = int(input("Enter the index of the order to update: "))
   # print("Order Status Options:")
   # for i, status in enumerate(order_status_list):
   #     print(f"{i}. {status}")
   # status_index = int(input("Enter the index of the new order status: "))
   # orders[order_index]['status'] = order_status_list[status_index]
   # print("Order status updated successfully!")
            
couriers_list = []

print("---Welcome to PRAN'S CAFE! See a list of options below---")


if __name__ == "__main__":
    
    while True:
        print("Welcome to PRAN'S CAFE! See a list of options below")
        print("1. Display the list of current products")
        print("2. Add a product to the list")
        print("3. Remove item")
        print("4. Update an item")
        print("5. Exit")
        print("6. Load courier list")
        print("7. Add a courier")
        print("8. Show orders")
        print("9. Show order status")
        print("10. Add a new order")
        print("11. Update order status")
        print("12. Establish database connection")
        print("13. This option isn't valid, l just dislike the number")
        print("14. Remove an order from the database.")
        print("15. Remove a courier from the database.")
        
        choice = input("Enter your choice: ")

        if choice == "2":
            add_product()

        
        elif choice == "1":
            display_products()
            #if product_list:
               # print("Current list:")
              #  for i, item in enumerate(product_list, 0):
                  #  print(f"{i}. {item}")
            # else:
                # print("The list is empty.")
                
        elif choice == "3":
            remove_product()
            # item = input("Enter item to remove from the list")
            # product_list.remove(item)3
            
           # print(f"{item} has been removed from the list.")
            
        elif choice == "4":
            update_product()
            
            
        elif choice == "6":
            view_couriers()
            # FIX THIS LATER , THIS IS TO DISPLAY COURIERS AND NUMBER
            # if courier_list:
               # print("Current list of couriers:")
               # for i, item in enumerate(courier_list,  start=1):
                  #  print(f"{i}.{item}")
                    
        elif choice == "7":
            add_courier()
            # courier = input("Enter the name of the courier to add to the list:")
            # courier_list.append(courier)
        
        elif choice == "8":
            load_orders()
                 # if orders:
               # print("Current list of orders")
               # for i, item in enumerate(orders, start=1 ):
                  #  print(f"{i}.{item}")
            # else:
                # print("Currently no orders")
            
        
        elif choice == "9":
             load_order_status()
            
            
        elif choice == "10":
            place_order()
        
        elif choice == "11":
            add_order_status()
            
            # Loop
            
        elif choice == "12":
            db_connection('x')
            print("You are establishing the connection")
            closeconnection_function('y')
        
        elif choice == "14":
            remove_order()
            
        elif choice == "15":
            remove_courier()
    
            
            
        elif choice == "5":
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
        
        []
        input("Press Enter to continue back to the menu...")  
    
    
    