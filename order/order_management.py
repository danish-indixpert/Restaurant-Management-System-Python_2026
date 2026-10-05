import json
import datetime


class Order_Admin:
    def view_all_order(self):
        count=0
        try:
            with open("database/order.json",'r') as file:
                order_data=json.load(file)
            print("===========================================================")
            print("*                    View All Orders                      *")
            print("===========================================================")
            for i in order_data:
                count+=1
                print(f"\n=========================== Orders,{count} ==============================")
                print("Order ID         : ",i["order_id"])
                print("Customer ID      : ",i["customer_id"])
                print("Customer Name    : ",i["customer_name"])
                print("Table ID         : ",i["table_id"])
                for item in i["order_items"]:
                    print("Category         : ", item["category"])
                    print("Food Name        : ", item["food_name"])
                    print("Size             : ", item["size"])
                    print("Price            : ", "₹" + str(item["price"]))
                    print("Quantity         : ", item["quantity"])
                    print("Total Amount     : ", "₹" + str(item["total_amount"]))
                print("Grand Total      : ", "₹" + str(i["total_amount"]))
                print("Payment Method   : ",i["payment_method"])
                print("Payment Status   : ",i["payment_status"])
                print("Order Status     : ",i["order_status"])
                print("Date             : ",i["date"])
                print("Time             : ",i["time"])
                print("_______________________________________________________________________________")
        except FileNotFoundError:
            with open("logs/error.log",'a') as file_not_found:
                file_not_found.write(f"[{str(datetime.datetime.now())}] [ERROR] - View All Order - order.json: File is not found\n")
            print("Orders Data is not found")
            return    
    def search_order(self):
        print("===========================================================")
        print("*                       Search Order                      *")
        print("===========================================================\n")
        try:
            with open("database/order.json",'r') as update_order:
                search_order_data=json.load(update_order)
                while True:
                    order_id=input("Enter Order ID: ")
                    if order_id:
                        break
                    else:
                        with open("logs/war.log",'a') as search_order:
                            search_order.write(f"[{str(datetime.datetime.now())}] [WARNING] - Search Order - Order ID - Invalid Order ID\n")
                        print("Invalid Order Id")
                for i in search_order_data:
                    if i["order_id"]==order_id:
                        print("\n============================== Order Details ==============================")
                        print("Order ID         : ",i["order_id"])
                        print("Customer ID      : ",i["customer_id"])
                        print("Customer Name    : ",i["customer_name"])
                        print("Table ID         : ",i["table_id"])
                        for item in i["order_items"]:
                            print("Category         : ", item["category"])
                            print("Food Name        : ", item["food_name"])
                            print("Size             : ", item["size"])
                            print("Price            : ", "₹" + str(item["price"]))
                            print("Quantity         : ", item["quantity"])
                            print("Total Amount     : ", "₹" + str(item["total_amount"]))
                        print("Grand Total      : ", "₹" + str(i["total_amount"]))
                        print("Payment Method   : ",i["payment_method"])
                        print("Payment Status   : ",i["payment_status"])
                        print("Order Status     : ",i["order_status"])
                        print("Date             : ",i["date"])
                        print("Time             : ",i["time"])
                        print("________________________________________________________")
                        break
                else:
                    with open("logs/war.log",'a') as search_file_error:
                        search_file_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Search Order - order.json: Data is not found\n")
                    print("Order ID is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as file_not_found:
                file_not_found.write(f"[{str(datetime.datetime.now())}] [ERROR] - Update Order - order.json: File is not found\n")
            print("Data is Not found")
            return
    def sales_report(self):
        try:
            with open("database/order.json",'r') as sales_file:
                sales_data=json.load(sales_file)
                total_orders=len(sales_data)
                total_sales=0
                for sales in sales_data:
                    total_sales+=sales["total_amount"]
                print("===========================================================")
                print("*                      Sales Report                       *")
                print("===========================================================")
                print("Total Orders: ",total_orders)
                print("Total Sales: ", "₹" + str(total_sales))
        except FileNotFoundError:
            with open("logs/error.log",'a') as sales_error:
                sales_error.write(f"[{str(datetime.datetime.now())}] [ERROR] - Sales Report - order.json: Order Data is not found\n")
            print("Order Data is Not Found")
            return
    def cancelled_order(self):
        try:
            with open("database/order.json",'r') as cancelled_file:
                cancelled_order_data=json.load(cancelled_file)
            count=0
            for cancelled in cancelled_order_data:
                if cancelled["order_status"]=="Cancelled":
                    count+=1
                    print("===========================================================")
                    print("*                    Cancelled Order                      *")
                    print("===========================================================")
                    print("Order ID         : ",cancelled["order_id"])
                    print("Customer ID      : ",cancelled["customer_id"])
                    print("Customer Name    : ",cancelled["customer_name"])
                    print("Table ID         : ",cancelled["table_id"])
                    for item in cancelled["order_items"]:
                        print("Category         : ", item["category"])
                        print("Food Name        : ", item["food_name"])
                        print("Size             : ", item["size"])
                        print("Price            : ", "₹" + str(item["price"]))
                        print("Quantity         : ", item["quantity"])
                        print("Total Amount     : ", "₹" + str(item["total_amount"]))
                    print("Grand Total      : ", "₹" + str(cancelled["total_amount"]))
                    print("Payment Method   : ",cancelled["payment_method"])
                    print("Order Status     : ",cancelled["order_status"])
                    print("Date             : ",cancelled["date"])
                    print("Time             : ",cancelled["time"])
                    print("________________________________________________________")
            if count==0:
                with open("logs/war.log",'a') as cancelled_file_error:
                    cancelled_file_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Cancelled Order - order.json: Data is not found\n")
                print("Cancelled Order not found")
        except FileNotFoundError: 
            with open("logs/error.log",'a') as cancelled_error:
                cancelled_error.write(f"[{str(datetime.datetime.now())}] [ERROR] - Cancelled Order - order.json: File is not found\n")
            print("Order Not found")
            return
    def menu(self):
        while True:
            print("===========================================================")
            print("*                        Order Menu                       *")
            print("===========================================================")
            print("1. View All Order")
            print("2. Search Order")
            print("3. Sales Report")
            print("4. Cancelled Order")
            print("5. Back")
            choice=input("Enter Your Choice: ")
            if choice=="1":
                self.view_all_order()
            elif choice=="2":
                self.search_order()
            elif choice=="3":
                self.sales_report()
            elif choice=="4":
                self.cancelled_order()
            elif choice=="5":
                print("Program Back Successful")
                break
            else:
                print("Invalid Your Choice")
