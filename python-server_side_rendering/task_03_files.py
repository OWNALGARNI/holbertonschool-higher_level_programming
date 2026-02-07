from flask import Flask, render_template, request
import json
import csv
from pathlib import Path
app = Flask(__name__)

path = Path(__file__).parent / "products.json"
path_csv = Path(__file__).parent / "products.csv"

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

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Check if source is valid
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read products from the appropriate source
    if source == 'json':
        products_list = read_products_json()
    else:
        products_list = read_products_csv()
    
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
