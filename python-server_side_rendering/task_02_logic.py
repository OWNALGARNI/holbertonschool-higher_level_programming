from flask import Flask, render_template
import json
from pathlib import Path

app = Flask(__name__)
items_path = Path(__file__).parent / "items.json"

@app.route('/items')
def items():
    with open(items_path) as f:
        data = json.load(f)
        items_list = data["items"]
    return render_template('items.html', items=items_list)

