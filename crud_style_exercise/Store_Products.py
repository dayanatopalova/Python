
def create_product(item, price, quantity):
    return {"item": item,
            "price": price,
            "quantity": quantity,
            "total_price": price * quantity}

def input_products():
    products = []

    while True:
        name = input("Enter a product or 'stop': ")
        if name.lower() == "stop":
            break

        price = float(input("Enter the price of the item: "))
        quantity = int(input("Enter the quantity of the product: "))

        product = create_product(name, price, quantity)
        products.append(product)

    return products

def find_most_expensive_product(products):
    most_expensive = products[0]

    for product in products:
        if product["price"] > most_expensive["price"]:
            most_expensive = product

    return most_expensive

def products_above_50_eur(products):
    count = 0

    for product in products:
        if product["price"] > 50:
            count += 1

    return count

def total_inventory_value(products):
    total = 0
    for product in products:
        total += product["total_price"]

    return total

products = input_products()
result = find_most_expensive_product(products)
print(result)
print(f"Number of products with price higher than 50 EUR: {products_above_50_eur(products)}")
print(f"The total value of the inventory is: {total_inventory_value(products)}")