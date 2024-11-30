from flask import Flask, request, jsonify
from product import Product

app = Flask(__name__)

products = []  # List to store products
@app.route("/")
def home():
    return "Home Page"
@app.route('/products', methods=['POST', 'GET'])
def products_handler():
    if request.method == 'POST':
        data = request.get_json()
        if not data or not all(field in data for field in ['name', 'description', 'price']):
            return jsonify({'error': 'Invalid product data'}), 400

        # Validate data (e.g., price > 0)
        new_product = Product(data['name'], data['description'], data['price'])
        products.append(new_product)
        return jsonify(new_product._dict_), 201

    elif request.method == 'GET':
       return jsonify([product._dict_ for product in products])

if __name__ == '__main__':
    app.run(debug=True)
