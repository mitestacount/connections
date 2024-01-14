"""
This script create a database test
"""
import sqlite3

# Function to create a SQLite database and tables
def create_database():
    # Connect to SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Create user_products table to represent the relationship between users and products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_products (
            user_id INTEGER,
            product_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (user_id),
            FOREIGN KEY (product_id) REFERENCES products (product_id),
            PRIMARY KEY (user_id, product_id)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to insert sample data into the tables
def insert_sample_data():
    # Connect to SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Insert sample users
    cursor.executemany('INSERT INTO users (username, email) VALUES (?, ?)',
                       [('user1', 'user1@example.com'),
                        ('user2', 'user2@example.com')])

    # Insert sample products
    cursor.executemany('INSERT INTO products (product_name, price) VALUES (?, ?)',
                       [('ProductA', 19.99),
                        ('ProductB', 29.99),
                        ('ProductC', 9.99)])

    # Insert sample user-product relationships
    cursor.executemany('INSERT INTO user_products (user_id, product_id) VALUES (?, ?)',
                       [(1, 1),  # user1 wants ProductA
                        (1, 2),  # user1 wants ProductB
                        (2, 2),  # user2 wants ProductB
                        (2, 3)])  # user2 wants ProductC

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Create the database and tables
create_database()

# Insert sample data
insert_sample_data()
