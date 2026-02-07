from flask import Flask, render_template, request
import json
import csv
import sqlite3
from pathlib import Path

app = Flask(__name__)

path = Path(__file__).parent / "products.json"
path_csv = Path(__file__).parent / "products.csv"
path_db = Path(__file__).parent / "products.db"

def read_products_json():
    with open(path) as f:
        data = json.load(f)
        return data
    
def read_products_csv():
    products = []
    with open(path_csv) as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = {
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            }
            products.append(product)
    return products

def read_products_sql():
    products = []
    try:
        conn = sqlite3.connect(path_db)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            product = {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            }
            products.append(product)
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Check if source is valid
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read products from the appropriate source
    if source == 'json':
        products_list = read_products_json()
    elif source == 'csv':
        products_list = read_products_csv()
    else:  # sql
        products_list = read_products_sql()
        if products_list is None:
            return render_template('product_display.html', error="Database error")
    
    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            products_list = [p for p in products_list if p['id'] == product_id]
            if not products_list:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
