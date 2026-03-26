inventary = []
Menu = 1
def errors_control (prompt, type=str):
    while 9:               
        try:
            return type(input(prompt))
        except ValueError:
            print(" Invalid input. Try again.\n")
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
