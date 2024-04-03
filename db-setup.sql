DROP DATABASE IF EXISTS cafe_data;
CREATE DATABASE cafe_data;
USE cafe_data;
# Orders table
CREATE TABLE maindata (
    id int NOT NULL AUTO_INCREMENT,
    customer_name varchar(100) NOT NULL,
    customer_address varchar(255) NOT NULL,
    customer_phone char(11) NOT NULL,
    courier_id int(10) NOT NULL,
    status_id int(2) NOT NULL,
    items_ids varchar(100) NOT NULL,
    PRIMARY KEY (id)
    #FOREIGN KEY (courier_id) REFERENCES couriers(id),
    #FOREIGN KEY (status_id) REFERENCES order_status(id)
);
# Order status table
CREATE TABLE order_status (
    id int NOT NULL AUTO_INCREMENT,
    order_status varchar(25) NOT NULL,
);
# Couriers table
CREATE TABLE couriers (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    phone char(11) NOT NULL,
    PRIMARY KEY (id)
);
# Products table
CREATE TABLE products (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    price float(11) NOT NULL,
    PRIMARY KEY (id));