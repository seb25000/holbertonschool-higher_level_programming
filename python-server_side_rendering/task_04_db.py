from flask import Flask, render_template, request, jsonify
import csv
import sqlite3
import json

import os

app = Flask(__name__)

def read_csv_data(filename):
    """Reads data from a CSV file and returns it as a list of dictionaries."""
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def read_json_data(filename):
    """Reads data from a JSON file and returns it as a list of dictionaries."""
    try:
        with open(filename, 'r') as jsonfile:
            data = json.load(jsonfile)
        return data
    except FileNotFoundError:
        return []  # Handle the case where the file doesn't exist
    except json.JSONDecodeError:
        return []  # Handle the case where the JSON is invalid

def read_sql_data(db_name):
    """Reads data from a SQLite database and returns it as a list of dictionaries."""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()

        # Convert rows to a list of dictionaries
        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        return data
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None  # Or raise the exception if you prefer


@app.route('/')
def display_products():
    """Displays product data based on the source query parameter."""
    source = request.args.get('source', 'json')  # Default to JSON if no source is provided

    if source == 'json':
        products = read_json_data('products.json')
        if not products:  # Check for empty data (e.g., file not found, invalid JSON)
            return render_template('error.html', message="JSON file not found or invalid.")
    elif source == 'csv':
        products = read_csv_data('products.csv')
        if not products: # Check for empty data (e.g., file not found)
            return render_template('error.html', message="CSV file not found or empty.")
    elif source == 'sql':
        products = read_sql_data('products.db')
        if products is None:  # Check for database error
            return render_template('error.html', message="Database error occurred.")
        if not products: # Check for empty data (e.g., no products in DB)
            return render_template('error.html', message="No products found in the database.")
    else:
        return render_template('error.html', message="Wrong source.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':

    #Create the database and populate it

    def create_database():
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        conn.commit()
        conn.close()

    create_database()
    app.run(debug=True)