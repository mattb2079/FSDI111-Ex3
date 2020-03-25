"""
Program: Warehouse inventory control system
Functionality
    - Register items to the calatog
        id (auto generate)
        title
        category
        price
        stock
    - Display Catalog
    - Display Catalog (no stock items)
    - Update the stock of a selected item


    - Save catalog
    - Retrieve catalog

    - Print total value of current stock

"""

from Menu import print_menu, print_header
from Item import Item
import os
import pickle

catalog = []
id_count = 1
data_file = "catalog.data"

# methods declaration

def clear():
    return os.system('cls')

def save_catalog():
    global data_file
    writer = open(data_file, "wb") # open a file to write binary
    pickle.dump(catalog, writer)
    writer.close()
    print(" Data saved!")

def read_catalog():
    global data_file
    global id_count

    try:
        reader = open(data_file, "rb") # open the file to read binary
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[-1] # get the last element from the array
        id_count = last.id + 1
        how_many = len(catalog)
        print(" Loaded " + str(how_many) + " Items")
    except:
        # when the above code crashes, we go here
        print(" *Error loading data!")

def register_item():
    global id_count # import the global variable into the function scope
    print_header(' Register New Item')
    title = input('Please input title: ')
    category = input('Please input Category: ')
    price = float (input('Please input Price: '))
    stock = int(input('Please input Stock: '))

    # do validations here

    #create the object
    new_item = Item() # < - how to create an object of a class
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock
    print(new_item)
    
    id_count += 1
    catalog.append(new_item)
    print(" Item created!")

def display_catalog():
    num_items = len(catalog) # <- get length of array or string
    print_header(' Your Catalog contains ' + str(num_items) + ' Items')
    print("|ID  |"
    + " Title ".ljust(20)
    + " | " + "Category".center(15)
    + " | " + "Price".center(9)
    + " | " + "Stock".rjust(5))
    print('-' * 80)

    for item in catalog:
        print(str(item.id).ljust(4)
        + " | " + item.title.ljust(19)
        + " | " + item.category.center(15)
        + " | " + str(item.price).center(9)
        + " | " + str(item.stock).rjust(5))
    
    print('-' * 80)

def print_zero_stock():
    print_header(' Items are out of stock')
    print(" Title ".ljust(20)
    + " | " + "Category".center(15)
    + " | " + "Price".center(9)
    + " | " + "Stock".rjust(5))
    print('-' * 80)

    for item in catalog:
        if (item.stock == 0):
            print(" " + item.title.ljust(19)
            + " | " + item.category.center(15)
            + " | " + str(item.price).center(9)
            + " | " + str(item.stock).rjust(5))
    
    print('-' * 80)

def update_stock():
    # show all the items
    # ask the user to choose one
    # ask for the new stock value
    # update the stock value of the selected item
    display_catalog()
    selected = int(input('please select the ID to update: '))

    found = False
    for item in catalog:
        if(item.id == selected):
            new_stock = input(' Please input a new stock value: ')
            item.stock = int(new_stock)
            found = True
            print(' Stock updated!')
    
    if(found == False):
        print('** Error: Selected ID does not exist, try again')

def print_total_value():
    total_value = 0
    for item in catalog:
        line_value = item.price * item.stock
        total_value += line_value
    print(" Total value of all items: $" + str(total_value))

# load data
read_catalog()

# loop to display menu
opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Select an option: ')

    if(opc == '1'):
        register_item()
        save_catalog()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        print_zero_stock()
    elif(opc == '4'):
        update_stock()
        save_catalog()
    elif(opc == '5'):
        print_total_value()

    input('Press Enter to continue...')