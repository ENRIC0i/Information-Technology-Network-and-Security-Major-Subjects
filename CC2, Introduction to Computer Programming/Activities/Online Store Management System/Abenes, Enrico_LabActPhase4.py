# Programmed by: Abenes, Enrico O.
# Program Title: Final Project - Phase 4
# Program Date: June 23, 2023

from datetime import datetime, timedelta
from collections import defaultdict

inventoryFile = "Inventory.txt"
orderFile = "Sales.txt"
inventory = []
orders = []

def mainMenu():
    while True:
        print("______________________________")
        print("Online Store Management System")
        print(" ")
        print("1: Manage Products")
        print("2: Current Inventory")
        print("3: Track Inventory")
        print("4: Process Order")
        print("5: Generate Sales Report")
        print("6: Exit")
        print(" ")
        choice = input("Enter(1-6): ")
        print("______________________________")

        if choice == '1':
            manageProducts()
        elif choice == '2':
            currentInventory()
        elif choice == '3':
            searchProduct()
        elif choice == '4':
            processOrder()
        elif choice == '5':
            salesReport()
        elif choice == '6':
            print("Thank You")
            break
        else:
            print(" Invalid ")
            print("Try Again")

def manageProducts():
    while True:
        print("______________________________")
        print("      Managing Products       ")
        print(" ")
        print("1: Add Product")
        print("2: Update Product")
        print("3: Remove Product")
        print("4: Back")
        print(" ")
        choice = input("Enter(1-4): ")
        print("______________________________")

        if choice == '1':
            addProduct()
        elif choice == '2':
            updateProduct()
        elif choice == '3':
            removeProduct()
        elif choice == '4':
            mainMenu()
        else:
            print(" Invalid ")
            print("Try Again")

def loadInventory():
    try:
        with open(inventoryFile, "r") as file:
            for line in file:
                values = line.strip().split(",")
                if len(values) == 3:
                    name, price, quantity = values
                    product = {
                        "name": name,
                        "price": float(price),
                        "quantity": int(quantity)
                    }
                    inventory.append(product)
    except FileNotFoundError:
        with open(inventoryFile, "w") as file:
            pass

def loadOrders():
    try:
        with open(orderFile, "r") as file:
            for line in file:
                values = line.strip().split(",")
                if len(values) == 3:
                    name, quantity, date = values
                    order = {
                        "name": name,
                        "quantity": int(quantity),
                        "date": date
                    }
                    orders.append(order)
    except FileNotFoundError:
        with open(orderFile, "w") as file:
            pass

def saveInventory():
    with open(inventoryFile, "w") as file:
        for product in inventory:
            line = f"{product['name']},{product['price']},{product['quantity']}\n"
            file.write(line)

def saveOrders():
    with open(orderFile, "w") as file:
        for order in orders:
            line = f"{order['name']},{order['quantity']}\n"
            file.write(line)

def addProduct():
    print("Adding Product")
    print(" ")
    name = input("Product Name: ")

    while True:
        price = input("Price: ")
        if not price.isdigit():
            print(" ")
            print("     Invalid     ")
            print("Enter Valid Price")
            print(" ")
        else:
            price = float(price)
            break

    while True:
        quantity = input("Quantity: ")
        if not quantity.isdigit():
            print(" ")
            print("      Invalid      ")
            print("Enter Valid Quantity")
            print(" ")
        else:
            quantity = int(quantity)
            break

    product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(product)
    print("Product Added")
    print("______________________________")
    saveInventory()

def updateProduct():
    print("Updating Product")
    print(" ")
    name = input("Product Name: ")
    for product in inventory:
        if product['name'] == name:

            while True:
                newPrice = input("New Price: ")
                if not newPrice.isdigit():
                    print(" ")
                    print("     Invalid     ")
                    print("Enter Valid Price")
                    print(" ")
                else:
                    newPrice = float(newPrice)
                    break

            while True:
                newQuantity = input("New Quantity: ")
                if not newQuantity.isdigit():
                    print(" ")
                    print("      Invalid      ")
                    print("Enter Valid Quantity")
                    print(" ")
                else:
                    newQuantity = int(newQuantity)
                    break

            product['price'] = newPrice
            product['quantity'] = newQuantity
            print("Product Updated")
            print("______________________________")
            saveInventory()
            return
    print("Product Not Found")
    print("______________________________")

