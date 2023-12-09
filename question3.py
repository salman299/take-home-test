import sqlite3
from prettytable import PrettyTable

def create_tables(conn):
    """
    Create Category and ProductSold tables

    Parameters:
    - conn: Database connection
    """
    # Create Category Table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Category (
            CategoryId TEXT PRIMARY KEY,
            Category TEXT
        )
    ''')
    # Create ProductSold Table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS ProductSold (
            ProductName TEXT,
            CategoryId TEXT,
            Year INTEGER,
            QuantityPurchased INTEGER,
            PRIMARY KEY (ProductName, Year),
            FOREIGN KEY (CategoryId) REFERENCES CategoryTable(CategoryId)
        )
    ''')

    conn.commit()

def insert_data(conn):
    """
    Insert Dummy Data into the Category and ProductSold tables

    Parameters:
    - conn: Database connection
    """
    conn.executemany('''
        INSERT OR IGNORE INTO Category (CategoryId, Category)
        VALUES (?, ?)
    ''', [
        ('001', 'Sports and travel'),
        ('002', 'Produce'),
        ('003', 'Dairy'),
        ('004', 'Baking'),
        ('005', 'Home and lifestyle'),
        ('006', 'Health and beauty')
    ])

    # Insert data into ProductTable
    conn.executemany('''
        INSERT OR IGNORE INTO ProductSold (ProductName, Year, CategoryId, QuantityPurchased)
        VALUES (?, ?, ?, ?)
    ''', [
        ('Protein Powder', 2022, '001', 400),
        ('Energy Drink', 2020, '001', 834),
        ('Potato', 2021, '002', 30130),
        ('Cake Mix', 2020, '004', 720),
        ('Flour',  2021, '004', 39091),
        ('Brownie Mix', 2021, '004', 2131),
        ('Grapes', 2020, '002', 59000),
        ('Skimmed Milk', 2021, '003', 300000),
        ('Yogurt', 2020, '003', 98700),
        ('Baking Powder', 2020, '004', 5000),
        ('Light Bulbs', 2022, '005', 900),
        ('Bowl', 2021, '005', 210),
        ('Hand Soap', 2021, '006', 89211),
        ('Lotion', 2020, '006', 100),
        ('Shampoo', 2020, '006', 10070),
        ('Tomato', 2021, '002', 653)
    ])

def execute_and_print_query(conn):
    """
    Execute and print query results in the table
    """
    # Runnig the Query
    res = conn.execute('''
        SELECT c.CategoryId as Category_Id, c.Category AS Category, p.Year AS Year, SUM(p.QuantityPurchased) AS TotalQuantityPurchased
        FROM ProductSold p
        JOIN Category c ON p.CategoryId = c.CategoryId
        GROUP BY c.Category, p.Year
        ORDER BY c.Category, p.Year;
    ''')

    # Fetch all the results
    results = res.fetchall()

    table = PrettyTable(['Category_Id', 'Category', 'Year', 'TotalQuantity'], align="l")
    for row in results:
        table.add_row(row)

    print(table)

def main():
    """
    - Create dummy database, insert tables, and dummy data
    - Run Query for finding 
    """
    # Create database if it doesn't exist
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")

    create_tables(conn)
    insert_data(conn)
    execute_and_print_query(conn)

    conn.close()

if __name__ == '__main__':
    main()
