import json


def read_json_file(filename):
    with open(filename, 'r') as f:
        items = json.load(f)
    return items


def search(name, items):
    for item in items:
        if item['name'] == name:
            print("Item found!")
            print(f"Item name: {item['name']}")
            print(f"Item price: {item['price']}")
            return
    
    print("Item not found!")


def main():
    items = read_json_file("items.json")
    name = input("Enter item name to be searched: ")
    search(name, items)

main()
