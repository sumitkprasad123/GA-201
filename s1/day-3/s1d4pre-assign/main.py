from prettytable import PrettyTable
stock = {
    "1":{
        "name":"samosa",
        "price":20,
        "availability":"yes"
      },
    "2":{
        "name":"chai",
        "price":10,
        "availability":"yes"
    }
}

def show_item():
    table = PrettyTable()
    table.field_names = ["snack_id","items","price","availability"]

    for snack_id,nes_value in stock.items():
        row = [snack_id]
        row.extend(nes_value.values())
        table.add_row(row)

    print(table)    

def add_item():
    snack_id = input("Enter snack ID: ")
    if (snack_id in stock):
        print("snack ID already exists.\n")
        return
    name = input("Enter snack name: ")
    while True:
        try:
            snack_price = float(input("Enter snack price: "))
            break
        except:
            print("Invalid input. Please enter a number for the price.")
    snack = {"name":name,"price":snack_price,"availability":"yes"}
    stock[snack_id] = snack
    print(f"snack {name} added Successfully. \n")


def remove_item():
    snack_id = input("Enter snack Id: ")
    if snack_id in stock:
        del stock[snack_id]
        print(f"Snack with ID {snack_id} removed successfully. \n")
    else:
        print("Snack ID not found. \n")


def update_item(): 
    snack_id = input("Enter snack ID: ")
    if snack_id in stock:
       while True: 
          availability = input("Enter new availability (yes/no): ").lower()
          if availability in ["yes","no"]:
             stock[snack_id]["availability"] = availability
             print(f"Snack with ID {stock[snack_id]['name']} availability updated successfully. \n")
             return
          else:
              print("Invalid input. Please enter 'yes' or 'no'. \n" )
    else: 
       print("Snack ID not found. \n")



def record_sale():
    snack_id = input("Enter snack ID: ")
    if snack_id in stock and stock[snack_id]["availability"]=="yes":
       print(f"sold: {stock[snack_id]['name']}")
       stock[snack_id]['availability'] = 'no'
    else:
       print("Snack is not available for sale.\n")     



def main():
    while True:
        print(f"1. Show Item")
        print(f"2. Add Item")
        print(f"3. Remove Item")
        print(f"4. Update Item")
        print(f"5. Record sale")
        print(f"6. exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_item()
        elif choice == '2':
            add_item() 
        elif choice == '3':
            remove_item() 
        elif choice == '4':
            update_item() 
        elif choice == '5':
            record_sale()
        elif choice == '6':
            break
        else:
            print(f"Invalid option, please try again.\n")    


if __name__ == '__main__' :
    main()
