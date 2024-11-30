from flask import Flask, request, jsonify

app = Flask(__name__)

products = []  # List to store products
@app.route("/")
def home():
    return "Home Page"
@app.route('/products', methods=['POST'])
def create_product():
    """Handles the creation of a new product."""
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Invalid data. 'name' and 'price' are required."}), 400
    
    product_id = len(products) + 1
    product = {
        "id": product_id,
        "name": data['name'],
        "price": data['price']
    }
    products.append(product)
    return jsonify({"message": "Product created successfully.", "product": product}), 201

if __name__ == '__main__':
    app.run(debug=True)