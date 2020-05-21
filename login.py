import sys
def add_user(db):
    print("Please enter your username and password separated by a space")
    credentials = input()
    credentials = credentials.split(' ')
    db[credentials[0]] = credentials[1]
    print(f'Added  {credentials[0]}')

def show_users(db):
    print("List of all registered users:")
    for name, password in db.items():
        print (f'Username:\t{name}\t{password}\n')

db = {}
while True:
    option = 0
    while option not in [1,2,3,4]:
        print('Please select one of the following options:\n\
            1 to login\n\
            2 to create a new account\n\
            3 to see the list of all users\n\
            4 to exit')
        option=int(input())

    if option == 1 :
        print("Please enter your username and password separated by a space")
        user_input = input().split(' ')
        if user_input[0] in db.keys():
            if user_input[1] == db[user_input[0]]:
                print(f'Welcome back  {user_input[0]}')
                break
            else:
                print('Credentials not recognized')
                continue
        else:
            print('Credentials not recognized')
            continue
    elif option == 2:
        add_user(db)
    elif option == 3:
        show_users(db)
    else:
        sys.exit
