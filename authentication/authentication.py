from admin.admin_authentication import Admin_Authentication
import stdiomask
import datetime
import uuid
import json


class Authentication:
    def signup(self):
        while True:
            name=input("Enter Your Name: ").strip()
            if name.replace(" ","").isalpha():
                break
            else:
                with open("logs/war.log",'a') as name_error:
                    name_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Sighup Staff - Name - Alpha Value Only\n") 
                print("Only Alphabet")
        while True:
            email=input("Enter Your Email ID: ")
            if "@" in email and ".com" in email:
                break
            else:
                with open("logs/war.log",'a') as email_error:
                    email_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Sighup Staff - Email - Invalid Email\n") 
                print("Invalid Email ID")
        while True:
            try:
                password=stdiomask.getpass("Enter Password: ",mask="*")
                if password.isalnum() and  len(password)>=5:
                    break
                else:
                    with open("logs/war.log",'a') as password_six_error:
                        password_six_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Sighup Staff - Password - Password must be at leasts 6 Digits\n") 
                    print("Password must be at leasts 6 Digits")
            except ValueError:
                with open("logs/war.log",'a') as password_intger_error:
                    password_intger_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Sighup Staff - Password - Alpha Number Value Only\n") 
                print("Alpha Number Value Only")
                return
        uid="S" + str(uuid.uuid4())[:9]
        signup={
            "id":uid,
            "name":name,
            "email":email,
            "password":password,
        }
        try:
            with open("database/staff.json",'r') as file:
                data=json.load(file)
        except:
            data=[]
        for user in data:
            if user["email"]==email:
                with open("logs/war.log",'a') as email_already:
                    email_already.write(f"[{str(datetime.datetime.now())}] [WARNING] - Sighup Staff - Email Already Signup\n") 
                print("Email Already Signup")
                return
        data.append(signup)
        with open("database/staff.json",'w') as file:
            json.dump(data,file,indent=4)
        with open("logs/staff.log",'a') as log:
            log.write(f"[{str(datetime.datetime.now())}] [INFO]- Signup Successful: {email}\n")
        print("Signup Successful")
    def signin(self):
        try:
            while True:
                email=input("Enter Email ID & ID: ")
                if email:
                    break
                else:
                    with open("logs/war.log",'a') as sign_error:
                        sign_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Signin Staff - Email ID - Invalid Email ID\n")
                    print("Invalid Email ID")
            while True:
                try:
                    password=stdiomask.getpass("Enter Password: ",mask="*")
                    if password.isalnum():
                        break
                    else:
                        with open("logs/war.log",'a') as password_error_alpha:
                            password_error_alpha.write(f"[{str(datetime.datetime.now())}] [WARNING] Signin Staff - Password - Alpha Number Value Only\n")
                        print("Alpha Number Value Only")
                except ValueError:
                    with open("logs/war.log",'a') as password_error:
                        password_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Signin Staff - Password - Alpha Number Value Only\n")
                    print("Alpha Value Value Only")
                    return
            with open("database/staff.json",'r') as file:
                data=json.load(file)
            for user in data:
                if (user["email"]==email or user["id"]==email) and user["password"]==password:
                    with open("logs/staff.log",'a') as log:
                        log.write(f"[{str(datetime.datetime.now())}] [INFO]- Signin Successful: {email}\n")
                    print(f"{email}")
                    print("Staff")
                    print("Signin Successful")
                    return True
            else:
                with open("logs/war.log",'a') as log:
                    log.write(f"[{str(datetime.datetime.now())}] [WARNING]- Invalid Email and Password: {email}\n")
                print("Invalid Email and Password")
                return False
        except FileNotFoundError:
            with open("logs/error.log",'a') as sign_file:
                sign_file.write(f"[{str(datetime.datetime.now())}] [ERROR] - Staff Signin - File is not found\n")
            print("Data is not found")
            return False
    def view_menu(self):
        try:
            with open("database/staff.json",'r') as veiw_menu_file:
                veiw_menu_data=json.load(veiw_menu_file)
                print("=============================================================================================================")
                print("*                                                   View Menu                                               *")
                print("=============================================================================================================\n")
                count=0
                for i in veiw_menu_data:
                    count+=1
                    print("Staff ID                        Staff Name                       Email ID                            Password")
                    print("-------------------------------------------------------------------------------------------------------------")
                    print(str(count).ljust(2),str(i["id"]).ljust(30),str(i["name"]).ljust(27),str(i["email"]).ljust(40),str(i["password"]))
                    print("-------------------------------------------------------------------------------------------------------------")
                if count==0:
                    with open("logs/war.log",'a') as staff_error:
                        staff_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - View Staff - staff.json: Staff Data is not found\n")
                    print("Staff Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as view_menu_error:
                view_menu_error.write(f"[{str(datetime.datetime.now())}] [ERROR] - View Menu - staff.json: File is not found\n")
            print("Data is not found")
            return
    def update(self):
        try:
            with open("database/staff.json",'r') as file:
                update_data=json.load(file)
            while True:
                email_id=input("Enter Email ID & ID : ")
                if email_id:
                    break
                else:
                    with open("logs/war.log",'a') as invalid_email_error:
                        invalid_email_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Staff - Email ID or ID - Invalid Email ID & ID\n")
                    print("Invalid Email ID & ID")
            for update in update_data:
                if update["email"]==email_id or update["id"]==email_id:
                    while True:
                        print("================================")
                        print("--------- Update Menu ----------")
                        print("================================")
                        print("1. Name Update")
                        print("2. Password Update")
                        print("3. Back")
                        print("4. Exit")
                        update_choice=input("Enter Update Choice: ")
                        if update_choice=="1":
                            while True:
                                new_name=input("Enter New Name: ").strip()
                                if len(new_name)>2:
                                    if new_name.replace(" ","").isalpha():
                                        break
                                    else:
                                        with open("logs/error.log",'a') as update_name_error:
                                            update_name_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Staff - New Name - Alpha Value Only\n")
                                        print("Alpha Value Only")
                                else:
                                    with open("logs/war.log",'a') as new_name_allow:
                                        new_name_allow.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Staff - New Name - Maximum 3 Character Allow\n")
                                    print("Maximum 3 Character Allow")
                            update["name"]=new_name
                            with open("database/staff.json",'w') as name:
                                json.dump(update_data,name,indent=4)
                            with open("logs/staff.log",'a') as name_log:
                                name_log.write(f"[{str(datetime.datetime.now())}] [INFO]- Name Update Successful {email_id}\n")
                            print("Name Update Successful")
                        elif update_choice=="2":
                            while True:
                                try:
                                    new_password=input("Enter New Password: ")
                                    if len(new_password)>5:
                                        if new_password.isalnum():
                                            break
                                        else:
                                            with open("logs/war.log",'a') as new_password_alpha:
                                                new_password_alpha.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Staff - New Password - Alpha Number Value Only\n")
                                            print("Alpha Number Value Only")
                                    else:
                                        with open("logs/war.log",'a') as password_greater:
                                            password_greater.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Staff - New Password - Password must be at leasts 6 Digit\n")
                                        print("Password must be at leasts 6 Digits")
                                except ValueError:
                                    with open("logs/error.log",'a') as new_password_error:
                                        new_password_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Staff - New Password - Alpha Number Value Only\n")
                                    print("Alpha Number Value Only")
                            update["password"]=new_password
                            with open("database/staff.json",'w') as password:
                                json.dump(update_data,password,indent=4)
                            with open("logs/staff.log",'a') as password_log:
                                password_log.write(f"[{str(datetime.datetime.now())}] [INFO]- Password Update Successful {email_id}\n")
                            print("Password Update Successful")
                        elif update_choice=="3":
                            with open("logs/staff.log",'a') as signin:
                                signin.write(f"[{str(datetime.datetime.now())}] [INFO] - Program Back Successful {email_id}\n")
                            print("Program Back Successful")
                            self.main_menu()
                        elif update_choice=="4":
                            with open("logs/staff.log",'a') as exit:
                                exit.write(f"[{str(datetime.datetime.now())}] [INFO] - EXIT Program Close Successfully {email_id}\n")
                            print("Restaurant Management System Close Successfully.")
                            break
                        else:
                            with open("logs/war.log",'a') as update_staff_choice:
                                update_staff_choice.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Staff - Update - Invalid Your Update Choice\n")
                            print("Invalid Your Update Choice")
                else:
                    with open("logs/war.log",'a') as invalid_email:
                        invalid_email.write(f"[{str(datetime.datetime.now())}] [WARNING] - Invalid Email ID {email_id}\n")
                    print("Invalid Email ID")
                    return
            else:
                with open("logs/war.log",'a') as data_not_found:
                    data_not_found.write(f"[{str(datetime.datetime.now())}] [WARNING] - Staff Update - Data is no found\n")
                print("Data is Not found")
                return
        except FileNotFoundError:
            with open("logs/error.log",'a') as update_staff:
                update_staff.write(f"[{str(datetime.datetime.now())}] [ERROR] Update Staff - staff.json: File  id not found\n")
            print("Data Not Found")
            return
    def delete(self):
        try:
            with open("database/staff.json",'r') as delete:
                delete_data=json.load(delete)
                while True:
                    staff_email_id=input("Enter Email ID & ID: ")
                    if staff_email_id:
                        break
                    else:
                        with open("logs/war.log",'a') as delete_error_email:
                            delete_error_email.write(f"[{str(datetime.datetime.now())}] [WARNING] - Delete Staff - Email ID & ID - Invalid Email ID & ID\n")
                        print("Invalid Email ID & ID")
                for data in delete_data:
                    if data["email"]==staff_email_id or data["id"]==staff_email_id:
                        print("========================")
                        print("----- Staff Delete -----")
                        print("========================")
                        print("1. Staff Delete")
                        print("2. Staff Delete Cancel")
                        print("3. Back")
                        print("4. Exit")
                        yes_no=input("Staff Delete Please Reply Yes and No: ")
                        if yes_no=="1":
                            delete_data.remove(data)
                            with open("database/staff.json",'w') as delete_staff:
                                json.dump(delete_data,delete_staff,indent=4)
                            with open("logs/staff.log",'a') as file:
                                file.write(f"[{str(datetime.datetime.now())}] [INFO] - Staff Deleted Successfully {staff_email_id}\n")
                            print("Staff Deleted Successfully.")
                        elif yes_no=="2":
                            with open("logs/staff.log",'a') as cancel:
                                cancel.write(f"[{str(datetime.datetime.now())}] [INFO] -  Staff Delete Cancel {staff_email_id}\n")
                            print("Staff Delete Cancel")
                            break 
                        elif yes_no=="3":
                            with open("logs/staff.log",'a') as back:
                                back.write(f"[{str(datetime.datetime.now())}] [INFO] - Program Back Successfully {staff_email_id}\n")
                            print("Program Back Successful")
                            self.main_menu()
                        elif yes_no=="4":
                            with open("logs/error.log",'a') as delete_error:
                                delete_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Delete Staff - Restaurant Management System Program Close Successfully.\n")
                            print("Restaurant Management System Program Close Successfully.")
                            break
                        else:
                            with open("logs/war.log",'a') as delete_choice:
                                delete_choice.write(f"[{str(datetime.datetime.now())}] [WARNING] - Delete Staff - Delete - Invalid Your Delete Choice\n")
                            print("Invalid Your Delete Choice")
                else:
                    with open("logs/war.log",'a') as invalid:
                        invalid.write(f"[{str(datetime.datetime.now())}] [WARNING] Invalid Email ID {staff_email_id}\n")
                    print("Invalid Email ID")
        except FileNotFoundError:
            with open("logs/error.log",'a') as file_not_found:
                file_not_found.write(f"[{str(datetime.datetime.now())}] [ERROR] Delete Staff: staff.json: File is not found\n")
            print("Data is not found")
            return
    def auth_menu(self):
        while True:
            print("--------------- Authenticaton Menu ---------------")
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
            print("--------------- Auth Main-Menu ---------------")
            print("1. Admin Sign-in")
            print("2. Staff Sign-in")
            print("3. Exit")
            main_choice=input("Enter Auth Main-Menu Choice: ")
            if main_choice=="1":
                obj=Admin_Authentication()
                obj.admin_signin()
            elif main_choice=="2":
                self.signin()
            elif main_choice=="3":
                print("Prgram Close in Successfully.")
                break
            else:
                print("Invalid Your Auth Main-Menu Choice")
    def menu(self):
        while True:
            print("==========================================")
            print("*                Staff Menu              *")
            print("==========================================")
            print("1. Sign-Up Staff")
            print("2. View Staff")
            print("3. Update Staff")
            print("4. Delete Staff")
            print("5. Back")
            choice=input("Enter Your Choice: ")
            if choice=="1":
                self.signup()
            elif choice=="2":
                self.view_menu()
            elif choice=="3":
                self.update()
            elif choice=="4":
                self.delete()
            elif choice=="5":
                print("Program Back Successful")
                break
            else:
                print("Invalid Your Choice")
# obj=Authentication()
# obj.menu()