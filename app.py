menu = """Please select an option
1. Add a new journal entry
2. View existing entries
3. Exit journal

Your selection: """

welcome = "Welcome to your python journal!\n" 

print(welcome)

user_input = input(menu)

while user_input := input(menu) != "3":
    if user_input == "1":
        print("Adding...")
    elif user_input == "2":
        print("Viewing...")
    else: 
        print("Error")        