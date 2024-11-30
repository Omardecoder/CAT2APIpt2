import requests

base_url = 'http://localhost:5000'  # Replace with your server address

# Create a new product
new_product = {'name': 'T-Shirt', 'description': 'Cool T-Shirt', 'price': 19.99}
response = requests.post(f'{base_url}/products', json=new_product)

if response.status_code == 201:
    print(f"Product created: {response.json()}")
else:
    print(f"Error creating product: {response.text}")

# Get all products
response = requests.get(f'{base_url}/products')

if response.status_code == 200:
    print("Products:")
    for product in response.json():
        print(product)
else:
    print(f"Error getting products: {response.text}")
