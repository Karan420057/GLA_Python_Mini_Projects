inventry = {}
while True:
    print("Enter your choice to add or remove or check availability or exit: ")
    ch = input("Add | Remove | Check | Exit : ")
    if ch=='Add':
        key = input("Enter product name: ")
        value = int(input("Enter quantity: "))
        if key in inventry:
            inventry[key] += value
        else:
            inventry[key] = value
    elif ch=='Remove':
        key = input("Enter product name: ")
        value = int(input("Enter quantity you want to remove: "))
        if key in inventry and inventry[key]>(value - 1):
            inventry[key] -= value
        elif key in inventry and inventry[key]<value:
            print(f"There are only {inventry[key]} left in inventry")
        else:
            print("No item with this name found")
    elif ch=='Check':
        key = input("Enter product name: ")
        value = int(input("Enter quantity to check availability: "))
        if key in inventry and inventry[key]>=value:
            print(f"Product is available in required quantitu is: {key} = {inventry[key]}")
        elif key in inventry and inventry[key]<value:
            print(f"Product is present but avaiable quantity is: {inventry[key]}")
        else:
            print("Product is not avaiable")
    elif ch=='Exist':
        break
    else:
        print("Invalid input, proceed again")