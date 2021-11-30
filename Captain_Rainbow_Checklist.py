# Some things to consider:
# There are seven colors in the rainbow, and seven items of clothing to color.
# He can never wear the same color on any of his items. If he is wearing a purple shoe, he cannot wear a second purple shoe.
# He must wear every color of the rainbow each day

checklist = []

# CRUD 

def create(item) :
    checklist.append(item)

    return "Added {} to checklist".format(item)

def read(index) :
    return checklist[index]

def update(index, item) :
    old = checklist[index]
    checklist[index] = item

    return "Changed {} to {}".format(old, item)

def destroy(index) :
    removed = checklist[index]
    checklist.pop(index)

    return "Removed {} from checklist".format(removed)


# Helper functions

# View all items in checklist
def list_all() :

    i = 0

    for item in checklist :
        print(i, item)
        i += 1

# Adding √ to items in checklist
def completed() :
    for item in checklist :
        print("√", item)

# User input
def user_input(prompt) :
    user_in = input(prompt)
    return user_in




# User choosing functions
def user_choice() :

    status = True

    while status :

        function_code = user_input("\nWhich function would you like to use? Enter C for create, R for read, U for update, D for destroy, A to view all items currently in the checklist and S to select an item with a checkmark : ")

        # Create item
        if function_code == "C" or 'c':
            input_item = user_input("Enter item to create: ")

            create(input_item)

            continue


        # Read item
        elif function_code == "R" or 'r':
            item_index = user_input("Enter index Number to view: ")

            read(item_index)

            continue

        # Update item
        elif function_code == "U" or 'u':
            update_index = user_input("Enter index Number to update: ")
            update_item = user_input("Enter item to update: ")

            update(int(update_index, update_item))

            continue

        elif function_code == "D" or 'd':
            delete_index = user_input("Enter index Number to delete item: ")

            destroy(int(delete_index))

            continue

        elif function_code == "A" or 'a':
            list_all()

            continue

        elif function_code == "S" or 's':
            check_index = user_input("Enter index Number to check off: ")

            completed(int(check_index))

            continue

        else :
            end = user_input("Do you wish to quit? Enter Y for yes or N for no. ")

            if end == "Y" or end == 'y':
                print(checklist)
                editing = False
        
            else : 
                
                continue

    



# Testing   

def test() :
    # create("purple sox")
    # create("red cloak")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(1)

    # print(read(0))
    # # print(read(1))

    # list_all()
    # completed()
    # user_input("Julia")

    user_choice()

test()