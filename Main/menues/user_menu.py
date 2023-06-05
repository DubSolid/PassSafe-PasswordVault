from utils.tcolors import tcolors
from functions.item_operations import item_creation
from functions.item_operations import item_retrieval
from functions.item_operations import item_update
from functions.item_operations import item_deletion
from functions.item_operations import item_listing


def user_menu(db, logged_in, username, user_id):
    while logged_in:
        print('Logged in as ' + tcolors.GREEN (f'{username}'))
        print('Please choose an option:')
        print('1. Add a new item to your vault')
        print('2. List your items')
        print('3. Retrieve an item')
        print('4. Update an existing item')
        print('5. Delete an item')
        print('6. Log out of your vault')

        choice = input(tcolors.GREEN('(+) Enter an option: '))

        if not choice:
            continue

        match choice:
            case '1':
                item_creation(db, user_id)
            case '2':
                item_listing(db, user_id)
            case '3':
                item_retrieval(db, user_id)
            case '4':
                item_update(db, user_id)
            case '5':
                item_deletion(db, user_id)
            case '6':
                logout_message = '(-) Logging out...'
                seperator = '-' * len(logout_message)
                print(f'\n{seperator}\n{tcolors.WARNING(logout_message)}\n{seperator}')
                return True
            case _:
                invalid_message = '(-) Invalid option, please try again...'
                seperator = '-' * len(invalid_message)
                print(f'\n{seperator}\n{tcolors.WARNING(invalid_message)}\n{seperator}')


