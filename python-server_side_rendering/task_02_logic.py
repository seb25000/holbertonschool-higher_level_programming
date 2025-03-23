from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the 0-index.html template."""
    return render_template('0-index.html')

@app.route('/items')
def items():
    """Renders the items.html template with items from items.json."""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items = data.get('items', [])  # Get the items list, default to empty list if not found
    except FileNotFoundError:
        items = []  # If the file doesn't exist, treat it as an empty list.
    
    return render_template('items.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)