def removeProduct():
    print("Removing Product")
    print(" ")
    name = input("Product Name: ")
    for product in inventory:
        if product['name'] == name:
            inventory.remove(product)
            print("Product Removed")
            print("______________________________")
            saveInventory()
            return
    print("Product Not Found")
    print("______________________________")

def currentInventory():
    print("Current Inventory")
    print(" ")
    totalAmount = 0
    for product in inventory:
        prices = product['price'] * (product['quantity'])
        totalAmount += prices
        print(f"Product Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}, Overall Price: ₱ {prices}")
        print(" ")
    print(f"Total Price: ₱ {totalAmount}")
    print("______________________________")

def searchProduct():
    print("Tracking Inventory")
    print(" ")
    print("1: Search by Product Name")
    print("2: Search by Price Range")
    print("3: Search by Quantity Range")
    print("4: Back")
    print(" ")
    choice = input("Enter(1-4): ")
    print("______________________________")

    if choice == '1':
        name = input("Enter Product Name: ")
        searchbyName(name)
    elif choice == '2':
        minPrice = float(input("Enter Minimum Price: "))
        maxPrice = float(input("Enter Maximum Price: "))
        searchbyPriceRange(minPrice, maxPrice)
    elif choice == '3':
        minQuantity = int(input("Enter Minimum Quantity: "))
        maxQuantity = int(input("Enter Maximum Quantity: "))
        searchbyQuantityRange(minQuantity, maxQuantity)
    elif choice == '4':
        mainMenu()
    else:
        print(" Invalid ")
        print("Try Again")
        searchProduct()

def searchbyName(name):
    print("Searching bu Product Name")
    print(" ")
    found = False
    for product in inventory:
        if product['name'] == name:
            print("Product Found")
            print(f"Name: {product['name']}, Price: ₱ {product['price']}, Quantity: {product['quantity']}")
            print(" ")
            found = True
            break
    if not found:
        print("Product Not Found")
    print("______________________________")

def searchbyPriceRange(minPrice, maxPrice):
    print(" ")
    found = False
    for product in inventory:
        if minPrice <= product['price'] <= maxPrice:
            print(f"Product Name: {product['name']}, Price: ₱ {product['price']}, Quantity: {product['quantity']}")
            found = True
    if not found:
        print("No Products Found in the Price Range")
    print("______________________________")

def searchbyQuantityRange(minQuantity, maxQuantity):
    print("Searching by Quantity Range")
    print(" ")
    found = False
    for product in inventory:
        if minQuantity <= product['quantity'] <= maxQuantity:
            print(f"Product Name: {product['name']}, Price: ₱ {product['price']}, Quantity: {product['quantity']}")
            found = True
    if not found:
        print("No Products Found in the Quantity Range")
    print("______________________________")

def processOrder():
    print("Processing Order")
    print(" ")
    name = input("Product Name: ")

    while True:
        quantity = input("Enter order quantity: ")
        if not quantity.isdigit():
            print(" ")
            print("      Invalid      ")
            print("Enter Valid Quantity")
            print(" ")
        else:
            quantity = int(quantity)
            break

    orderDate = datetime.now().strftime("%Y-%m-%d")
    productFound = False

    for product in inventory:
        if product['name'] == name:
            if product['quantity'] >= quantity:
                product['quantity'] -= quantity
                productFound = True
                break
            else:
                print("Not Enough Stock")
                print("______________________________")
                return

    if productFound:
        print("Order Processed")
        print("______________________________")
        order = {
            "name": name,
            "quantity": quantity,
            "date": orderDate
        }
        orders.append(order)
        saveOrders()
        saveInventory()
        inventory.clear()
        loadInventory()
    else:
        print("Product Not Found")
        print("______________________________")

def getTopSellingProduct():
    productSales = defaultdict(lambda: {'quantity': 0, 'sales': 0})

    for order in orders:
        for product in inventory:
            if product['name'] == order['name']:
                sales = product['price'] * order['quantity']
                productSales[product['name']]['quantity'] += order['quantity']
                productSales[product['name']]['sales'] += sales

    topProduct = None
    maxSales = 0

    for product, salesData in productSales.items():
        if salesData['sales'] > maxSales:
            maxSales = salesData['sales']
            topProduct = {'name': product, 'quantity': salesData['quantity'], 'sales': salesData['sales']}

    return topProduct

