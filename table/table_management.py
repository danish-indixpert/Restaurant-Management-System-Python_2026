import json
from datetime import datetime,timedelta
import uuid


class Table_Management:
    def add_table(self):
        table_id="T" + str(uuid.uuid4())[:3]
        print("============================================================")
        print("*                        Add Table                         *")
        print("============================================================")
        while True:
            table_type=input("Enter Table Type: ").title()
            if len(table_type)>2:
                if table_type.isalpha():
                    break
                else:
                    with open("logs/war.log",'a') as table_type_error:
                        table_type_error.write(f"[{str(datetime.now())}] [WARNING] - Add Table - Table Type: Alpha Value Only\n")
                    print("Alpha Value Only")
            else:
                with open("logs/war.log",'a') as table_type_maximum:
                    table_type_maximum.write(f"[{str(datetime.now())}] [WARNING] - Add Table - Table Type - Maximum 3 Character Allow\n")
                print("Maximum 3 Character Allow")
        while True:
            try:
                table_capacity=int(input("Enter Table Capacity: "))
                if table_capacity>0:
                    break
                else:
                    with open("logs/war.log",'a') as capacity_error:
                        capacity_error.write(f"[{str(datetime.now())}] [WARNING] - Add Table - Table Capacity - Capacity 0 to Greater\n")
                    print("Capacity 0 to Greater")
            except ValueError:
                with open("logs/war.log",'a') as table_capacity_error:
                    table_capacity_error.write(f"[{str(datetime.now())}] [WARNING] - Add Table - Integer Value Only\n")
                print("Integer Value Only")
        status="Available"
        table={
            "table_id":table_id,
            "table_type":table_type,
            "table_capacity":table_capacity,
            "status":status
        }
        try:
            with open("database/table.json",'r') as file:
                table_data=json.load(file)
        except FileNotFoundError:
            table_data={
                "Small":[],
                "Medium":[],
                "Vip":[],
                "Booking_Table":[]
            }
        try:
            table_data[table_type].append(table)
        except KeyError:
            with open("logs/war.log",'a') as type_error:
                type_error.write(f"[{str(datetime.now())}] [WARNING] - Add Table - Invalid Your Table Type\n")
            print("Invalid Your Table Type")
            return
        with open("database/table.json",'w') as file:
            json.dump(table_data,file,indent=4)
        with open("logs/table.log",'a') as add_table_log:
            add_table_log.write(f"[{str(datetime.now())}] [INFO] -  Table Added in Successfully. {table_type}\n")
        print("Table Added in Successful.")
    def view_table(self):
        try:
            with open("database/table.json",'r') as file:
                table_data=json.load(file)
            table_count=0
            print("============================================================================================================")
            print("*                                                View Menu                                                 *")
            print("============================================================================================================\n")
            for table_type,user in table_data.items():
                count=0
                print("------------------------------------------------------------------------------------------------------------")
                print(f"                                                  {table_type}                                             ")
                print("------------------------------------------------------------------------------------------------------------")
                print("Table ID                      Table Type                         Table Capacity                       Status")
                print("------------------------------------------------------------------------------------------------------------")
                for table in user:
                    count+=1
                    table_count+=1
                    print(str(count).ljust(3),table["table_id"].ljust(27),table["table_type"].ljust(39) +str(table["table_capacity"]).ljust(27),str(table["status"]))
                print("____________________________________________________________________________________________________________\n\n\n")
            if table_count==0:
                with open("logs/war.log",'a') as table_error:
                    table_error.write(f"[{str(datetime.now())}] [WARNING] -  View Table - table.json: Table Data is not found\n")
                print("Table Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as veiw_table:
                veiw_table.write(f"[{str(datetime.now())}] [ERROR] View Table tabale.json: File is not found\n")
            print("Data is not Found")
            return
    def update_table(self):
        try:
            with open("database/table.json",'r') as update_table_file:
                update_table_data=json.load(update_table_file)
            print("============================================================")
            print("*                       Update Table                       *")
            print("============================================================")
            table_count=0
            while True:
                table_type=input("Enter Table Type: ").title()
                if len(table_type)>2:
                    break
                else:
                    with open("logs/war.log",'a') as type_error:
                        type_error.write(f"[{str(datetime.now())}] [WARNING] - Update Table - Table Type - Maximum 3 Character Allow\n")
                    print("Maximum 3 Character Allow")
            for table in update_table_data[table_type]:
                table_count+=1
                print(table_count, ".",table["table_id"])
            choice=int(input("Enter Your Choice: "))
            table_count=0
            for update_data in update_table_data[table_type]:
                table_count+=1
                if table_count == choice:
                    print("============================================================")
                    print("*                     Update Table Menu                    *")
                    print("============================================================")
                    print("1. Update Table Type")
                    print("2. Update Table Capacity")
                    print("3. Back")
                    print("4. Exit")
                    choice=input("Enter Your Choice: ")
                    if choice=="1":
                        while True:
                            new_table_type=input("Enter New Table Type: ").title()
                            if len(new_table_type)>2:
                                if new_table_type.isalpha():
                                    break
                                else:
                                    with open("logs/war.log",'a') as table_type_error:
                                        table_type_error.write(f"[{str(datetime.now())}] [WARNING] - Update Table - New Table Type - Alpha Value Only\n")
                                    print("Alpha Value Only")
                            else:
                                with open("logs/war.log",'a') as new_table_alpha:
                                    new_table_alpha.write(f"[{str(datetime.now())}] [WARNING] - Update Table - New Table Type - Maximum 3 Character Allow\n")
                                print("Maximum 3 Character Allow")
                        update_data["table_type"]=new_table_type
                        with open("database/table.json",'w') as table_type_file:
                            json.dump(update_table_data,table_type_file,indent=4)
                        with open("logs/table.log",'a') as info_type:
                            info_type.write(f"[{str(datetime.now())}] [INFO] - Update Table - Table Type Update Successful\n")
                        print("Table Type Update Successful")
                    elif choice=="2":
                        while True:
                            try:
                                new_table_capacity=int(input("Enter New Table Capacity: "))
                                if new_table_capacity>0:
                                    break
                                else:
                                    with open("logs/war.log",'a') as capacity_integer:
                                        capacity_integer.write(f"[{str(datetime.now())}] [WARNING] - Update Table - New Table Capacity - Capacity 0 to Greater\n")
                                    print("Capacity 0 to Greater")
                            except ValueError:
                                with open("logs/war.log",'a') as capacity_error:
                                    capacity_error.write(f"[{str(datetime.now())}] [WARNING] - Update Table - New Table Capacity - Integer Value Only\n")
                                print("Integer Value Only")
                        update_data["table_capacity"]=new_table_capacity
                        with open("database/table.json",'w') as table_capacity_file:
                            json.dump(update_table_data,table_capacity_file,indent=4)
                        with open("logs/table.log",'a') as info_capacity:
                            info_capacity.write(f"[{str(datetime.now())}] [INFO] - Update Table - Table Capacity Update Successful\n")
                        print("Table Capacity Update Successful")
                    elif choice=="3":
                        with open("logs/table.log",'a') as update_error:
                            update_error.write(f"[{str(datetime.now())}] [INFO] - Update Table - Program Back Successful\n")
                        print("Program Back Successful")
                        self.menu()
                    elif choice=="4":
                        with open("logs/table.json") as error_exit:
                            error_exit.write(f"[{str(datetime.now())}] [INFO] - Update Table - Restaurant Management System Close Successful.\n")
                        print("Restaurant Management System Close Successful. ")
                        break
                    else:
                        print("Invalid Your Update Table Choice")
            if table_count==0:
                with open("logs/war.log",'a') as data_not_found:
                    data_not_found.write(f"[{str(datetime.now())}] [WARNING] - Update Table - table.json: Table Data is not found\n")
                print("Table Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as data_not:
                data_not.write(f"[{str(datetime.now())}] [ERROR] - Update Table - table.json: File Data is not found\n")
            print("Data is not found")
            return
    def delete_table(self):
        try:
            with open("database/table.json",'r') as delete_file:
                delete_table_data=json.load(delete_file)
                print("============================================================")
                print("*                      Delete Table                        *")
                print("============================================================")
                table_count=0
                while True:
                    table_type=input("Enter Table Type: ").title()
                    if len(table_type)>2:
                        break
                    else:
                        with open("logs/war.log",'a') as type_error:
                            type_error.write(f"[{str(datetime.now())}] [WARNING] - Delete Table - Table Type - Maximum 3 Character Allow\n")
                        print("Maximum 3 Character Allow")
                for delete in delete_table_data[table_type]:
                    table_count+=1
                    if delete["table_type"]==table_type:
                        print(table_count,".",delete["table_id"])
                delete_table_id=input("Enter Delete Table ID: ")
                for table_data in delete_table_data[table_type]:
                    table_count=0
                    if table_data["table_id"]==delete_table_id:
                        delete_table_data[table_type].remove(table_data)
                        with open("database/table.json",'w') as delete_table_file:
                            json.dump(delete_table_data,delete_table_file,indent=4)
                        with open("logs/table.log",'a') as delete_error:
                            delete_error.write(f"[{str(datetime.now())}] [INFO] - Delete Table - Table Delete Successful\n")                            
                        print("Table Delete Successful")
                        break
                else:
                    with open("logs/war.log",'a') as delete_error_file:
                        delete_error_file.write(f"[{str(datetime.now())}] [WARNING] - Delete Table - table.json: Table Data is not found\n")
                    print("Table Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as error:
                error.write(f"[{str(datetime.now())}] [ERROR] - Delete Table - table.json: File Data is not found\n")
            print("Data is not found")
            return
    def table_booking(self):
        try:
            with open("database/table.json", 'r') as table_file:
                table_data = json.load(table_file)
            print("=============================================================================================================")
            print("*                                                Table Book                                                 *")
            print("=============================================================================================================\n")
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
    def menu(self):
        while True:
            print("============================================================")
            print("*                        Table Menu                        *")
            print("============================================================")
            print("1. Add Table")
            print("2. View Menu")
            print("3. Update Table")
            print("4. Delete Table")
            print("5. Table Booking")
            print("6. Cancel Table Booking")
            print("7. Back")
            menu_choice=input("Enter Your Choice: ")
            if menu_choice=="1":
                self.add_table()
            elif menu_choice=="2":
                self.view_table()
            elif menu_choice=="3":
                self.update_table()
            elif menu_choice=="4":
                self.delete_table()
            elif menu_choice=="5":
                self.table_booking()
            elif menu_choice=="6":
                self.cancel_table_booking()
            elif menu_choice=="7":
                print("Program Back Successful")
                break
            else:
                print("Invalid Your Choice")
# obj=Table_Management()
# obj.menu()