# Menu class keeps the data of category, name, portion and price of product.
class Menu:
    def __init__(self, category, name, portion, price):
        self.category = category
        self.name = name
        self.portion = portion
        self.price = price

    # Menu class has a function for ordered products. Returns the information of the ordered product.
    def buy(self):
        return [self.name, self.portion, self.price]


# Validation of the Input
def validation(choose, list):
    if len(list) < choose or choose <= 0 or choose == " ":
        return False
    return True


# Checkout UI, Shows that the all orders.
def checkout(sellings):
    print("\n")

    total = 0  # Total is the total cost of the order.

    # Order list UI
    for i in sellings:
        print(i[0], end=(40 - len(i[0]))*" ")
        print(i[1], end=(15 - len(i[1]))*" ")
        print(i[2])

        number = i[2][1:]
        total += float(number)

    # Total UI
    total = round(total, 2)
    print(65*"-")
    print("Total", end=50*" ")
    print("$"+str(total))


# Control Panel UI, it is shown after last step of an order.
# 1 for new order, 2 for finishing the order
def control_panel(sellings):
    print("\n")

    print("Control Panel: ")
    print("1. Add New")
    print("2. Checkout")

    option = int(
        input("\nPlease select an operation (enter integer number of the option): "))
    if option == 1:
        main()  # For new order, main function is called
    elif option == 2:
        # For finishing the order, checkoput function is called with sellings parameter
        checkout(sellings)
    else:
        print("Choose a valid option")


# It is a function for add the order to sellings list.
def add(product_name, portion, menu):
    for i in menu:
        # Controls name and portion, returns buy function of the object.
        if i.name == product_name and i.portion == portion:
            return i.buy()


# Portions UI, it is shown after select the product name.
def portions(product_name, menu, sellings):
    print("\n")

    print(f"{product_name} Portions:")

    counter = 1  # Created for UI element, [1. Xyz, 2. Abc, 3. Dam, ...]
    portionList = []  # keeps the data of portion names.
    for i in menu:
        # Controls the portion whether is it written to be an option.
        if i.portion not in portionList and i.name == product_name:
            print(f"{counter}. {i.portion}")
            portionList.append(i.portion)
            counter += 1

    while True:
        # Portion choosing
        portion = int(
            input("\nPlease select product portion (enter integer number of the option): "))

        if validation(portion, portionList):
            # Adds the selected product to the sellings list.
            sellings.append(add(product_name, portionList[portion - 1], menu))
            # Shows the Control Panel UI.
            control_panel(sellings)
            break
        else:
            print("Choose a valid option")


# Product UI, it is shown after select the catagory.
def products(category_name, menu, sellings):
    print("\n")

    print(f"Products in {category_name}:")

    counter = 1  # Created for UI element, [1. Xyz, 2. Abc, 3. Dam, ...]
    productList = []  # keeps the data of product names.
    for i in menu:
        # Controls the product whether is it written to be an option.
        if i.name not in productList and i.category == category_name:
            print(f"{counter}. {i.name}")
            productList.append(i.name)
            counter += 1

    while True:
        # Product choosing
        product = int(
            input("\nPlease select product name (enter integer number of the option): "))

        if validation(product, productList):
            # Shows the portion UI according to chosen product.
            portions(productList[product - 1], menu, sellings)
            break
        else:
            print("Choose a valid option")


# File operations are done here. Retruns menu as an object list.
def file_operations():
    file = open("menu.txt", "r")  # File open in read mode

    menuList = []
    file.readline()  # For the first line, it is an empty line.
    for i in file:
        # String line split according to the "; " characters, splitLine is a list.
        splitLine = i.split("; ")

        # menu object is created for all products.
        menu = Menu(splitLine[0], splitLine[1],
                    splitLine[2], splitLine[3].split("\n")[0])
        menuList.append(menu)  # Menu objects are appended to menuList list.

    file.close()  # File close
    return menuList


# Main Screen:
def main():
    print("\n")

    menu = file_operations()  # menu = menuList

    counter = 1  # Created for UI element, [1. Xyz, 2. Abc, 3. Dam, ...]
    categoryList = []  # keeps the data of category names.
    print("Product Categories:")
    for i in menu:
        # Controls the category whether is it written to be an option.
        if i.category not in categoryList:
            print(f"{counter}. {i.category}")
            categoryList.append(i.category)
            counter += 1

    while True:
        # Catagory choosing
        category = int(
            input("\nPlease select product category (enter integer number of the option): "))

        if validation(category, categoryList):
            # Shows the product UI according to chosen catagory.
            products(categoryList[category - 1], menu, sellings)
            break
        else:
            print("Choose a valid option")


if __name__ == "__main__":
    # Creating an empty list when the program has started, it keeps the data of ordered products.
    sellings = []
    main()
