import requests
base_url = "https://fakestoreapi.com/"

products = requests.get(f"{base_url}products").json()
filtered = [product for product in products if product.get('price', 0) < 20]
print("Продукты с ценой <20:")
for product in filtered:
    print(f"{product['title']} {product['price']}")

categories = requests.get(f"{base_url}products/categories").json()
print("\nВсе категории")
for category in categories:
    print(category)

products = requests.get(f"{base_url}products/category/jewelery").json()
print("\nПродукты с категорией jewelery:")
for product in products:
    print(product["title"])

users = requests.get(f"{base_url}users").json()
print("\nВсе пользователи:")
for user in users:
    print(f"username: {user['username']}, name: {user['name']['firstname']} {user['name']['lastname']}")

user_data = {
    'address' :
        {
            'geolocation' :
                {
                    'lat': '-5',
                    'long': '-5'
                },
            'city': 'karaganda',
            'street': 'abai',
            'number': 322,
            'zip-code': '228'
        },
    'email': 'kazakhstan_rulit@mail.ru',
    'username': 'mickle_jordan',
    'password': 'qwerty123',
    'name':
        {
            'firstname': 'Azamat',
            'lastname': 'Nurgaliev'
        },
    'phone': '+77771234567'
}

response = requests.post(f"{base_url}users", json=user_data)
if response.status_code == 200 or response.status_code == 201:
    response_data = response.json()
    new_user = user_data.copy()
    new_user['id'] = response_data.get('id')
    print(f"\nNew user {new_user['username']} added")
else:
    print(response.status_code)