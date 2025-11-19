def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    
    item=input('Enter the item to add: ')
    shopping_list.append(item)
    return shopping_list
    

def display_list(shopping_list):
    if not shopping_list:
        print('List is empty')
        return shopping_list
    
    print('Current List:')
    for i , item in enumerate(shopping_list, 1):
        print(f'{i}. {item}')
        
    
    
def remove_item(shopping_list):
    index=int(input('Enter the number of item to remove: '))-1
    shopping_list.pop(index)
    return shopping_list

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item(shopping_list)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_item(shopping_list)
            pass
        elif choice == '3':
            # Display the shopping list
            display_list(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()