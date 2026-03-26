#List to store the products
inventary = []
#Variable to control the menu loop
Menu = 1
#Function to control the errors in the input, it receives a prompt and a type, and returns the input converted to the specified type.
# If the conversion fails, it prints an error message and asks for the input again.
def errors_control (prompt, type=str):
    validar = "y"
    while validar:                
        try:
            return type(input(prompt))
        except ValueError:
            print(" Invalid input. Try again.\n")
#Function to add products to the inventory, it asks for the product name, price and quantity, and stores them in a dictionary
#This is added to the inventory list. It also asks if the user wants to add another product.
def add_product():
            continuar = "yes"
#The loop continues until the user answers "no" to the question of whether they want to add another product.
            while continuar != "no":
                print ("="*60)
#If the user enters an invalid input for the price or quantity, the error control function will handle it
#Ask for the input again until it is valid.
                product_name = errors_control("\nEnter the product name: ")
                product_price = errors_control("Enter the product price: ", float)
                producto_quantity = errors_control("Enter the product quantity: ", int)
#The product information is stored in a dictionary and added to the inventory list.
#After adding the product, the user is asked if they want to add another product, and the loop continues until they answer "no".
                products ={
                    "name": product_name,
                    "price": product_price,
                    "quantity": producto_quantity
                }
                inventary.append(products)
                continuar = input("\nDo you want to add another product? (yes, no): ").lower()
#Function to show the inventory, it checks if the inventory is empty and prints a message if it is.
#If there are products in the inventory, it iterates through the list and prints the name, price and quantity of each product in a formatted way.
def show_inventory():
    if not inventary:
        print("No purchases recorded.\n")
    for products in inventary:
         print(f"""\nProduct: {products['name']} 
Price: {products['price']} 
Quantity: {products['quantity']}""")
         print ("-"*60)
#Function to calculate the total value of the inventory, it checks if the inventory is empty and prints a message if it is.
#If there are products in the inventory, it iterates through the list and multiplies the price by the quantity of each product, adding the result to a total variable.
#Finally, it prints the total value of the inventory.

def Calculate_statistics ():
    if not inventary:
        print("No products registered.\n")
    total = 0
    for products in inventary:
        total += products['price'] * products['quantity']    
    return print(f"\nTotal inventory value: {total}\n")
#Welcome message

print("""
╔════════════════════════════════════════════════════════════╗
        WELCOME TO THE SALES RECORD RIWI STORE!!             
╚════════════════════════════════════════════════════════════╝
""")
#The main menu loop, it continues until the user chooses to exit by entering the option 4.
#Inside the loop, it tries to convert the user's input to an integer and checks which option was selected.
#If the input is not a valid number, it catches the ValueError and prints an error message.
while Menu:
    try:
        option = int(input(f"""{"-"*24} MAIN MENU {"-"*25}
1) 🍎 Enter Product
2) 🧾 Show inventory
3) 🔍 Calculate statistics 
4) 💀 Exit
{"="*60}
➤ """))
#Depending on the option selected, it calls the corresponding function to perform the desired action.
#If the user selects an option that is not available, it prints a message indicating that the option is not valid.
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
