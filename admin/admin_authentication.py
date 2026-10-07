import json
import stdiomask
import datetime
import uuid


class Admin_Authentication:
    def admin_signup(self):
        print("============================================================")
        print("*                       Admin Signup                       *")
        print("============================================================")
        admin_id="A" + str(uuid.uuid4())[:9]
        admin_name=input("Enter Your Name: ")
        admin_email=input("Enter Your Email ID: ")
        admin_password=input("Enter Password: ")
        admin_confirm_password=input("Enter Confirm Password: ")
        if admin_password==admin_confirm_password:
            pass
        else:
            print("Invalid Password Not Match")
            return
        admin={
            "admin_id":admin_id,
            "admin_name":admin_name,
            "admin_email_id":admin_email,
            "admin_password":admin_password
        }
        try:
            with open("database/admin.json",'r') as admin_sign:
                admin_data=json.load(admin_sign)
        except FileNotFoundError:
            admin_data=[]
        admin_data.append(admin)
        with open("database/admin.json",'w') as admin_sighup:
            json.dump(admin_data,admin_sighup,indent=4)
        print("Signup Successful")
    def admin_signin(self):
        print("============================================================")
        print("*                       Admin Signin                       *")
        print("============================================================")
        admin_signin_email_id=input("Enter Admin Email ID & Admin ID: ")
        admin_signin_password=stdiomask.getpass("Enter Admin Password: ",mask="*")
        with open("database/admin.json",'r') as file:
            admin_info=json.load(file)
        for admin_detail in admin_info:
            if (admin_detail["admin_email_id"]==admin_signin_email_id or admin_detail["admin_id"]==admin_signin_email_id) and admin_detail["admin_password"]==admin_signin_password:
                with open("logs/admin.log",'a') as admin:
                    admin.write(f"[{str(datetime.datetime.now())}] [INFO] - Admin Signin Successful\n")
                print(f"{admin_signin_email_id}")
                print("admin")
                print("Admin Signin Successful |")
                return True
            with open("logs/admin.log",'a') as admin:
                admin.write(f"[{str(datetime.datetime.now())}] [WARNING] - Invalid Email and Password\n")
            print("Invalid email id and password")
            return False
    def menu(self):
        while True:
            print("============================================================")
            print("*                          Menu                            *")
            print("============================================================") 
            print("1. Sign-up")
            print("2. Sign-in")
            print("3. Exit")
            choice=input("Enter Your Choice: ")
            if choice=="1":
                self.admin_signup()
            elif choice=="2":
                self.admin_signin()
            elif choice=="3":
                print("Menu Close Successful")
                break
            else:
                print("Invalid Your Choice")
# obj=Admin_Authentication()
# obj.menu()