def getSalesByPeriod(startDate, endDate):
    totalSales = 0
    for order in orders:
        orderDate = datetime.strptime(order['date'], "%Y-%m-%d")
        if startDate <= orderDate <= endDate:
            for product in inventory:
                if product['name'] == order['name']:
                    sales = product['price'] * order['quantity']
                    totalSales += sales
    return totalSales

def salesReport():
    print("Top Selling Product:")
    topProduct = getTopSellingProduct()
    if topProduct:
        print("Product Name: ", topProduct['name'])
        print("Quantity Sold: ", topProduct['quantity'])
        print("Total Sales: ₱ ", topProduct['sales'])
        print(" ")
    else:
        print("No Sales Available")
        print(" ")
    print("Generating Sales Report")
    print(" ")
    print("1: Daily Sales Report")
    print("2: Weekly Sales Report")
    print("3: Monthly Sales Report")
    print("4: Back")
    print(" ")
    choice = input("Enter(1-4): ")
    print("______________________________")

    if choice == '1':
        dailysalesReport()
    elif choice == '2':
        weeklysalesReport()
    elif choice == '3':
        monthlysalesReport()
    elif choice == '4':
        mainMenu()
    else:
        print(" Invalid ")
        print("Try Again")
        salesReport()

def dailysalesReport():
    dateStr = input("Enter Date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(dateStr, "%Y-%m-%d")
        startDate = date
        endDate = date
        totalSales = getSalesByPeriod(startDate, endDate)
        print(f"Date Sales Report ({dateStr})")

        print("Products Sold:")
        for order in orders:
            orderDate = datetime.strptime(order['date'], "%Y-%m-%d")
            if startDate <= orderDate <= endDate:
                for product in inventory:
                    if product['name'] == order['name']:
                        sales = product['price'] * order['quantity']
                        print(f"Product Name: {product['name']}, Quantity Sold: {order['quantity']}, Sales: ₱ {sales}")

        print(" ")
        print("Total Sales: ₱ ", totalSales)
        print("______________________________")
    except ValueError:
        print("Invalid Date Format")
        print("______________________________")
    salesReport()

def weeklysalesReport():
    weekStr = input("Enter Date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(weekStr, "%Y-%m-%d")
        startDate = date - timedelta(days=date.weekday())
        endDate = startDate + timedelta(days=6)
        totalSales = getSalesByPeriod(startDate, endDate)
        print(f"Weekly Sales Report ({startDate.strftime('%Y-%m-%d')} to {endDate.strftime('%Y-%m-%d')})")

        print("Products Sold:")
        for order in orders:
            orderDate = datetime.strptime(order['date'], "%Y-%m-%d")
            if startDate <= orderDate <= endDate:
                for product in inventory:
                    if product['name'] == order['name']:
                        sales = product['price'] * order['quantity']
                        print(f"Product Name: {product['name']}, Quantity Sold: {order['quantity']}, Sales: ₱ {sales}")

        print("Total Sales: ₱ ", totalSales)
        print("______________________________")
    except ValueError:
        print("Invalid Date Format")
        print("______________________________")
    salesReport()

def monthlysalesReport():
    monthStr = input("Enter Date (YYYY-MM): ")
    try:
        startDate = datetime.strptime(monthStr, "%Y-%m")
        endDate = startDate.replace(day=28) + timedelta(days=4)
        totalSales = getSalesByPeriod(startDate, endDate)
        print(f"Monthly Sales Report ({startDate.strftime('%Y-%m')} to {endDate.strftime('%Y-%m-%d')})")

        print("Products Sold:")
        for order in orders:
            orderDate = datetime.strptime(order['date'], "%Y-%m-%d")
            if startDate <= orderDate <= endDate:
                for product in inventory:
                    if product['name'] == order['name']:
                        sales = product['price'] * order['quantity']
                        print(f"Product Name: {product['name']}, Quantity Sold: {order['quantity']}, Sales: ₱ {sales}")

        print("Total Sales: ₱ ", totalSales)
        print("______________________________")
    except ValueError:
        print("Invalid Date Format")
        print("______________________________")
    salesReport()

loadInventory()
loadOrders()
mainMenu()