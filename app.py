from database import add_entry, view_entries

menu = """Please select an option
1. Add a new journal entry
2. View existing entries
3. Exit journal

Your selection: """

welcome = "Welcome to your python journal!\n" 

print(welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        add_entry
    elif user_input == "2":
        view_entries
    else: 
        print("Error")        