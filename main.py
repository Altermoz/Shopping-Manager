def display_menu():
    print("\nWelcome to the Shopping List Manager!")
    print("1. Add item to list")
    print("2. Remove item from list")
    print("3. Clear list")
    print("4. Display list")
    print("5. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")

        elif choice == '2':
            if not shopping_list:
                print(f"The shopping list is empty. Nothing to remove.")
            else:
                try:
                    index = int(input("Enter the index of the item to remove: ")) - 1
                    removed_item = shopping_list.pop(index)
                    print(f"{removed_item} has been removed from the shopping list.")
                except (IndexError, ValueError):
                    print("Invalid index. Please try again.")
        
        elif choice == '3':
            shopping_list.clear()
            print("The shopping list has been cleared.")

        elif choice == '4':
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Current Shopping List: ")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
        
        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()