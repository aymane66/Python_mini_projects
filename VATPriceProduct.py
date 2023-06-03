price_before_tax = input("Price without tax: ")
category = input("Category: ")

try:
    price_before_tax = float(price_before_tax)

    print("----- Information: -----")
    print("Price before tax: ", price_before_tax)
    print("Category: ", category)

    if category.lower() == "a":
        print("Price after tax: ", price_before_tax + price_before_tax * 0.07)
    elif category.lower() == "b":
        print("Price after tax: ", price_before_tax + price_before_tax * 0.2)
    elif category.lower() == "c":
        print("Price after tax: ", price_before_tax + price_before_tax * 0.07)
    else:
        print("Invalid category! ")

except:
    print("Invalid price input")

