from admin.admin import Admin_Menu
from staff.order import Order_Staff
from admin.admin_authentication import Admin_Authentication
from authentication.authentication import Authentication


class Auth_Menu:
    def auth_menu(self):
            while True:
                print("============================================================")
                print("*                        Auth Menu                         *")
                print("============================================================")
                print("1. Sign In")
                print("2. Exit")
                choice=input("Enter Your Auth Choice: ")
                if choice=="1":
                    self.main_menu()
                elif choice=="2":
                    print("Program Close Successfully |")
                    break
                else:
                    print("Invalid Your Auth Choice |")
    def main_menu(self):
            while True:
                print("============================================================")
                print("*                     Auth Main-Menu                       *")
                print("============================================================")
                print("1. Admin Sign-in")
                print("2. Staff Sign-in")
                print("3. Exit")
                main_choice=input("Enter Auth Main-Menu Choice: ")
                if main_choice=="1":
                    obj=Admin_Authentication()
                    login=obj.admin_signin()
                    if login==True:
                        obj=Admin_Menu()
                        obj.admin_menu()
                elif main_choice=="2":
                    obj=Authentication()
                    login=obj.signin()
                    if login==True:
                        obj=Order_Staff()
                        obj.menu()
                elif main_choice=="3":
                    print("Prgram Close in Successfully.")
                    break
                else:
                    print("Invalid Your Auth Main-Menu Choice")