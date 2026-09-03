cust_name = input("Customer Name: ")

product1 = input("Product 1: ")
price1 = input("Price: ")

product2 = input("Product 2: ")
price2 = input("Price: ")

product3 = input("Product 3: ")
price3 = input("Price: ")


discount = 0

try:
    price = [int(price) for price in [price1, price2, price3]]
    subtotal = sum(price)

    for price in price:
        if price >= 5000:
            discount = subtotal * 0.20
        elif price >= 3000:
            discount = subtotal * 0.10
        elif price >= 1000:
            discount = subtotal * 0.05

except ValueError:
    print("Error: Please enter valid integer prices.")
    exit()

final_total = subtotal - discount

print(f"Subtotal: {subtotal}")
print(f"Discount: {discount:.0f}")
print(f"Final Total: {final_total:.0f}")
