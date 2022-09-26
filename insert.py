import json


def show_list(items):
    print("list:\n")
    print("name\tprice\n")
    print("-----------\n")
    for item in items:
        print(f"{item['name']}\t{item['price']}")
    print("\n\n")


def insert_item(items, name, price):
    item = {"name": name, "price": price}
    items.append(item)
    print(f"Item {name} added to the list")


def get_item_input():
    name = input("Enter name of item: ")
    price = input("Enter price of item: ")
    return name, price


def read_json_file(filename):
    with open(filename, "r") as f:
        items = json.load(f)
    return items


def update_json_file(filename, items):
    with open(filename, "w") as f:
        json.dump(items, f)


def main():
    items = read_json_file("items.json")
    while True:
        choice = int(
            input("1. Insert item\n2. Show list\n3. Save & Exit\n\nEnter your choice: ")
        )
        if choice == 1:
            name, price = get_item_input()
            insert_item(items, name, price)
        elif choice == 2:
            show_list(items)
        elif choice == 3:
            update_json_file("items.json", items)
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
