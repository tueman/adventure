import time
import town


def cave():
    while True:
        print('You are at a cave. Inside the cave is a key. To the south is a town.')
        time.sleep(1)
        print('Commands: Pickup   South')
        while True:
            choice = input().lower()
            if choice in ['pickup', 'south']:
                if choice == 'pickup':
                    print('You pickup the key.')
                    town.inventory.append('Key')
                    town.town()
                elif choice == 'south':
                    town.town()
            else:
                print('Unrecognized command. Try again.')
                continue
