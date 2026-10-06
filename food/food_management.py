import json
import datetime
import uuid


class Food_Management:
    def add_food(self):
        print("============================================================")
        print("*                        Add Food                          *")
        print("============================================================")
        while True:
            category=input("Enter Food Category (Chinese/Fast Food/Italian/North Indian/Beverage): ").strip().title()
            if len(category)>2:
                if category.replace(" ","").isalpha():
                    break
                else:
                    with open("logs/war.log",'a') as category_error:
                        category_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Food - Category: Alpha Value Only\n")
                    print("Alpha Value Only")
            else:
                with open("logs/war.log",'a') as allow_three:
                    allow_three.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Food - Category - Maximum 3 Character Allow\n")
                print("Maximum 3 Character Allow")
        while True:
            food_name=input("Enter Food Name: ").strip().title()
            if len(food_name)>2:
                if food_name.replace(" ","").isalpha():
                    break
                else:
                    with open("logs/war.log",'a') as food_name_error:
                        food_name_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Food - Food Name: Alpha Value Only\n")
                    print("Alpha Value Only")
            else:
                with open("logs/war.log",'a') as allow_four:
                    allow_four.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Food - Food Name - Maximum 3 Character Allow\n")
                print("Maximum 3 Character Allow")
        while True:
            try:
                half_size_price=int(input("Enter Half Size Price: "))
                if half_size_price>0:
                    break
                else:
                    with open("logs/war.log",'a') as price_error:
                        price_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Food - Half Size Price - Price 0 to Greater\n")
                    print("Price 0 to Greater")
            except ValueError:
                with open("logs/war.log",'a') as half_size:
                    half_size.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Food - Half Size Price: Integer Value Only\n")
                print("Integer Value Only")
                return
        while True:
            try:
                full_size_price=int(input("Enter Full Price: "))
                if full_size_price>0:
                    break
                else:
                    with open("logs/war.log",'a') as full_price:
                        full_price.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Food - Full Size Price - Price 0 to Greater\n")
                    print("Price 0 to Greater")
            except ValueError:
                with open("logs/war.log",'a') as full_size:
                    full_size.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Food - Full Size Price: Intger Value Only\n")
                print("Integer Value Only")
                return 
        food_id="F" + str(uuid.uuid4())[:3] 
        food={
            "id":food_id,
            "category":category,
            "food_name":food_name,
            "half_size_price":half_size_price,
            "full_size_price":full_size_price,
        }
        try:
            with open("database/food.json",'r') as file:
                food_data=json.load(file)
        except FileNotFoundError:
            food_data={
                "Chinese":[],
                "Fast Food":[],
                "Italian":[],
                "North Indian":[],
                "Beverage":[]
            }
        for category_data in food_data:
            for food_data_item in food_data[category_data]:
                if food_data_item["food_name"].lower() == food_name.lower():
                    with open("logs/war.log",'a') as food_error:
                        food_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Food - Food Already Added\n")
                    print("Food Already Added")
                    return
        try:
            food_data[category].append(food)
        except KeyError:
            with open("logs/war.log",'a') as invalid:
                invalid.write(f"[{str(datetime.datetime.now())}] [WARNING] - Add Food - Invalid Food Category\n")
            print("Invalid Food Category")
            return
        with open("database/food.json",'w') as file:
            json.dump(food_data,file,indent=4)
        with open("logs/food.log",'a') as food_add:
            food_add.write(f"[{str(datetime.datetime.now())}] [INFO] - Food added in Successfully\n")
        print("Food Added in Successful")
    def view_food(self):
        try:
            with open("database/food.json",'r') as file:
                food_data=json.load(file)
            print("------------------------------------------------------------------------------------------------------------")
            print("============================================================================================================")
            print("*                                               View Menu                                                  *")
            print("============================================================================================================\n")
            for category,user in food_data.items():
                count=0
                print(f"\n\n                                            ||-+-{category}-+-||                                        ")
                print("------------------------------------------------------------------------------------------------------------")
                print("Food Name                                    Half Size Price                                 Full Size Price")
                print("------------------------------------------------------------------------------------------------------------")
                for food in user:
                    count+=1
                    print(
                        str(count).ljust(2),food["food_name"].ljust(48) +
                        ("₹" + str(food["half_size_price"])).ljust(48) +
                        ("₹" + str(food["full_size_price"])).ljust(15)
                    )
                print("____________________________________________________________________________________________________________")
        except FileNotFoundError:
            with open("logs/error.log",'a') as view_food:
                view_food.write(f"[{str(datetime.datetime.now())}] [ERROR] View Food - food.json: File is not found\n")
            print("Data is Not Found")
            return
    def update_food(self):
        try:
            with open("database/food.json",'r') as food_file:
                food_data=json.load(food_file)
                print("============================================================")
                print("*                       Update Food                        *")
                print("============================================================")
                count_food=0
                while True:
                    catetory=input("Enter Food Category (Chinese/Fast Food/Italian/North Indian/Beverage): ").strip().title()
                    if len(catetory)>2:
                        if catetory.replace(" ","").isalpha():
                            break
                        else:
                            with open("logs/war.log",'a') as category_error:
                                category_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Food - Category - Alpha Value Only\n")
                            print("Alpha Value Only")
                    else:
                        with open("logs/war.log",'a') as file_cate:
                            file_cate.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Food - Category - Maximum 3 Character Allow\n")
                        print("Maximum 3 Character Allow")
                for food in food_data[catetory]:
                    count_food+=1
                    print(count_food,".",food["food_name"])
                while True:
                    try:
                        choice=int(input("Enter Your Choice: "))
                        break
                    except ValueError:
                        with open("logs/war.log",'a') as intger_error:
                            intger_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Food - Choice - Integer Value Only\n")
                        print("Integer Value Only")
                selected_food=0
                for food in food_data[catetory]:
                    selected_food+=1
                    if selected_food==choice:
                        print("============================================================")
                        print("*                     Update Food Menu                     *")
                        print("============================================================")
                        print("1. Update Food Name")
                        print("2. Update Half Size Price")
                        print("3. Update Full Size Price")
                        print("4. Back")
                        print("5. Exit")
                        choice=input("Enter Your Choice: ")
                        if choice=="1":
                            while True:
                                new_food_name=input("Enter Update Food Name: ").strip().title() 
                                if len(new_food_name)>2:
                                    if new_food_name.replace(" ","").isalpha():
                                        break
                                    else:
                                        with open("logs/war.log",'a') as new_food_allow:
                                            new_food_allow.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Food - New Food Name - Alpha Value Only\n")
                                        print("Alpha Value Only")
                                else:
                                    with open("logs/war.log",'a') as name_allow:
                                        name_allow.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Food - New Food Name - Maximum 3 Character Allow\n")
                                    print("Maximum 3 Character Allow")
                            food["food_name"]=new_food_name
                            with open("database/food.json",'w') as new_food_write:
                                json.dump(food_data,new_food_write,indent=4)
                            with open("logs/food.log",'a') as new_food_error:
                                new_food_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Update Food - Food Name Update Successful\n")
                            print("Food Name Update Successful")
                        elif choice=="2":
                            while True:
                                try:
                                    new_half_size_price=int(input("Enter New Half Size Price: "))
                                    if new_half_size_price>0:
                                        break
                                    else:
                                        with open("logs/war.log",'a') as new_half_price:
                                            new_half_price.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Food - New Half Size Price - Price 0 to Greater\n")
                                        print("Price 0 to Greater")
                                except ValueError:
                                    with open("logs/war.log",'a') as new_price:
                                        new_price.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Food - New Half Size Price - Integer Value Only\n")
                                    print("Integer Value Only")
                            food["half_size_price"]=new_half_size_price
                            with open("database/food.json",'w') as new_half_price_write:
                                json.dump(food_data,new_half_price_write,indent=4)
                            with open("logs/food.log",'a') as half_size_error:
                                half_size_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Update Food - Half Size Price Update Successful\n")
                            print("Half Size Price Update Successful")
                        elif choice=="3":
                            while True:
                                try:
                                    new_full_size_price=int(input("Enter New Full Size Price: "))
                                    if new_full_size_price>0:
                                        break
                                    else:
                                        with open("logs/war.log",'a') as full_size_price:
                                            full_size_price.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Food - New Full Size Price - Price 0 to Greater\n")
                                        print("Price 0 to Greater")
                                except ValueError:
                                    with open("logs/war.log",'a') as full_price:
                                        full_price.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Food - New Full Size Price - Integer Value Only\n")
                                    print("Integer Value Only")
                            food["full_size_price"]=new_full_size_price
                            with open("database/food.json",'w') as new_full_price_write:
                                json.dump(food_data,new_full_price_write,indent=4)
                            with open("logs/food.log",'a') as full_size_error:
                                full_size_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Update Food - Full Size Price Update Successful\n")
                            print("Full Size Price Update Successful")
                        elif choice=="4":
                            with open("logs/food.log",'a') as back_program:
                                back_program.write(f"[{str(datetime.datetime.now())}] [INFO] - Update Food - Program Back Successful\n")
                            print("Program Back Successful")
                            self.menu()
                        elif choice=="5":
                            with open("logs/food.log",'a') as close:
                                close.write(f"[{str(datetime.datetime.now())}] [INFO] - Update Food - Restaurant Management System - Update Food - Close Successful.\n")
                            print("Restaurant Management System - Update Food - Close Successful.\n")
                            break
                        else:
                            with open("logs/war.log",'a') as food_choice:
                                food_choice.write(f"[{str(datetime.datetime.now())}] [WARNING] - Update Food - Update Food Menu - Invalid Your Update Food Choice\n")
                            print("Invalid Your Update Food Choice: ")
                            break
        except FileNotFoundError:
            with open("logs/error.log",'a') as file_error:
                file_error.write(f"[{str(datetime.datetime.now())}] [ERROR] - Update Food - food.json: File is not found\n")
            print("Data is not found")
            return
    def delete_food(self):
        try:
            with open("database/food.json",'r') as delete_food_file:
                delete_food_data=json.load(delete_food_file)
                print("============================================================")
                print("*                       Delete Food                        *")
                print("============================================================")
                delete_count=0
                while True:
                    category=input("Enter Food Category (Chinese/Fast Food/Italian/North Indian/Beverage):").strip().title()
                    if len(category)>2:
                        if category.replace(" ","").isalpha():
                            break
                        else:
                            with open("logs/war.log",'a') as delete_category_error:
                                delete_category_error.write(f"[{str(datetime.datetime.now())}] [WARNING] - Delete Food - Category - Alpha Value Only\n")
                            print("Alpha Value Only")
                    else:
                        with open("logs/war.log",'a') as category_allow:
                            category_allow.write(f"[{str(datetime.datetime.now())}] [WARNING] - Delete Food - Categoryy - Maximum 3 Character Allow\n")
                        print("Maximum 3 Character Allow")
                for delete_category in delete_food_data[category]:
                    delete_count+=1
                    if delete_category["category"]==category:
                        print(delete_count,".",delete_category["food_name"])
                while True:
                    try:                        
                        choice=int(input("Enter Your Choice: "))
                        break
                    except ValueError:
                        with open("logs/war.log",'a') as delete_integer:
                            delete_integer.write(f"[{str(datetime.datetime.now())}] [WARNING] - Delete Food - Choice - Integer Value Only\n")
                        print("Integrer Value Only")
                delete_count=0
                for delete in delete_food_data[category]:
                    delete_count+=1
                    if delete_count==choice:
                        food_name=delete["food_name"]
                        delete_food_data[category].remove(delete)
                        with open("database/food.json",'w') as delete_file:
                            json.dump(delete_food_data,delete_file,indent=4)
                        with open("logs/food.log",'a') as delete_error:
                            delete_error.write(f"[{str(datetime.datetime.now())}] [INFO] - Delete Food - Food Delete Successful\n")
                        print("Food Delete Successful")
                        break
                else:
                    with open("logs/war.log",'a') as delete_food:
                        delete_food.write(f"[{str(datetime.datetime.now())}] [WARNING] - Delete Food - food.json: Food Data is not found\n")
                    print("Food Data is not found")
        except FileNotFoundError:
            with open("logs/error.log",'a') as food_data_delete:
                food_data_delete.write(f"[{str(datetime.datetime.now())}] [ERROR] - Delete Food - food.json: File is not found\n")
            print("Data is not found")
            return
    def menu(self):
        while True:
            print("===========================================================")
            print("*                        Food Menu                        *")
            print("===========================================================")
            print("1. Add Food")
            print("2. View Menu")
            print("3. Update Food")
            print("4. Delete Food")
            print("5. Back")
            choice=input("Enter Your Choice: ")
            if choice=="1":
                self.add_food()
            elif choice=="2":
                self.view_food()
            elif choice=="3":
                self.update_food()
            elif choice=="4":
                self.delete_food()
            elif choice=="5":
                print("Program Back Successful")
                break
            else:
                print("Invalid Your Choice")
# obj=Food_Management()
# obj.menu()