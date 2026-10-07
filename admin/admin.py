from food.food_management import Food_Management
from table.table_management import Table_Management
from order.order_management import Order_Admin
from authentication.authentication import Authentication
from billing.admin_bill import Admin_Billing
from inventory.inventory import Inventory




class Admin_Menu:
    def admin_menu(self):
        while True:
            print("==============================================")
            print("*              Admin Dashboard               *")
            print("==============================================")
            print("1. Food Management")
            print("2. Table Management")
            print("3. Order Management")
            print("4. Inventory Management")
            print("5. Staff Management")
            print("6. Bill Management")
            print("7. Exit")
            choice=input("Enter Your Choice: ")
            if choice=="1":
                obj=Food_Management()
                obj.menu()
            elif choice=="2":
                obj=Table_Management()
                obj.menu()
            elif choice=="3":
                obj=Order_Admin()
                obj.menu()
            elif choice=="4":
                obj=Inventory()
                obj.menu()
            elif choice=="5":
                obj=Authentication()
                obj.menu()
            elif choice=="6":
                obj=Admin_Billing()
                obj.menu()
            elif choice=="7":
                print("Program Close")
                break
            else:
                print("Invalid Your Choice")