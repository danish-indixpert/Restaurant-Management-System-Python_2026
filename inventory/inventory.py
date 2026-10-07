import json
import uuid
from datetime import datetime


class Inventory:
    def add_inventory(self):
        print("\n=========================================================")
        print("                     Add Inventory                       ")
        print("=========================================================\n")
        inventory_id="I" + str(uuid.uuid4())[:3]
        while True:
            inventory_name=input("Enter Inventory Name: ").strip()
            if len(inventory_name)>2:
                if inventory_name.replace(" ","").isalpha():
                    break
                else:
                    with open("logs/war.log",'a') as inventory_name_error:
                        inventory_name_error.write(f"[{str(datetime.now())}] [WARNING] - Add Inventory - Inventory Name: Alpha Value Only\n")
                    print("Alpha Value Only")
            else:
                with open("logs/war.log",'a') as inventory_allow:
                    inventory_allow.write(f"[{str(datetime.now())}] [WARNING] - Add Inventory - Inventory Name - Maximum 3 Character Allow\n")
                print("Maximum 3 Character Allow")
        while True:
            inventory_category=input("Enter Inventory Category: ").strip().title()
            if len(inventory_category)>2:
                if inventory_category.isalpha():
                    break
                else:
                    with open("logs/war.log",'a') as inventory_category_error:
                        inventory_category_error.write(f"[{str(datetime.now())}] [WARNING] - Add Inventory - Inventory Category: Alpha Value Only\n")
                    print("Alpha Value Only")
            else:
                with open("logs/war.log",'a') as category_error:
                    category_error.write(f"[{str(datetime.now())}] [WARNING] - Add Inventory - Inventory Category - Maximum 3 Character Allow\n")
                print("Maximum 3 Character Allow")
        while True:
            inventory_unit=input("Enter Inventory Unit: ")
            if inventory_unit =="kg" or inventory_unit=="litre":
                inventory_quantity=float(input("Enter Inventory Quantity: "))
                if inventory_quantity>0:
                    break
                else:
                    with open("logs/war.log",'a') as greater_error:
                        greater_error.write(f"[{str(datetime.now())}] [WARNING] - Add Inventory - Inventory Quantity - Quantity 0 to Greater\n")
                    print("Quantity 0 to Greater")
            else:
                with open("logs/war.log",'a') as unit_error:
                    unit_error.write(f"[{str(datetime.now())}] [WARNING] - Add Inventory - Inventory Unit - Alpha Number Value Only\n")
                print("Alpha Number Value Only")
        while True:
            try:
                inventory_price=int(input("Enter Inventory Price: "))
                if inventory_price>0:
                    break
                else:
                    with open("logs/war.log",'a') as inventory_error:
                        inventory_error.write(f"[{str(datetime.now())}] [WARNING] - Add Inventory - Inventory Price - Price 0 to Greanter\n")
                    print("Price 0 to Greater")
            except ValueError:
                with open("logs/war.log",'a') as add_error:
                    add_error.write(f"[{str(datetime.now())}] [WARNING] - Add Inventory - Inventory Price - Intger Value Only\n")
                print("Integer Value Only")
        inventory_stock_status="In Stock"
        inventory_date=datetime.now().strftime("%d-%m-%Y")
        inventory_time=datetime.now().strftime("%I:%M:%p")
        inventory={
            "inventory_id":inventory_id,
            "inventory_name":inventory_name,
            "inventory_category":inventory_category,
            "inventory_quantity":inventory_quantity,
            "inventory_unit":inventory_unit,
            "inventory_price":inventory_price,
            "inventory_stock_status":inventory_stock_status,
            "inventory_date":inventory_date,
            "inventory_time":inventory_time
        }
        try:
            with open("database/inventory.json",'r') as inventory_file:
                inventory_data=json.load(inventory_file)
        except FileNotFoundError:
            inventory_data=[]
        inventory_data.append(inventory)
        with open("database/inventory.json",'w') as inventory_file:
            json.dump(inventory_data,inventory_file,indent=4)
        with open("logs/inventory.log",'a') as inventory_data_add:
            inventory_data_add.write(f"[{str(datetime.now())}] [INFO] - Inventory Added In Successful\n")
        print("Inventory Added in Successful")
    def view_inventory(self):
        try:
            with open("database/inventory.json",'r') as view_inventory_file:
                view_inventory_data=json.load(view_inventory_file)
            print("=============================================================================================================================")
            print("*                                                          View Menu                                                        *")
            print("=============================================================================================================================\n")
            count=0
            print("Inventory ID              Inventory Name              Category               Quantity               Unit               Status")
            print("-----------------------------------------------------------------------------------------------------------------------------")
            for view in view_inventory_data:
                count+=1
                print(str(count).ljust(2),view["inventory_id"].ljust(28) +str(view["inventory_name"]).ljust(24) +str(view["inventory_category"]).ljust(23),str(view["inventory_quantity"]).ljust(21),str(view["inventory_unit"]).ljust(14),str(view["inventory_stock_status"]))
            if count==0:
                with open("logs/war.log",'a') as found_table:
                    found_table.write(f"[{str(datetime.now())}] [WARNING] - View Inventory - inventory.json: Inventory Data is not found\n")
                print("Inventory Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as veiw_error:
                veiw_error.write(f"[{str(datetime.now())}] [ERROR] - View Inventory - inventory.json: File is not found\n")
            print("Data is not found")
            return
    def update_inventory(self):
        try:
            with open("database/inventory.json",'r') as update_inventory_file:
                update_inventory_data=json.load(update_inventory_file)
                while True:
                    inventory_id=input("Enter Inventory ID or Inventory Name: ").strip()
                    if inventory_id.replace(" ","").isalnum():
                        break
                    else:
                        with open("logs/war.log",'a') as update_error:
                            update_error.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - Inventory ID - Alpha Number Value Only\n")
                        print("Alpha Number Value Only")
                for update in update_inventory_data:
                    if update["inventory_id"]==inventory_id or update["inventory_name"]==inventory_id:
                        print("==============================================================================")
                        print("*                             Update Inventory                               *")
                        print("==============================================================================")
                        print("1. Inventory Name Update")
                        print("2. Inventory Category Update")
                        print("3. Inventory Quantity Update")
                        print("4. Inventory Unit Update")
                        print("5. Inventory Price Update")
                        print("6. Back")
                        inventory_choice=input("Enter Your Inventory Choice: ")
                        if inventory_choice=="1":
                            while True:
                                new_inventory_name=input("Enter New Inventory Name: ").strip().title()
                                if len(new_inventory_name)>2:
                                    if new_inventory_name.replace(" ","").isalpha():
                                        break
                                    else:
                                        with open("logs/war.log",'a') as update_error_inventory:
                                            update_error_inventory.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - New Inventory Name - Alpha Value Only\n")
                                        print("Alpha Value Only")
                                else:
                                    with open("logs/war.log",'a') as new_name_error:
                                        new_name_error.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - New Inventory Name - Maximum 3 Character Allow\n")
                                    print("Maximum 3 Character Allow")
                            update["inventory_name"]=new_inventory_name
                            with open("database/inventory.json",'w') as new_name:
                                json.dump(update_inventory_data,new_name,indent=4)
                            with open("logs/inventory.log",'a') as info_name:
                                info_name.write(f"[{str(datetime.now())}] [INFO] - Update Inventory - Inventory Name Update Successful\n")
                            print("Inventory Name Update Successful")
                            break
                        elif inventory_choice=="2":
                            while True:
                                new_inventory_category=input("Enter New Inventory Category: ").strip().title()
                                if len(new_inventory_category)>2:
                                    if new_inventory_category.replace(" ","").isalpha():
                                        break
                                    else:
                                        with open("logs/war.log",'a') as category_eeor:
                                            category_eeor.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - New Inventory Category - Alpha Value Only\n")
                                        print("Alpha Value Only")
                                else:
                                    with open("logs/war.log",'a') as new_category_allow:
                                        new_category_allow.write(f"[{str(datetime.now())}] [WARNING] - Update Invetory - New Inventory Category - Maximum 3 Character Allow\n")
                                    print("Maximum 3 Character Allow")
                            update["inventory_category"]=new_inventory_category
                            with open("database/inventory.json",'w') as new_category:
                                json.dump(update_inventory_data,new_category,indent=4)
                            with open("logs/inventory.log",'a') as info_category:
                                info_category.write(f"[{str(datetime.now())}] [INFO] - Update Inventory - Inventory Category Update Successful\n")
                            print("Inventory Category Update Successful")
                            break
                        elif inventory_choice=="3":
                            while True:
                                try:
                                    new_inventory_quantity=float(input("Enter New Inventory Quantity: "))
                                    if new_inventory_quantity>0:
                                        break
                                    else:
                                        with open("logs/war.log",'a') as update_quantity:
                                            update_quantity.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - New Inventory Quantity - Quantity Greater Than 0 Only\n")
                                        print("Quantity Greater Than 0 Only")
                                except ValueError:
                                    with open("logs/war.log",'a') as update_error_value:
                                        update_error_value.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - New Inventory Quantity - Integer Value Only\n")
                                    print("Integer Value Only")
                            update["inventory_quantity"]=new_inventory_quantity
                            if new_inventory_quantity==0:
                                update["inventory_stock_status"]="Out Of Stock"
                            elif new_inventory_quantity <10:
                                update["inventory_stock_status"]="Low Stock"
                            else:
                                update["inventory_stock_status"]="In Stock"
                            with open("database/inventory.json",'w') as new_quantity:
                                json.dump(update_inventory_data,new_quantity,indent=4)
                            with open("logs/inventory.log",'a') as update_erro:
                                update_erro.write(f"[{str(datetime.now())}] [INFO] - Update Inventory - Inventory Quantity Update Successful\n")
                            print("Inventory Quantity Update Successful")
                            break
                        elif inventory_choice=="4":
                            while True:
                                new_inventory_unit=input("Enter New Inventory Unit: ")
                                if len(new_inventory_unit)>1:
                                    if new_inventory_unit.isalpha():
                                        break
                                    else:
                                        with open("logs/war.log",'a') as inventory_error:
                                            inventory_error.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - New Inventory Unit - Alpha Value Only\n")
                                        print("Alpha Value Only")
                                else:
                                    with open("logs/war.log",'a') as unit_error:
                                        unit_error.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - New Inventory Unit - Maximum 2 Character Allow\n")
                                    print("Maximum 2 Character Allow")
                            update["inventory_unit"]=new_inventory_unit
                            with open("database/inventory.json",'w') as new_unit:
                                json.dump(update_inventory_data,new_unit,indent=4)
                            with open("logs/inventory.log",'a') as update_data_inventory:
                                update_data_inventory.write(f"[{str(datetime.now())}] [INFO] - Update Inventory - Inventory Unit Update Successful\n")
                            print("Inventory Unit Update Successful")
                            break
                        elif inventory_choice=="5":
                            while True:
                                try:
                                    new_inventory_price=int(input("Enter New Inventory Price: "))
                                    if new_inventory_price>0:
                                        break
                                    else:
                                        with open("logs/war.log",'a') as price_inventory:
                                            price_inventory.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - New Inventory Price - Price 0 to Greater\n")
                                        print("Price 0 to Greater")
                                except ValueError:
                                    with open("logs/war.log",'a') as update_intger:
                                        update_intger.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - New Inventory Price - Integer Value Only\n")
                                    print("Integer Value Only")
                            update["inventory_price"]=new_inventory_price
                            with open("database/inventory.json",'w') as new_price:
                                json.dump(update_inventory_data,new_price,indent=4)
                            with open("logs/inventory.log",'a') as error_data_inventory:
                                error_data_inventory.write(f"[{str(datetime.now())}] [INFO] - Update Inventory - Inventory Price Update Successful\n")
                            print("Inventory Price  Update Successful")
                            break
                        elif inventory_choice=="6":
                            with open("logs/inventory.log",'a') as back_inventory:
                                back_inventory.write(f"[{str(datetime.now())}] [INFO] - Update Inventory - Program Back Successful\n")
                            print("Program Back Successful")
                            self.menu()
                        else:
                            with open("logs/war.log",'a') as inventory_choice_error:
                                inventory_choice_error.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - Invalid Your Inventory Update Choice\n")
                            print("Invalid Your Inventory Update Choice")
                else:
                    with open("logs/war.log",'a') as update_inventory_error:
                        update_inventory_error.write(f"[{str(datetime.now())}] [WARNING] - Update Inventory - inventory.json: Inventory Data is not found\n")
                    print("Inventory Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as inventory:
                inventory.write(f"[{str(datetime.now())}] [ERROR] - Update Inventory - inventory.json: File is not found\n")
            print("Data is not found")
            return
    def delete_inventory(self):
        try:
            with open("database/inventory.json",'r') as delete_inventory_file:
                delete_inventory_data=json.load(delete_inventory_file)
                print("==============================================================================")
                print("*                              Delete Inventory                              *")
                print("==============================================================================")
                while True:
                    delete_inventory_id=input("Enter Inventory ID: ")
                    if delete_inventory_id:
                        break
                    else:
                        with open("logs/war.log",'a') as id_inventory:
                            id_inventory.write(f"[{str(datetime.now())}] [WARNING] - Delete Inventory - Inventory ID - Invalid Delete Inventory ID\n")
                        print("Invalid Delete Inventory ID")
                for delete in delete_inventory_data:
                    if delete["inventory_id"]==delete_inventory_id:
                        print("=============================================")
                        print("*            Delete Option Menu             *")
                        print("=============================================")
                        print("1. yes")
                        print("2. no")
                        delete_option_choice=input("Enter Delete Option Choice: ")
                        if delete_option_choice=="yes":
                            delete_inventory_data.remove(delete)
                            with open("database/inventory.json",'w') as delete_inventory:
                                json.dump(delete_inventory_data,delete_inventory,indent=4)
                            with open("logs/inventory.log",'a') as delete_errro:
                                delete_errro.write(f"[{str(datetime.now())}] [INFO] - Delete Inventory - Inventory Delete Successful\n")
                            print("Inventory Delete Successful")
                            break
                        elif delete_option_choice=="no":
                            with open("logs/inventory.log",'a') as daata_errr:
                                daata_errr.write(f"[{str(datetime.now())}] [INFO] - Delete Inventory - Delete Cancelled Successful\n")
                            print("Delete Cancelled Successful")
                            return
                        else:
                            with open("logs/war.log",'a') as delete_option:
                                delete_option.write(f"[{str(datetime.now())}] [WARNING] - Delete Inventory - Delete Option Menu - Invalid Your Delete Option Menu Choice\n")
                            print("Invalid Your Delete Option Menu Choice")
                else:
                    with open("logs/war.log",'a') as delete_inventory_error:
                        delete_inventory_error.write(f"[{str(datetime.now())}] [WARNING] - Delete Inventory - inventory.json: Inventory Data is not found\n")
                    print("Inventory ID Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as delete_data:
                delete_data.write(f"[{str(datetime.now())}] [ERROR] - Delete Inventory - inventory.json: File is not found\n")
            print("Data is not found")
            return
    def low_stock_inventory(self):
        try:
            with open("database/inventory.json",'r') as low_stock_inventory_file:
                low_stock_inventory_data=json.load(low_stock_inventory_file)
                print("=============================================================================================================")
                print("*                                            Low Stock Inventory                                            *")
                print("=============================================================================================================\n")
                count_inventory=0
                print("Inventory ID:         Inventory Name           Category            Quantity            Unit            Status")
                print("-------------------------------------------------------------------------------------------------------------")
                
                for low_stock in low_stock_inventory_data:
                    if low_stock["inventory_quantity"] > 0 and low_stock["inventory_quantity"] <=1:
                        count_inventory+=1
                        print(
                            str(count_inventory).ljust(3) + str(low_stock["inventory_id"]).ljust(23),
                            str(low_stock["inventory_name"]).ljust(20),
                            str(low_stock["inventory_category"]).ljust(20),
                            str(low_stock["inventory_quantity"]).ljust(17),
                            str(low_stock["inventory_unit"]).ljust(12),
                            str(low_stock["inventory_stock_status"])
                        )   
                if count_inventory==0:
                    with open("logs/war.log",'a') as low_data:
                        low_data.write(f"[{str(datetime.now())}] [WARNING] - Low Stock Inventory - inventory.json: Inventory Data is not found\n")
                    print("Inventory Data is not found") 
        except FileNotFoundError:
            with open("logs/error.log",'a') as low_error:
                low_error.write(f"[{str(datetime.now())}] [ERROR] - Low Stock Inventory - inventory.json: File is not found\n")
            print("Data is not found")
            return
    def out_of_stock_inventory(self):
        try:
            with open("database/inventory.json",'r') as out_of_stock_inventory_file:
                out_of_stock_inventory_data=json.load(out_of_stock_inventory_file)
                print("=============================================================================================================")
                print("*                                           Out Of Stock Inventory                                          *")
                print("=============================================================================================================\n")
                count_inventory=0
                print("Inventory ID:         Inventory Name           Category            Quantity            Unit            Status")
                print("-------------------------------------------------------------------------------------------------------------")
                for out_of_stock in out_of_stock_inventory_data:
                    if out_of_stock["inventory_quantity"]==0:
                        count_inventory+=1
                        print(
                            str(out_of_stock["inventory_id"]).ljust(25),
                            str(out_of_stock["inventory_name"]).ljust(20),
                            str(out_of_stock["inventory_category"]).ljust(22),
                            str(out_of_stock["inventory_quantity"]).ljust(17),
                            str(out_of_stock["inventory_unit"]).ljust(12),
                            str(out_of_stock["inventory_stock_status"])
                        )
                if count_inventory==0:
                    with open("logs/war.log",'a') as out_error:
                        out_error.write(f"[{str(datetime.now())}] [WARNING] - Out Of Stock Inventory - inventory.json: Out Of Stock Inventory Data is not found\n")
                    print("Out Of Stock Data is not found")    
        except FileNotFoundError:
            with open("logs/error.log",'a') as not_data_error:
                not_data_error.write(f"[{str(datetime.now())}] [ERROR] - Out Of Stock Inventory - inventory.json: File is not found\n")
            print("Data is not found")
            return
    def menu(self):
        while True:
            print("==========================================================")
            print("*                     Inventory Menu                     *")
            print("==========================================================")
            print("1. Add Inventory")
            print("2. View Inventory")
            print("3. Update Inventory")
            print("4. Delete Inventory")
            print("5. Low Stock Inventory")
            print("6. Out of Stock Inventory")
            print("7. Back")
            choice=input("Enter Your Choice: ")
            if choice=="1":
                self.add_inventory()
            elif choice=="2":
                self.view_inventory()
            elif choice=="3":
                self.update_inventory()
            elif choice=="4":
                self.delete_inventory()
            elif choice=="5":
                self.low_stock_inventory()
            elif choice=="6":
                self.out_of_stock_inventory()
            elif choice=="7":
               print("Program Back Successful")
               break
            else:
                print("Invalid You Choice")
# obj=Inventory()
# obj.menu()