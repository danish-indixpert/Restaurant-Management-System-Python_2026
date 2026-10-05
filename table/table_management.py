import json
import datetime
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
                        table_type_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Table - Table Type: Alpha Value Only\n")
                    print("Alpha Value Only")
            else:
                with open("logs/war.log",'a') as table_type_maximum:
                    table_type_maximum.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Table - Table Type - Maximum 3 Character Allow\n")
                print("Maximum 3 Character Allow")
        while True:
            try:
                table_capacity=int(input("Enter Table Capacity: "))
                if table_capacity>0:
                    break
                else:
                    with open("logs/war.log",'a') as capacity_error:
                        capacity_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Table - Table Capacity - Capacity 0 to Greater\n")
                    print("Capacity 0 to Greater")
            except ValueError:
                with open("logs/war.log",'a') as table_capacity_error:
                    table_capacity_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Table - Integer Value Only\n")
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
                type_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Table - Invalid Your Table Type\n")
            print("Invalid Your Table Type")
            return
        with open("database/table.json",'w') as file:
            json.dump(table_data,file,indent=4)
        with open("logs/table.log",'a') as add_table_log:
            add_table_log.write(f"[{str(datetime.datetime.now())}] [INFO] -  Table Added in Successfully. {table_type}\n")
        print("Table Added in Successful.")
    def view_table(self):
        try:
            with open("database/table.json",'r') as file:
                table_data=json.load(file)
            print("============================================================================================================")
            print("*                                                View Menu                                                 *")
            print("============================================================================================================\n")
            for table_type,user in table_data.items():
                count=0
                print("------------------------------------------------------------------------------------------------------------")
                print(f"                                                  {table_type}                                             ")
                print("------------------------------------------------------------------------------------------------------------")
                print("Table Type                                    Table Capacity                                          Status")
                print("------------------------------------------------------------------------------------------------------------")
                for table in user:
                    count+=1
                    print(str(count).ljust(4) + table["table_type"].ljust(48) + str(table["table_capacity"]).ljust(47) + str(table["status"]))
                print("____________________________________________________________________________________________________________\n\n\n")
        except FileNotFoundError:
            with open("logs/error.log",'a') as veiw_table:
                veiw_table.write(f"[{str(datetime.datetime.now())}] [ERROR] View Table tabale.json: File is not found\n")
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
                        type_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Table - Table Type - Maximum 3 Character Allow\n")
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
                                        table_type_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Table - New Table Type - Alpha Value Only\n")
                                    print("Alpha Value Only")
                            else:
                                with open("logs/war.log",'a') as new_table_alpha:
                                    new_table_alpha.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Table - New Table Type - Maximum 3 Character Allow\n")
                                print("Maximum 3 Character Allow")
                        update_data["table_type"]=new_table_type
                        with open("database/table.json",'w') as table_type_file:
                            json.dump(update_table_data,table_type_file,indent=4)
                        with open("logs/table.log",'a') as info_type:
                            info_type.write(f"[{str(datetime.datetime.now())}] [INFO] - Update Table - Table Type Update Successful\n")
                        print("Table Type Update Successful")
                    elif choice=="2":
                        while True:
                            try:
                                new_table_capacity=int(input("Enter New Table Capacity: "))
                                if new_table_capacity>0:
                                    break
                                else:
                                    with open("logs/war.log",'a') as capacity_integer:
                                        capacity_integer.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Table - New Table Capacity - Capacity 0 to Greater\n")
                                    print("Capacity 0 to Greater")
                            except ValueError:
                                with open("logs/war.log",'a') as capacity_error:
                                    capacity_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Table - New Table Capacity - Integer Value Only\n")
                                print("Integer Value Only")
                        update_data["table_capacity"]=new_table_capacity
                        with open("database/table.json",'w') as table_capacity_file:
                            json.dump(update_table_data,table_capacity_file,indent=4)
                        with open("logs/table.log",'a') as info_capacity:
                            info_capacity.write(f"[{str(datetime.datetime.now())}] [INFO] - Update Table - Table Capacity Update Successful\n")
                        print("Table Capacity Update Successful")
                    elif choice=="3":
                        with open("logs/table.log",'a') as update_error:
                            update_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Update Table - Program Back Successful\n")
                        print("Program Back Successful")
                        self.menu()
                    elif choice=="4":
                        with open("logs/table.json") as error_exit:
                            error_exit.write(f"[{str(datetime.datetime.now())}] [INFO] - Update Table - Restaurant Management System Close Successful.\n")
                        print("Restaurant Management System Close Successful. ")
                        break
                    else:
                        print("Invalid Your Update Table Choice")
            if table_count==0:
                with open("logs/war.log",'a') as data_not_found:
                    data_not_found.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Table - table.json: Table Data is not found\n")
                print("Table Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as data_not:
                data_not.write(f"[{str(datetime.datetime.now())}] [ERROR] - Update Table - table.json: File Data is not found\n")
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
                            type_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Delete Table - Table Type - Maximum 3 Character Allow\n")
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
                            delete_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Delete Table - Table Delete Successful\n")                            
                        print("Table Delete Successful")
                        break
                else:
                    with open("logs/war.log",'a') as delete_error_file:
                        delete_error_file.write(f"[{str(datetime.datetime.now())}] [WARNING] - Delete Table - table.json: Table Data is not found\n")
                    print("Table Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as error:
                error.write(f"[{str(datetime.datetime.now())}] [ERROR] - Delete Table - table.json: File Data is not found\n")
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
            print("5. Back")
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
                print("Program Back Successful")
                break
            else:
                print("Invalid Your Choice")
# obj=Table_Management()
# obj.menu()