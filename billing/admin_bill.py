import json
from datetime import datetime

class Admin_Billing:
    def view_all_bills(self):
        try:
            with open("database/bill.json",'r') as view_all_bills_file:
                view_all_bills_data=json.load(view_all_bills_file)
                print("\n=========================================================")
                print("                     View All Bill                       ")
                print("=========================================================")
                count=0
                for bill in view_all_bills_data:
                    count+=1
                    print("Bill ID          : ",bill["bill_id"])
                    print("Customer Name    : ",bill["customer_name"])
                    print("Table ID         : ",bill["table_id"])
                    for item in bill["order_items"]:
                        print("Category         : ", item["category"])
                        print("Food Name        : ", item["food_name"])
                        print("Size             : ", item["size"])
                        print("Price            : ", "₹" + str(item["price"]))
                        print("Quantity         : ", item["quantity"])
                        print("Total Amount     : ", "₹" + str(item["total_amount"]))
                        print("Discount         : ",str(bill["discount"]) + "%")
                        print("GST              : ", bill["gst"])
                    print("Grand Total      : ", "₹" + str(bill["total_amount"]))
                    print("Payment Method   : ",bill["payment_method"])
                    print("Payment Status   : ",bill["payment_status"])
                    print("Date             : ",bill["date"])
                    print("Time             : ",bill["time"])
                    print("________________________________________________________")
                if count==0:
                    with open("logs/war.log",'a') as view_error_bill:
                        view_error_bill.write(f"[{str(datetime.now())}] [WARNING] - View All Bills - bill.json: Bill Data is not found\n")
                    print("Bill Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as view_error:
                view_error.write(f"[{str(datetime.now())}] [ERROR] - View All Bills - bill.json: File is not found\n")
            print("Data is not found")
            return
    def search_bill(self):
        try:
            with open("database/bill.json",'r') as search_bill_file:
                search_bill_data=json.load(search_bill_file)
                print("\n=========================================================")
                print("                      Search  Bill                       ")
                print("=========================================================")
                count=0
                bill_id=input("Enter Bill ID: ")
                for search in search_bill_data:
                    if search["bill_id"]==bill_id:
                        count+=1
                        print("Bill ID         : ",search["bill_id"])
                        print("Customer Name   : ",search["customer_name"])
                        print("Table ID        : ",search["table_id"])
                        for item in search["order_items"]:
                            print("Category         : ", item["category"])
                            print("Food Name        : ", item["food_name"])
                            print("Size             : ", item["size"])
                            print("Price            : ", "₹" + str(item["price"]))
                            print("Quantity         : ", item["quantity"])
                            print("Total Amount     : ", "₹" + str(item["total_amount"]))
                            print("Discount         : ",str(search["discount"]) + "%")
                            print("GST              : ", search["gst"])
                        print("Grand Total      : ", "₹" + str(search["total_amount"]))
                        print("Payment Method  : ",search["payment_method"])
                        print("Payment Status  : ",search["payment_status"])
                        print("Date            : ",search["date"])
                        print("Time            : ",search["time"])
                        print("________________________________________________________")
                if count==0:
                    with open("logs/war.log",'a') as search_bill_error:
                        search_bill_error.write(f"[{str(datetime.now())}] [WARNING] - Search Bill - Bill Data is not found\n")
                    print("Bill Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as search_error:
                search_error.write(f"[{str(datetime.now())}] [ERROR] - Search Bill - bill.json: File is not found\n")
            print("Data is not found")
            return
    def update_bill(self):
        try:
            with open("database/bill.json",'r') as update_bill_file:
                update_bill_data=json.load(update_bill_file)
                print("\n=========================================================")
                print("                      Update  Bill                       ")
                print("=========================================================")
                count=0
                while True:
                    bill_id=input("Enter Bill ID: ")
                    if bill_id.isalnum():
                        break
                    else:
                        with open("logs/error.log",'a') as update_error:
                            update_error.write(f"[{str(datetime.now())}] [WARNING] - Update Bill - Bill ID - Alpha Number Value Only\n")
                        print("Alpha Number Value Only")
                for update in update_bill_data:
                    if update["bill_id"]==bill_id:
                        count+=1
                        print("=========================================================")
                        print("                      Update  Menu                       ")
                        print("=========================================================")
                        print("1. Payment Method")
                        print("2. Payment Status")
                        print("3. Back")
                        print("4. Exit")
                        update_choice=input("Enter Your Update Choice: ")
                        if update_choice=="1":
                            print("=========================================================")
                            print("                 Update Payment Method                   ")
                            print("=========================================================")
                            print("1. Cash")
                            print("2. Phone Pay")
                            print("3. UPI")
                            update_payment_method_choice=input("Enter Update Payment Method Choice: ")
                            if update_payment_method_choice=="1":
                                update["payment_method"]="Cash"
                                with open("database/bill.json",'w') as cash:
                                    json.dump(update_bill_data,cash,indent=4)
                                with open("logs/bill.log",'a') as update_cash_error:
                                    update_cash_error.write(f"[{str(datetime.now())}] [INFO] - Update Bill - Cash Payment Method Update Successful\n")
                                print("Cash Payment Method Update Successful")
                            elif update_payment_method_choice=="2":
                                update["payment_method"]="Phone Pay"
                                with open("database/bill.json",'w') as phone_pay:
                                    json.dump(update_bill_data,phone_pay,indent=4)
                                with open("logs/bill.log",'a') as update_phone_pay_error:
                                    update_phone_pay_error.write(f"[{str(datetime.now())}] [INFO] - Update Bill - Phone Pay Payment Method Update Successful\n")
                                print("Phone Pay Payment Method Update Successful")
                            elif update_payment_method_choice=="3":
                                update["payment_method"]="UPI"
                                with open("database/bill.json",'w') as upi:
                                    json.dump(update_bill_data,upi,indent=4)
                                with open("logs/bill.log",'a') as update_cash_upi:
                                    update_cash_upi.write(f"[{str(datetime.now())}] [INFO] - Update Bill - UPI Payment Method Update Successful\n")
                                print("UPI Payment Method Update Successful")
                            else:
                                print("Invalid Your Update Payment Method Choice: ")
                        elif update_choice=="2":
                            print("=========================================================")
                            print("                 Update Payment Status                   ")
                            print("=========================================================")
                            print("1. Complete")
                            print("2. Pending")
                            print("3. Cancelled")
                            update_payment_status_choice=input("Enter Update Payment Status Choice: ")
                            if update_payment_status_choice=="1":
                                update["payment_status"]="Complete"
                                with open("database/bill.json",'w') as complete:
                                    json.dump(update_bill_data,complete,indent=4)
                                with open("logs/bill.log",'a') as complete_error:
                                    complete_error.write(f"[{str(datetime.now())}] [INFO] - Update Bill - Payment Status Complete Update Successful\n")
                                print("Payment Status Complete Update Sucessfull")
                            elif update_payment_status_choice=="2":
                                update["payment_status"]="Pending"
                                with open("database/bill.json",'w') as pending:
                                    json.dump(update_bill_data,pending,indent=4)
                                with open("logs/bill.log",'a') as pending_error:
                                    pending_error.write(f"[{str(datetime.now())}] [INFO] - Update Bill - Payment Status Pending Update Successful\n")
                                print("Payment Status Pending Update Successful")
                            elif update_payment_status_choice=="3":
                                update["payment_status"]="Cancelled"
                                with open("database/bill.json",'w') as cancelled:
                                    json.dump(update_bill_data,cancelled,indent=4)
                                with open("logs/bill.log",'a') as cancelled_error:
                                    cancelled_error.write(f"[{str(datetime.now())}] [INFO] - Update Bill - Payment Status Cancelled Update Successful\n")
                                print("Payment Status Cancelled Update Successful")
                            else:
                                with open("logs/war.log",'a') as payment_invalid:
                                    payment_invalid.write(f"[{str(datetime.now())}] [WARNING] - Update Bill - Update Payment Status - Invalid Your Update Payment Status Choice\n")
                                print("Invalid Your Update Payment Status Choice")
                        elif update_choice=="3":
                            print("Program Back In Successful")
                            with open("logs/bill.log",'a') as update_back:
                                update_back.write(f"[{str(datetime.now())}] [INFO] - Update Bill - Progran Back in Successful.\n")
                            self.update_bill()
                        elif update_choice=="4":
                            with open("logs/bill.log",'a') as update_exit:
                                update_exit.write(f"[{str(datetime.now())}] [INFO] - Update Bill - Restaurant Management System - Update Bill - Close Successful\n")
                            print("Restaurant Management System - Update Bill - Close Successful.")
                            break
                        else:
                            with open("logs/war.log",'a') as bill_choice:
                                bill_choice.write(f"[{str(datetime.now())}] [WARNING] - Update Bill - Update Bill - Invalid Your Update Bill Choice\n")
                            print("Invalid Your Update Bill Choice")
                        break
                if count==0:
                    with open("logs/war.log",'a') as update_error_bill:
                        update_error_bill.write(f"[{str(datetime.now())}] [WARNING] - Update Bill - bill.json Bill Data is not found\n")
                    print("Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as update_bill_error:
                update_bill_error.write(f"[{str(datetime.now())}] [ERROR] - Update Bill - bill.json File is not found\n")
            print("Data is not found")
            return
    def delete_bill(self):
        try:
            with open("database/bill.json",'r') as delete_bill_file:
                delete_bill_data=json.load(delete_bill_file)
                print("\n=========================================================")
                print("                      Delete  Bill                       ")
                print("=========================================================")
                while True:
                    bill_id=input("Enter Bill ID: ")
                    if bill_id.isalnum():
                        break
                    else:
                        with open("logs/error.log",'a') as delete_error:
                            delete_error.write(f"[{str(datetime.now())}] [WARNING] - Delete Bill - Bill ID - Alpha Number Value Only\n")
                        print("Alpha Number Value Only")
                for delete in delete_bill_data:
                    if delete["bill_id"]==bill_id:
                        print("\n=========================================================")
                        print("                  Confirm Delete Bill                    ")
                        print("=========================================================")
                        print("1. Confirm Delete Bill")
                        print("2. Cancel Delete Bill")
                        print("3. Back")
                        print("4. Exit")
                        confirm_choice=input("Enter Your Confirm Bill Choice: ")
                        if confirm_choice=="1":
                            delete_bill_data.remove(delete)
                            with open("database/bill.json",'w') as confirm:
                                json.dump(delete_bill_data,confirm,indent=4)
                            with open("logs/bill.log",'a') as update_cash_error:
                                update_cash_error.write(f"[{str(datetime.now())}] [INFO] - Delete Bill - Bill Delete Successful\n")
                            print("Bill Delete Successful")
                        elif confirm_choice=="2":
                            with open("logs/bill.log",'a') as delete_cancel:
                                delete_cancel.write(f"[{str(datetime.now())}] [INFO] - Delete Bill - Bill Cancel Successful\n")
                            print("Bill Cancel Successful")
                        elif confirm_choice=="3":
                            print("Program Back Successful")
                            with open("logs/bill.log",'a') as delete_back:
                                delete_back.write(f"[{str(datetime.now())}] [INFO] - Delete Bill - Program Back in Successful\n")
                            self.delete_bill()
                        elif confirm_choice=="4":
                            with open("logs/bill.log",'a') as delete_exit:
                                delete_exit.write(f"[{str(datetime.now())}] [INFO] - Delete Bill - Restaurant Management System Close Successful.\n")
                            print("Restaurant Management System Close Successful. ")
                            break
                        else:
                            with open("logs/war.log",'a') as confirm_error:
                                confirm_error.write(f"[{str(datetime.now())}] [WARNING] - Delete Bill - Confirm Bill - Invalid Your Confirm Bill Choice\n")
                            print("Invalid Your Confirm Bill Choice")
                else:
                    with open("logs/war.log",'a') as delete_bill_error:
                        delete_bill_error.write(f"[{str(datetime.now())}] [WARNING] - Delete Bill - bill.json: Bill Data is not found\n")
                    print("Bill Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as delete_file:
                delete_file.write(f"[{str(datetime.now())}] [ERROR] - Delete Bill - bill.json: File is not found\n")
            print("Data is not found")
            return
    def menu(self):
        while True:
            print("=========================================================")
            print("                       Bill Menu                         ")
            print("=========================================================")
            print("1. View All Bills")
            print("2. Search Bill")
            print("3. Update Bill")
            print("4. Delete Bill")
            print("5. Back")
            choice=input("Enter Your Choice: ")
            if choice=="1":
                self.view_all_bills()
            elif choice=="2":
                self.search_bill()
            elif choice=="3":
                self.update_bill()
            elif choice=="4":
                self.delete_bill()
            elif choice=="5":
                print("Program Close Successful")
                break
            else:
                print("Invalid Your Choice")
