# PRAN'S CAFE

Welcome to PRAN'S CAFE! This program manages a cafe's inventory, orders, and couriers. It provides a user-friendly interface for performing various tasks such as adding products, placing orders, updating order status, and more.

#INTRODUCTION

'ntroduction

PRAN'S CAFE Management System is a Python-based program designed to assist cafe owners in managing their inventory, orders, and couriers quickly and efficiently. The system provides various functionalities such as adding, updating, and removing products, managing courier services, placing orders, and updating order statuses. You are also able to send your user input into a database, and a csv file too if you want!


#PROJECT BACKGROUND

This project was done to help us understand how to make a programme that can help a business to maintain a collection of products and couriers, and also keep track of orders.


## Setup

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install required packages:
    ```bash
    pip install pymysql python-dotenv
    ```
3. Create a `.env` file in the project directory with the following content:

mysql_host=localhost
mysql_user=root
mysql_pass=password
mysql_db=cafe_data

## HOW TO USE THIS PROGRAMME

#First, ensure the above steps are done correctly, then login to adminer on MySQL with http://localhost:8080/, login with details that are provided.


Run the program by executing `py Miniproject_Final.py` in the terminal. Follow the on-screen prompts to interact with the menu and perform various tasks. You will be prompted after each input to return to the main meny by pressing the 'Enter' key, unless you choose to exit the app. 


### Menu Options:

1. **Display the list of current products:** View the current list of available products.
2. **Add a product to the list:** Add a new product to the inventory.
3. **Remove item:** Remove a product from the inventory.
4. **Update an item:** Modify details of an existing product.
5. **Exit:** Exit the program.
6. **Load courier list:** Load the list of available couriers.
7. **Add a courier:** Add a new courier to the list.
8. **Show orders menu:** Display the current list of orders.
9. **Add a new order:** Place a new order.
10. **Update order status:** Update the status of an existing order.
11. **Establish database connection:** Connect to the MySQL database.

## What did i learn?

I learned about functions, how to link vscode and python into a database, and update it from vscode. also how to upload to github, and how to load, write and read to a CSV file.
That databases can be link , both together and with python and vscode.
How to check for errors, and unit testing.

using functions within dictionaries
