import json
import uuid
import datetime


class Bill_Management:
    def generate_bill(self):
        try:
            with open("database/order.json",'r') as generate_file:
                generate_bill_data=json.load(generate_file)
                count=0
                order_id=input("Enter Order ID: ")
                for order in generate_bill_data:
                    if order["order_id"]==order_id:
                        count+=1
                        if order["order_status"]=="Complete":
                            bill_id="B" + str(uuid.uuid4())[:3]
                            try:
                                with open("database/bill.json",'r') as bill_error:
                                    bill_generate_data=json.load(bill_error)
                            except FileNotFoundError:
                                bill_generate_data=[]
                            for data_bill in bill_generate_data:
                                if data_bill["order_id"]==order_id:
                                    print("Bill Already Generated")
                                    print("Bill ID:", data_bill["bill_id"])
                                    return
                            print("============================================================")
                            print("*                      Bill Generate                       *")
                            print("============================================================\n")
                            print("\n---------------------- Payment Method ----------------------")
                            print("1. Cash")
                            print("2. UPI")
                            print("3. Phone Pay")
                            payment_status="Paid"
                            payment_method_choice=input("Enter Your Payment Method Choice: ")
                            if payment_method_choice=="1":
                                payment_method="Cash"
                                with open("logs/bill.log",'a') as cash_error:
                                    cash_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Generate Bill - Payment Method Cash Successful\n")
                                print("Payment Method Cash Successful")
                            elif payment_method_choice=="2":
                                payment_method="UPI"
                                with open("logs/bill.log",'a') as upi_error:
                                    upi_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Generate Bill - Payment Method UPI Successful\n")
                                print("Payment Method UPI Successful")
                            elif payment_method_choice=="3":
                                payment_method="Phone Pay"
                                with open("logs/bill.log",'a') as phone_pay_error:
                                    phone_pay_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Generate Bill - Payment Method Phone Pays Successful\n")
                                print("Payment Method Phone Pay Successful")
                            else:
                                with open("logs/war.log",'a') as payment:
                                    payment.write(f"[{str(datetime.datetime.now())}] [WARNING] - Generate Bill - Payment Method - Invalid Your Payment Method Choice\n")
                                print("Invalid Your Payment Method Choice")
                                return
                            discount=10
                            discount_amount=order["total_amount"]*discount/100
                            after_discount=order["total_amount"]-discount_amount
                            gst="5%"
                            gst_amount=after_discount*5/100
                            total_amount=after_discount+gst_amount
                            bill={
                                "bill_id":bill_id,
                                "order_id":order["order_id"],
                                "customer_id":order["customer_id"],
                                "customer_name":order["customer_name"],
                                "table_id":order["table_id"],
                                "order_items":order["order_items"],
                                "discount":discount,
                                "gst":gst,
                                "total_amount":total_amount,
                                "payment_method":payment_method,
                                "payment_status":payment_status,
                                "order_status":order["order_status"],
                                "date":order["date"],
                                "time":order["time"]
                            }
                            try:
                                with open("database/bill.json",'r') as bill_file:
                                    bill_data=json.load(bill_file)
                            except FileNotFoundError:
                                bill_data=[]
                            bill_data.append(bill)
                            with open("database/bill.json",'w') as bill_file:
                                json.dump(bill_data,bill_file,indent=4)
                            with open("logs/bill.log",'a') as bill_generate_error:
                                bill_generate_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Generate Bill - Bill Generate Successful\n")
                            print("Bill Generate Successful")
                            return
                if count==0:
                    with open("logs/war.log",'a') as bill_data_not_found:
                        bill_data_not_found.write(f"[{str(datetime.datetime.now())}] [WARNING] -  Generate Bill - order.json: Order Data is not found\n")
                    print("Order Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as generate_bill_not_found_error:
                generate_bill_not_found_error.write(f"[{str(datetime.datetime.now())}] [ERROR] Generate Bill - order.json: File is not found\n") 
            print("Data is not found")
            return
    def view_bill(self):
        try:
            with open("database/bill.json",'r') as view_bill_file:
                view_bill_data=json.load(view_bill_file)
                count=0
                for view in view_bill_data:
                    count+=1
                    print("\n============================================================")
                    print("*                         View Menu                          *")
                    print("============================================================\n")
                    print("Order ID         : ",view["order_id"])
                    print("Customer ID      : ",view["customer_id"])
                    print("Customer Name    : ",view["customer_name"])
                    print("Table ID         : ",view["table_id"])
                    for item in view["order_items"]:
                        print("Category         : ",item["category"])
                        print("Food Name        : ",item["food_name"])
                        print("Size             : ",item["size"])
                        print("Price            : ","₹" + str(item["price"]))
                        print("Quantity         : ",item["quantity"])
                        print("Total Amount     : ","₹" + str(item["total_amount"]))
                    print("Discount         : ",str(view["discount"]) + "%")
                    print("GST              : ",view["gst"])
                    print("Total Amount     : ", "₹" + str(view["total_amount"]))
                    print("Payment Method   : ",view["payment_method"])
                    print("Payment Status   : ",view["payment_status"])
                    print("Order Status     : ",view["order_status"])
                    print("Date             : ",view["date"])
                    print("Time             : ",view["time"])
                    print("________________________________________________________")
                if count==0:
                    with open("logs/war.log",'a') as bill_not:
                        bill_not.write(f"[{str(datetime.datetime.now())}] [WARNING] - View Bill - bill.json Bill Data is not found\n")
                    print("Bill Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as view_bill_error:
                view_bill_error.write(f"[{str(datetime.datetime.now())}] [ERROR] - View Bill - bill.json: File is not found\n")
            print("Data is not found")
            return
    def bill_history(self):
        try:
            with open("database/bill.json",'r') as bill_history_file:
                bill_history_data=json.load(bill_history_file)
                count=0
                for bill in bill_history_data:
                    count+=1
                    print(f"-------------------- Bill{count} --------------------")
                    print("Bill ID          : ",bill["bill_id"])
                    print("Order ID         : ",bill["order_id"])
                    print("Customer Name    : ",bill["customer_name"])
                    for item in bill["order_items"]:
                        print("Food Name        : ",item["food_name"])
                        print("Size             : ",item["size"])
                        print("Quantity         : ",item["quantity"])
                        print("Total Amount     : ","₹" + str(item["total_amount"]))
                    print("Discount         : ",str(bill["discount"]) + "%")
                    print("GST              : ",bill["gst"])
                    print("Total Amount     : ",bill["total_amount"])
                    print("Payment Method   : ",bill["payment_method"])
                    print("Payment Status   : ",bill["payment_status"])
                    print("Date             : ",bill["date"])
                    print("Time             : ",bill["time"])
                    print("________________________________________________________")
                if count==0:
                    with open("logs/war.log",'a') as bill_history_not:
                        bill_history_not.write(f"[{str(datetime.datetime.now())}] [WARNING] - Bill History - bill.json: Bill Data is not found\n")
                    print("Bill Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as bill_history_not_data:
                bill_history_not_data.write(f"[{str(datetime.datetime.now())}] [ERROR] - Bill History - bill.json: File is not found\n")
            print("Data is not found")
            return
    def menu(self):
        while True:
            print("==========================================")
            print("*                Bill Menu               *")
            print("==========================================")
            print("1. Generate Bill")
            print("2. View Bill")
            print("3. Bill History")
            print("4. Back")
            bill_choice=input("Enter Bill Choice: ")
            if bill_choice=="1":
                self.generate_bill()
            elif bill_choice=="2":
                self.view_bill()
            elif bill_choice=="3":
                self.bill_history()
            elif bill_choice=="4":
                print("Program Back Successful")
                break
            else:
                print("Invalid Your Bill Choice")
