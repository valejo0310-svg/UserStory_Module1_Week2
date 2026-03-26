inventary = []
Menu = 1
def errors_control (prompt, type=str):
    while 9:               
        try:
            return type(input(prompt))
        except ValueError:
            print(" Invalid input. Try again.\n")
def add_product():
            continuar = "yes"
            while continuar != "no":
                print ("="*60)
                product_name = errors_control("\nEnter the product name: ")
                product_price = errors_control("Enter the product price: ", float)
                producto_quantity = errors_control("Enter the product quantity: ", int)
                products ={
                    "name": product_name,
                    "price": product_price,
                    "quantity": producto_quantity
                }
                inventary.append(products)
                continuar = input("\nDo you want to add another product? (yes, no): ").lower()
def show_inventory():
    if not inventary:
        print("No purchases recorded.\n")
    for products in inventary:
         print(f"""\nProduct: {products['name']} 
Price: {products['price']} 
Quantity: {products['quantity']}""")
         print ("-"*60)
print("""
╔════════════════════════════════════════════════════════════╗
        WELCOME TO THE SALES RECORD RIWI STORE!!             
╚════════════════════════════════════════════════════════════╝
""")

while Menu:
    try:
        option = int(input(f"""{"-"*24} MAIN MENU {"-"*25}
1) 🍎 Enter Product
2) 🧾 Show inventory
3) 🔍 Calculate statistics 
4) 💀 Exit
{"="*60}
➤ """))

        if option == 1:
            add_product()

        elif option == 2:
            show_inventory()
        elif option == 3:
            Calculate_statistics()       

        elif option == 4:
            print("Exiting...")
            Menu = 0

        else:
            print("Option not available.\n")

    except ValueError:
        print("❌ Invalid number.\n")
