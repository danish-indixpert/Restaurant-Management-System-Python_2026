from billing.bill import Bill_Management
from datetime import datetime,timedelta
import uuid
import json


class Order_Staff:
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
                            break
            order_items=[]
            total_amount=0
            while True:
                while True:
                    category=input("Enter Food Category: ").strip().title()
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
                    print("Invalid Choice")
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
                "order_status":"Pending",
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
            print("Order Status  : ","Pending")
        except FileNotFoundError:
            with open("logs/error.log",'a') as file_not_found:
                file_not_found.write(f"[{str(datetime.now())}] [ERROR] - Create Order - food.json: File is not found\n")
            print("Data is not found")
    def view_order(self):
        try:
            with open("database/order.json",'r') as view_order:
                view_order_data=json.load(view_order)
                user=0
                for order in view_order_data:
                    user+=1
                    print("============================================================")
                    print(f"*                    View Order {user}                    *")
                    print("============================================================")
                    print("Order ID         : ", order["order_id"])
                    print("Customer ID      : ", order["customer_id"])
                    print("Customer Name    : ", order["customer_name"])
                    print("Table ID         : ", order["table_id"])
                    for item in order["order_items"]:
                        print("Category         : ", item["category"])
                        print("Food Name        : ", item["food_name"])
                        print("Size             : ", item["size"])
                        print("Price            : ", "₹" + str(item["price"]))
                        print("Quantity         : ", item["quantity"])
                        print("Total Amount     : ", "₹" + str(item["total_amount"]))
                    print("Grand Total      : ", "₹" + str(order["total_amount"]))
                    print("Order Status     : ", order["order_status"])
                    print("Date             : ", order["date"])
                    print("Time             : ", order["time"])
                    print("________________________________________________________")
                if user==0:
                    with open("logs/war.log",'a') as view_order_error:
                        view_order_error.write(f"[{str(datetime.now())}] [WARNING] - View Order - order.json: Data is nout found\n")
                    print("Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as error_not_found:
                error_not_found.write(f"[{str(datetime.now())}] [ERROR] - View Order - order.json: File is not found\n")
            print("Data is not found")
            return
    def update_order(self):
        try:
            with open("database/order.json",'r') as update:
                update_data=json.load(update)
            while True:
                order_id=input("Enter Order ID: ")
                if order_id.isalnum():
                    break
                else:
                    with open("logs/war.log",'a') as order_error:
                        order_error.write(f"[{str(datetime.now())}] [WARNING] - Update Order - Order ID - Alpha Number Value Only\n")
                    print("Alpha Number Value Only")
            for i in update_data:
                if i["order_id"]==order_id:
                    print("============================================================")
                    print("*                      Status Menu                         *")
                    print("============================================================")
                    print("1. Pending")
                    print("2. Complete")
                    print("3. Cancelled")
                    status_choice=input("Enter Status Choice: ")
                    if status_choice=="1":
                        i["order_status"]="Pending"
                    elif status_choice=="2":
                        i["order_status"]="Complete"
                    elif status_choice=="3":
                        i["order_status"]="Cancelled"
                    else:
                        print("Invalid Your Order Status Choice")
                        return           
                    with open("database/order.json",'w') as update_status:
                        json.dump(update_data,update_status,indent=4)
                    print("Order Update Successful")
                    return                 
            else:
                with open("logs/war.log",'a') as update_error:
                    update_error.write(f"[{str(datetime.now())}] [WARNING] - Update Order - order.json: Order Data is not found\n")
                print("Order not found")
                return
        except FileNotFoundError:
            with open("logs/error.log",'a') as error_not_found:
                error_not_found.write(f"[{str(datetime.now())}] [ERROR] - Update Order - order.json: File is not found")
            print("Data is not found")
            return
    def cancel_order(self):
        count=0
        try:
            with open("database/order.json",'r') as cancel:
                cancel_data=json.load(cancel)
            while True:
                order_id=input("Enter Order ID: ")
                if order_id.isalnum():
                    break
                else:
                    with open("logs/war.log",'a') as order_id_error:
                        order_id_error.write(f"[{str(datetime.now())}] [WARNING] - Cancel Order - Order ID - Alpha Number Value Only\n")
                    print("Alpha Value Only")
            for i in cancel_data:
                if i["order_id"]==order_id:
                    count+=1
                    if i["order_status"]=="Pending":
                        i["order_status"]="Cancelled"
                    else:
                        with open("logs/war.log",'a') as called:
                            called.write(f"[{str(datetime.now())}] [WARNING] - Cancel Order - Order Cannot be Cancelled\n")
                        print("Order Cannot be Cancelled")
                        return
                    with open("database/order.json",'w') as remove_file:
                        json.dump(cancel_data,remove_file,indent=4)
                    with open("logs/order.log",'a') as cancel_data_error:
                        cancel_data_error.write(f"[{str(datetime.now())}] [INFO] - Cancel Order - Order Cancel Successful\n")
                    print("Order Cancel Successful")
                    return
            if count==0:
                with open("logs/war.log",'a') as cancel_error:
                    cancel_error.write(f"[{str(datetime.now())}] [WARNING] - Cancel Order - order.json: Order Data is not found\n")
                print("Order Not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as cancel_order_error:
                cancel_order_error.write(f"[{str(datetime.now())}] [ERROR] - Cancel Order - order.json - File is not found\n")
            print("Data is not found")
            return
    def view_pending_order(self):
        try:
            with open("database/order.json",'r') as pending_order:
                view_pending_order_data=json.load(pending_order)
                user=0
                for i in view_pending_order_data:
                    if i["order_status"]=="Pending":
                        user+=1
                        print("============================================================")
                        print(f"*                View Pending Order {user}                *")
                        print("============================================================")
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
                        print("Order Status     : ",i["order_status"])
                        print("Date             : ",i["date"])
                        print("Time             : ",i["time"])
                        print("________________________________________________________")
                if user==0:
                    with open("logs/war.log",'a') as view_pending_error:
                        view_pending_error.write(f"[{str(datetime.now())}] [WARNING] - View Pending Order - order.json: Data is not found\n")
                    print("Data is not found")                        
        except FileNotFoundError:
            with open("logs/error.log",'a') as view_pending:
                view_pending.write(f"[{str(datetime.now())}] [ERROR] - View Pending Order - order.json: File is not found\n")
            print("Data is not found")
            return
    def view_complete_order(self):
        try:
            with open("database/order.json",'r') as complete_order:
                view_complete_order_data=json.load(complete_order)
                user=0
                for i in view_complete_order_data:
                    if i["order_status"]=="Complete":
                        user+=1
                        print("==============================================================================")
                        print(f"*                        View Complete Order {user}                         *")
                        print("==============================================================================")
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
                        print("Order Status     : ",i["order_status"])
                        print("Date             : ",i["date"])
                        print("Time             : ",i["time"])
                        print("________________________________________________________")
                if user==0:
                    with open("logs/war.log",'a') as complete_error:
                        complete_error.write(f"[{str(datetime.now())}] [WARNING] - View Complete Order - order.json: Order Data is not found\n")
                    print("Order Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as complete_order_error:
                complete_order_error.write(f"[{str(datetime.now())}] [ERROR] - View Complete Order - order.json: File is not found\n")
            print("Data is not found")
            return
    def order_history(self):
        try:
            with open("database/order.json",'r') as history:
                order_history_data=json.load(history)
                user=0
                for order in order_history_data:
                    user+=1
                    print("==============================================================================")
                    print(f"*                                Order {user}                               *")
                    print("==============================================================================")
                    print("Order ID         : ",order["order_id"])
                    print("Customer ID      : ",order["customer_id"])
                    print("Customer Name    : ",order["customer_name"])
                    print("Table ID         : ",order["table_id"])
                    for item in order["order_items"]:
                        print("Category         : ", item["category"])
                        print("Food Name        : ", item["food_name"])
                        print("Size             : ", item["size"])
                        print("Price            : ", "₹" + str(item["price"]))
                        print("Quantity         : ", item["quantity"])
                        print("Total Amount     : ", "₹" + str(item["total_amount"]))
                    print("Grand Total      : ", "₹" + str(order["total_amount"]))
                    print("Payment Method   : ",order["payment_method"])
                    print("Payment Status   : ",order["payment_status"])
                    print("Order Status     : ",order["order_status"])
                    print("Date             : ",order["date"])
                    print("Time             : ",order["time"])
                    print("________________________________________________________")
                else:
                    with open("logs/war.log",'a') as order_history_error:
                        order_history_error.write(f"[{str(datetime.now())}] [WARNING] - Order History - order.json: Order Data is not found\n")
                    print("Order Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as history_error:
                history_error.write(f"[{str(datetime.now())}] [ERROR] - Order History - order.json: File is not found\n")
            print("Data is not found")
            return
    def table_booking(self):
        try:
            with open("database/table.json", 'r') as table_file:
                table_data = json.load(table_file)
            print("=============================================================================================================")
            print("*                                                Table Book                                                 *")
            print("=============================================================================================================")
            table_count = 0
            print("Table ID                       Table Type                         Table Capacity                       Status")
            print("-------------------------------------------------------------------------------------------------------------")
            for category in table_data:
                for table in table_data[category]:
                    if table["status"] == "Available":
                        table_count += 1
                        print(str(table_count).ljust(3),table["table_id"].ljust(28),table["table_type"].ljust(39) +str(table["table_capacity"]).ljust(27),str(table["status"]))
            while True:            
                table_id=input("Enter Table ID: ")
                if len(table_id)>2:
                    if table_id.isalnum():
                        break
                    else:
                        with open("logs/war.log",'a') as table_id_error:
                            table_id_error.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Table ID - Alpha Number Value Only\n")
                        print("Alpha Number Value Only")
                else:
                    with open("logs/war.log",'a') as table_error:
                        table_error.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Table ID - Maximum 3 Character or Number Allow\n")
                    print("Maximum 3 Character or Number Allow")
            table_count = 0
            for category in table_data:
                if category == "Booking_Table":
                    continue
                for table in table_data[category]:
                    if table["table_id"] == table_id:
                        if table["status"] == "Booked":
                            with open("logs/war.log",'a') as booked:
                                booked.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Table is Already Booked\n")
                            print("Table is Already Booked")
                            return
                        if table["status"] == "Available":
                            table_count += 1
                            while True:
                                table_type=input("Enter Booking Table Type: ").strip()
                                if len(table_type)>2:
                                    if table_type.replace("_","").isalnum():
                                        break
                                    else:
                                        with open("logs/war.log",'a') as type_error:
                                            type_error.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Table Type - Alpha Value Only\n")
                                        print("Alpha Value Only")
                                else:
                                    with open("logs/war.log",'a') as table_type_erro:
                                        table_type_erro.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Table Type - Maximum 3 Character Allow\n")
                                    print("Maximum 3 Character Allow")
                            customer_id = "C" + str(uuid.uuid4())[:9]
                            table["table_type"]==table_type
                            while True:
                                customer_name=input("Enter Customer Name: ").strip()
                                if len(customer_name)>2:
                                    if customer_name.replace(" ","").isalpha():
                                        break
                                    else:
                                        with open("logs/war.log",'a') as name_error:
                                            name_error.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Customer Name - Alpha Value Only\n")
                                        print("Alpha Value Only")
                                else:
                                    with open("logs/war.log",'a') as customer_name_error:
                                        customer_name_error.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Customer Name - Maximum 3 Character Allow\n")
                                    print("Maximum 3 Character Allow")
                            while True:
                                date=input("Enter Table Booking Date: ")
                                try:
                                    booking_date=datetime.strptime(date,"%d-%m-%Y")
                                    if booking_date.date()<datetime.now().date():
                                        with open("logs/war.log",'a') as back_time:
                                            back_time.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Booking Date - Back Date is Not Allow\n")
                                        print("Back Date is Not Allow")
                                    else:
                                        break
                                except ValueError:
                                    with open("logs/war.log",'a') as invalid_date:
                                        invalid_date.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Date - Invalid Date\n")
                                    print("Invalid Date")
                            while True:
                                time=input("Enter Table Booking Time: ")
                                try:
                                    booking_time=datetime.strptime(time,"%I:%M %p")
                                    if booking_time.time()<datetime.now().time():
                                        with open("logs/war.log",'a') as back_time_error:
                                            back_time_error.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Booking Time - Back Time is Not Allow\n")
                                        print("Back Time is Not Allow")
                                    else:
                                        break
                                except ValueError:
                                    with open("logs/war.log",'a') as invalid_time:
                                        invalid_time.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Invalid Time\n")
                                    print("Invalid Time")
                            while True:
                                try:
                                    duration=int(input("Enter Duration Time: "))
                                    if duration>0:
                                        break
                                    else:
                                        with open("logs/war.log",'a') as duration_error:
                                            duration_error.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Duration - 0 is Not Allow\n")
                                        print("0 is Not Allow")
                                except ValueError:
                                    with open("logs/war.log",'a') as duration_integer:
                                        duration_integer.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - Duration - Integer Value Only\n")
                                    print("Integer Value Only")
                            booking_datetime = datetime.combine(booking_date.date(),booking_time.time())
                            end_time=booking_datetime+timedelta(hours=duration)
                            table["status"] = "Booked"
                            data={
                                "table_id": table_id,
                                "table_type":table["table_type"],
                                "table_capacity":table["table_capacity"],
                                "customer_id":customer_id,
                                "customer_name":customer_name,
                                "date":date,
                                "start_time":time,
                                "duration":duration,
                                "end_time": end_time.strftime("%d-%m-%Y %I:%M %p"),
                                "status":table["status"]
                            }
                            try: 
                                table_data["Booking_Table"].append(data)
                            except KeyError:
                                with open("logs/war.log",'a') as invalid_type:
                                    invalid_type.write(f"[{str(datetime.now())}] Table Booking - Invalid Table Type\n")
                                print("Invalid Table Type")
                                return
                            with open("database/table.json", 'w') as table_file:
                                json.dump(table_data, table_file, indent=4)
                            with open("logs/table.log",'a') as table_book:
                                table_book.write(f"[{str(datetime.now())}] [INFO] - Table Booking - Table Booked Successful\n")
                            print("Table Booked Successfully")
            if table_count==0:
                with open("logs/war.log",'a') as booking_error:
                    booking_error.write(f"[{str(datetime.now())}] [WARNING] - Table Booking - table.json: Table Dat is not found\n")
                print("Table Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as file_error:
                file_error.write(f"[{str(datetime.now())}] [ERROR] - Table Booking - table.json: File is not found\n")
            print("Data is not found")
    def cancel_table_booking(self):
        try:
            with open("database/table.json",'r') as cancel_file:
                cancel_table_booking_data=json.load(cancel_file)
            print("============================================================")
            print("*                   Cancel Table Booking                   *")
            print("============================================================")
            while True:
                table_id=input("Enter Table ID: ")
                if table_id.isalnum():
                    break
                else:
                    with open("logs/war.log",'a') as table_id_error:
                        table_id_error.write(f"[{str(datetime.now())}] [WARNING] - Cancel Table Booking - Table ID - Alpha Number Value Only\n")
                    print("Alpha Value Only")
            for  type in cancel_table_booking_data:
                for i in cancel_table_booking_data[type]:
                    if i["table_id"]==table_id:
                        if i["status"]=="Booked":
                            i["status"]="Available"
                            for booking in cancel_table_booking_data["Booking_Table"].copy():
                                if booking["table_id"] == table_id:
                                    cancel_table_booking_data["Booking_Table"].remove(booking)
                            with open("database/table.json",'w') as avialabe_data:
                                json.dump(cancel_table_booking_data,avialabe_data,indent=4)
                            with open("logs/table.log",'a') as error_availabe:
                                error_availabe.write(f"[{str(datetime.now())}] [INFO] - Cancel Table Booking - Table Booking Cancel Successful\n")
                            print("Table Booking Cancel Successful")
                            return
                        else:
                            with open("logs/war.log",'a') as booked_error:
                                booked_error.write(f"[{str(datetime.now())}] [WARNING] - Cancel Table Booking - Table is not Booked\n")
                            print("Table is not Booked")
                            return
        except FileNotFoundError:
            with open("logs/error.log",'a') as error:
                error.write(f"[{str(datetime.now())}] [ERROR] - Cancel Table Booking - table.json: File is not found\n")
            print("Data is not found")
            return
    def veiw_booked_table(self):
        try:
            with open("database/table.json",'r') as file:
                view_booked_table_data=json.load(file)
            print("Table ID               Customer Name                 Booking Date                 Start Time                 End Time")
            print("---------------------------------------------------------------------------------------------------------------------")
            table_count=0
            for i in view_booked_table_data["Booking_Table"]:
                if i["status"]=="Booked":
                    table_count+=1
                    print(str(table_count).ljust(3),i["table_id"].ljust(21),i["customer_name"].ljust(28) +str(i["date"]).ljust(28),str(i["start_time"]).ljust(14),str(i["end_time"]))
            if table_count==0:
                with open("logs/war.log",'a') as war_log:
                    war_log.write(f"[{str(datetime.now())}] [WARNING] - View Booked Table - table.json: Table Data is not found\n")
                print("Table Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as error_log:
                error_log.write(f"[{str(datetime.now())}] [ERROR] - Veiw Booked Table - table.json: File is not found\n")
            print("Data is not found")
            return
    def table_menu(self):
        while True:
            print("===========================================================")
            print("*                       Table Menu                        *")
            print("===========================================================")
            print("1. Table Booking")
            print("2. Cancel Table Booking")
            print("3. View Booked Table")
            print("4. Back")
            choice=input("Enter Your Choice: ")
            if choice=="1":
                self.table_booking()
            elif choice=="2":
                self.cancel_table_booking()
            elif choice=="3":
                self.veiw_booked_table()
            elif choice=="4":
                print("Program Back Successful")
                break
            else:
                print("Invalid Your Choice")
    def menu(self):
        while True:
            print("===========================================================")
            print("*                    Order Staff Menu                     *")
            print("===========================================================")
            print("1. Create Order")
            print("2. View Order")
            print("3. Update Order")
            print("4. Cancel Order")
            print("5. View Pending Order")
            print("6. View Complete Order")
            print("7. Order History")
            print("8. Bills")
            print("9. Table Book")
            print("10. Back")
            choice=input("Enter Your Choice: ")
            if choice=="1":
                self.create_order()
            elif choice=="2":
                self.view_order()
            elif choice=="3":
                self.update_order()
            elif choice=="4":
                self.cancel_order()
            elif choice=="5":
                self.view_pending_order()
            elif choice=="6":
                self.view_complete_order()
            elif choice=="7":
                self.order_history() 
            elif choice=="8":
                obj=Bill_Management()
                obj.menu()
            elif choice=="9":
                self.table_menu()
            elif choice=="10":
                print("Program Back Successful.")
                break         
            else:
                print("Invalid Your Choice")
# obj=Order_Staff()
# obj.menu()