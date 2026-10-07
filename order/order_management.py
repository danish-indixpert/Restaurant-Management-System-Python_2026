import json
from datetime import datetime
import uuid


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
                file_not_found.write(f"[{str(datetime.now())}] [ERROR] - View All Order - order.json: File is not found\n")
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
                            search_order.write(f"[{str(datetime.now())}] [WARNING] - Search Order - Order ID - Invalid Order ID\n")
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
                        search_file_error.write(f"[{str(datetime.now())}] [WARNING] - Search Order - order.json: Data is not found\n")
                    print("Order ID is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as file_not_found:
                file_not_found.write(f"[{str(datetime.now())}] [ERROR] - Update Order - order.json: File is not found\n")
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
                sales_error.write(f"[{str(datetime.now())}] [ERROR] - Sales Report - order.json: Order Data is not found\n")
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
                    cancelled_file_error.write(f"[{str(datetime.now())}] [WARNING] - Cancelled Order - order.json: Data is not found\n")
                print("Cancelled Order not found")
        except FileNotFoundError: 
            with open("logs/error.log",'a') as cancelled_error:
                cancelled_error.write(f"[{str(datetime.now())}] [ERROR] - Cancelled Order - order.json: File is not found\n")
            print("Order Not found")
            return
    def create_order(self):
            try:
                with open("database/food.json",'r') as food_file:
                    food_data=json.load(food_file)
                print("============================================================================================================")
                print("*                                               View Food                                                  *")
                print("============================================================================================================\n")
                for category,user in food_data.items():
                    count=0
                    print(f"\n                                            ||-+-{category}-+-||")
                    print("------------------------------------------------------------------------------------------------------------")
                    print("Food Name                                    Half Size Price                                 Full Size Price")
                    print("------------------------------------------------------------------------------------------------------------")
                    for food in user:
                        count+=1
                        print(str(count).ljust(3) + food["food_name"].ljust(46),("₹" + str(food["half_size_price"])).ljust(48),("₹" + str(food["full_size_price"])))
                    print("____________________________________________________________________________________________________________")
                customer_id="C" + str(uuid.uuid4())[:9]
                while True:
                    customer_name=input("Enter Customer Name: ").strip()
                    if len(customer_name)>2:
                        if customer_name.replace(" ","").isalpha():
                            break
                        else:
                            with open("logs/war.log",'a') as customer_name_file:
                                customer_name_file.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Custoomer: Alpha Value Only\n")
                            print("Alpha Value")
                    else:
                        with open("logs/war.log",'a') as maximum_allow:
                            maximum_allow.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Customer Name - Maximum 3 Character Allow\n")
                        print("Maximum 3 Character Allow")
                while True:
                    table_id=input("Enter Table ID: ")
                    if len(table_id)>2:
                        if table_id:
                            break
                        else:
                            with open("logs/war.log",'a') as table_id_file:
                                table_id_file.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Table ID: Alpha Number Value Only\n")
                            print("Invalid Table ID")
                    else:
                        with open("logs/war.log",'a') as table_error:
                            table_error.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Table ID - Maximum 3 Character or Number Allow\n")
                        print("Maximum 3 Character or Number Allow")
                try:
                    with open("database/table.json",'r') as file:
                        table_data=json.load(file)
                except FileNotFoundError:
                    with open("logs/war.log",'a') as error_data:
                        error_data.write(f"[{str(datetime.now())}] [WARNING] Create Order - table.json: Table Data is not found\n")
                    print("Table Data is not found")
                    return
                for category,tables in table_data.items():
                    for table in tables:
                        if table["table_id"]==table_id:
                            if table["status"]=="Booked":
                                with open("logs/war.log",'a') as already:
                                    already.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Table is Already Booked\n")
                                print("Table is Already Booked")
                                return
                            elif table["status"]=="Available":
                                table["status"]="Booked"
                                with open("database/table.json",'w') as status:
                                    json.dump(table_data,status,indent=4)
                                break
                order_items=[]
                total_amount=0
                while True:
                    while True:
                        category=input("Enter Food Category (Chinese/Fast Food/Italian/North Indian/Beverage): ").strip().title()
                        if len(category)>2:
                            if category.replace(" ","").isalpha():
                                break
                            else:
                                with open("logs/war.log",'a') as category_file:
                                    category_file.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Category: Alpha Value Only\n")
                                print("Alpha Value Only")
                        else:
                            with open("logs/war.log",'a') as category_allow:
                                category_allow.write(f"[{str(datetime.now())}] [WARNING] - Creater Order - Category - Maximum 3 Character Allow\n")
                            print("Maximum 3 Character Allow")
                    try:
                        category_data=food_data[category]
                    except KeyError:
                        with open("logs/war.log",'a') as category_error:
                            category_error.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Category - Invalid Food Category\n")
                        print("Invalid Food Category")
                        return
                    while True:
                        food_name=input("Enter Food Name: ").strip()
                        if len(food_name)>2:
                            if food_name.replace(" ","").isalpha():
                                break
                            else:
                                with open("logs/war.log",'a') as order_error:
                                    order_error.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Food Name - Alpha Value Only\n")
                                print("Alpha Value Only")
                        else:
                            with open("logs/war.log",'a') as food_name_error:
                                food_name_error.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Food Name - Maximum 3 Character Allow\n")
                            print("Maximum 3 Character Allow")
                    food_not_found=0
                    for food in category_data:
                        if food["food_name"].lower()==food_name.lower():
                            food_not_found=1
                            break
                    else:
                        with open("logs/war.log",'a') as food_found:
                            food_found.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Food not found\n")
                        print("Food Not found")
                    if food_not_found==0:
                        continue
                    print("============================================================")
                    print("*                         Food Size                        *")
                    print("============================================================")
                    print("1. Half Size Price")
                    print("2. Full Size Price")
                    food_size_choice=input("Enter Food Size Choice: ")
                    if food_size_choice=="1":
                        size="Half Size Price"
                        price=food["half_size_price"]
                    elif food_size_choice=="2":
                        size="Full Size Price"
                        price=food["full_size_price"]
                    else:
                        with open("logs/war.log",'a') as half_size:
                            half_size.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Food Size Choice - Invalid Your Food Size Choice\n")
                        print("Invalid Your Food Size Choice")
                        return
                    while True:
                        try:
                            quantity=int(input("Enter Quantity: "))
                            if quantity>0:
                                break
                            else:
                                with open("logs/war.log",'a') as order_quantity:
                                    order_quantity.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Quantity - Quantity 0 ot greater\n")
                                print("Quantity 0 or greater")
                        except ValueError:
                            with open("logs/war.log",'a') as quantity_file:
                                quantity_file.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Quantity: Integer Value Only\n")
                            print("Integer Value Only")
                    food_total=price*quantity
                    order_items.append({
                        "category":category,
                        "food_name":food["food_name"],
                        "size":size,
                        "price":price,
                        "quantity":quantity,
                        "total_amount":food_total
                    })
                    total_amount+=food_total
                    with open("logs/food.log",'a') as food_added:
                        food_added.write(f"[{str(datetime.now())}] [INFO] - Create Order - Food Added Successful\n")
                    print("Food Added Successfully")
                    print("Food Total: ₹" + str(food_total))
                    food_selection=input("Do you want to add more food? (yes/no): ").capitalize()
                    if food_selection=="Yes":
                        continue
                    elif food_selection=="No":
                        break
                    else:
                        with open("logs/war.log",'a') as selection:
                            selection.write(f"[{str(datetime.now())}] [WARNING] - Create Order - Food Selection Yes/No - Invalid Your Choice\n")
                        print("Invalid Your Choice")
                        break
                order_id="O" + str(uuid.uuid4())[:3]
                date=datetime.now().strftime("%d-%m-%Y")
                time=datetime.now().strftime("%I:%M:%p")
                order={
                    "order_id":order_id,
                    "customer_id":customer_id,
                    "customer_name":customer_name,
                    "table_id":table_id,
                    "order_items":order_items,
                    "total_amount":total_amount,
                    "payment_method":"Pending",
                    "payment_status":"Pending",
                    "order_status":"Complete",
                    "date":str(date),
                    "time":str(time)
                }
                try:
                    with open("database/order.json",'r') as order_file:
                        orders=json.load(order_file)
                except FileNotFoundError:
                    orders=[]
                for unique_id in orders:
                    if unique_id["order_id"]==order_id:
                        with open("logs/war.log",'a') as dup_order_id:
                            dup_order_id.write(f"[{str(datetime.now())}] [WARNING] - Create Order - This Order ID is Already Ordered Create\n")
                        print("This Order ID is Already Ordered Create")
                        return
                orders.append(order)
                with open("database/order.json",'w') as order_file:
                    json.dump(orders,order_file,indent=4)
                with open("logs/order.log",'a') as order_successful:
                    order_successful.write(f"[{str(datetime.now())}] [INFO] - Order Create Successful {order_id}\n")
                print("\nOrder Create Successful\n")
                print("Order ID      : ",order_id)
                print("Customer Name : ",customer_name)
                print("Table ID      : ",table_id)
                print("Total Amount  : ","₹" + str(total_amount))
                print("Order Status  : ","Complete")
            except FileNotFoundError:
                with open("logs/error.log",'a') as file_not_found:
                    file_not_found.write(f"[{str(datetime.now())}] [ERROR] - Create Order - food.json: File is not found\n")
                print("Data is not found")
    def delete_order(self):
        try:
            with open("database/order.json",'r') as delete_order_error:
                delete_order_data=json.load(delete_order_error)
                count=0
                order_id=input("Enter Order: ")
                for delete in delete_order_data:
                    count+=1
                    if delete["order_id"]==order_id:
                        print("1. yes")
                        print("2. no")
                        choice=input("Enter Your Choice or (yes/no): ").strip().title()
                        if choice=="Yes":
                            delete_order_data.remove(delete)
                            with open("database/order.json",'w') as order_file:
                                json.dump(delete_order_data,order_file,indent=4)
                            with open("logs/order.log",'a') as delete_order:
                                delete_order.write(f"[{str(datetime.now())}] [INFO] - Delete Order - Order Delete Successful\n")
                            print("Order Delete Successful")
                        elif choice=="No":
                            with open("logs/order.log",'a') as successful:
                                successful.write(f"[{str(datetime.now())}] [INFO] - Delete Order - Order Delete Cancel Successful\n")
                            print("Order Delete Cancel Successful")
                        else:
                            with open("logs/war.log",'a') as invalid:
                                invalid.write(f"[{str(datetime.now())}] [WARNING] - Delete Order - Invalid Your Choice\n")
                            print("Invalid Your Choice")
                if count==0:
                    with open("logs/war.log",'a') as order_data:
                        order_data.write(f"[{str(datetime.now())}] [WARNING] - Delete Order - order.json: Order Data is not found\n")
                    print("Order Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as file_not:
                file_not.write(f"[{str(datetime.now())}] [ERROR] - Delete Order - order.json: File is not found\n")
            print("Data is not found")
    def menu(self):
        while True:
            print("===========================================================")
            print("*                        Order Menu                       *")
            print("===========================================================")
            print("1. View All Order")
            print("2. Search Order")
            print("3. Sales Report")
            print("4. Cancelled Order")
            print("5. Create Order")
            print("6. Delete Order")
            print("7. Back")
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
                self.create_order()
            elif choice=="6":
                self.delete_order()
            elif choice=="7":
                print("Program Back Successful")
                break
            else:
                print("Invalid Your Choice")
# obj=Order_Admin()
# obj.menu()