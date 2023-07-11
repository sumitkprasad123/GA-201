from prettytable import PrettyTable
dish = {
    "1":{
        "name":"samosa",
        "price":20,
        "availability":"no"
      },
    "2":{
        "name":"chai",
        "price":10,
        "availability":"yes"
    },
    "3":{
        "name":"manchurain",
        "price":50,
        "availability":"yes"
    }
}

order = {
     "1":{
          "customer_name":"sumit",
          "dish_ID":[1,2],
          "status":"received"
     },
     "2":{
          "customer_name":"Amit",
          "dish_ID":[3],
          "status":"received"
     }
}

# showing the dish from the dictionary name 'dish'
def show_dish():
   table = PrettyTable()
   table.field_names = ["dish_ID","Dishes","price","availability"]
   for dish_ID,nes_value in dish.items():
        row = [dish_ID]
        row.extend(nes_value.values())
        table.add_row(row)

   print(table) 


# adding the dish in the dictionary  
def add_dish():
     dish_ID = input("enter dish_ID: ")
     if dish_ID in dish:
          print(f"dish_ID {dish_ID} is already exist")
          return
     name = input("Enter dish name: ")
     while True:
          try:
               price = float(input("Enter the price: "))
               break
          except:
               print("Enter price in a number")    
     new_dish = {"name":name,"price":price,"availability":"yes"}
     dish[dish_ID] = new_dish
     print(f"Dish is successfully added")  

# Updating the dish in the dictionary
def update_dish():
     dish_ID = input("Enter the dish_ID: ")
     if dish_ID in dish:
         while True:
              availability = input("Enter availability yes/no: ").lower()
              if availability in ["yes","no"]:
                 dish[dish_ID]["availability"] = availability
                 print(f"Snack with ID {dish[dish_ID]['name']} availability updated successfully. \n")
                 return
              else: 
                 print("Enter input in form of yes/no")
     else:           
          print(f"dish_ID does not exist")    


# Deleting the dish from dictionary
def delete_dish():
     dish_ID = input("Enter the dish_ID: ")
     if dish_ID in dish:
          del dish[dish_ID]
          print(f"dish_ID {dish_ID} is successfully deleted")
          return
     print(f"This dish_ID does not exist")


# showing all the order in form of table
def show_order():
   table = PrettyTable()
   table.field_names = ["order_ID","customer name","dish_ID","status","total price"]
   global total_price
   for k,v in order.items():
       total_price=0
       x = v["dish_ID"]  # it is list of dish_ID
       for j in range(0,len(x)):
           total_price+=dish[str(x[j])]["price"]
       order[k]["price"] = total_price  #adding total price in each order

   for order_ID,nes_value in order.items():
        row = [order_ID]
        row.extend(nes_value.values())
        table.add_row(row)

   print(table) 


# Taking new order and maintaining in order dictionary  
def order_dish():
     dish_ID = input("Enter dish_ID: ")
     if dish_ID in dish:
          if dish[dish_ID]["availability"]=="yes":
            while True:
                order_ID = input("Enter order_ID: ")
                if order_ID in order:
                    print(f"order_ID {order_ID} is already exist")
                    
                    while True:
                        add_more_dish = input("you want to add more dish yes/no: ").lower()
                        if add_more_dish == "yes":
                           order[order_ID]["dish_ID"].append(int(dish_ID))
                           break
                        elif add_more_dish == "no":
                           break
                        else:
                            print("Enter input in form of yes/no")
                    break
                else:
                    customer_name = input("Enter you name Please: ")
                    new_order = {
                        "customer_name":customer_name,
                        "dish_ID":[int(dish_ID)],
                        "status":"received"
                        }
                    order[order_ID] = new_order
                    print(f"{customer_name} your order id Received")
                    dish[dish_ID]["availability"] = "no"
                    break
          else:
              print(f"Sorry this dish is currently not available")
     else:
          print(f"dish_ID {dish_ID} does not exist")


def change_status():
     order_ID = input("Enter order_ID: ")
     if order_ID in order:
         current_status = order[order_ID]["status"]
         print(f"current_status is {current_status}")
       
         while True:
              if current_status == "received":
                 status = "preparing"
                 print(f"Now, your order is 'preparing'")
                 break
              elif current_status == "preparing":
                 status = "ready for pickup" 
                 print(f"Now, your order is 'ready for pickup'")
                 break
              elif current_status == "ready for pickup":
                 status = "delivered"
                 print(f"Now, your order is going to 'delivered'")
                 break
              else:
                 print("your order is already delivered")
                 return
       
         order[order_ID]["status"] = status
         print(f"status of order_ID {order_ID} is changed successfully")
     else:
         print(f"order_ID {order_ID} does not exist")    


# main function to handle operations by the staff of Zesty Zomato 
def main():
     while True:
          print(" ")
          print("1. show all dishes")
          print("2. add new dish")
          print("3. update dish")
          print("4. delete dish")
          print("5. show orders")
          print("6. place order")
          print("7. change status of order")
          print("8. exit")
          choice = input("Enter your choice: ")
           
          if choice == '1':
               show_dish()
          elif choice == '2':
               add_dish()
          elif choice == '3':
               update_dish()
          elif choice == '4':
               delete_dish()
          elif choice == "5":
               show_order()     
          elif choice == '6':
               order_dish()
          elif choice == '7':
               change_status()        
          elif choice == '8':
               break
          else:
               print(f"Enter valid choice. \n")                         

if __name__ == '__main__':
     main()