import time
import cave

inventory = []


def town():
    while True:
        print('You are in a town. To the north is a cave. To the south is the bank.')
        time.sleep(1)
        print('Commands: North   South')
        while True:
            choice = input().lower()
            if choice in ['north', 'south']:
                if choice == 'north':
                    cave.cave()
                elif choice == 'south':
                    if 'Key' in inventory:
                        print('You open the door with your key.')
                        inventory.remove('Key')
                    else:
                        print('The door is locked.')
                        break
            else:
                print('Unrecognized command. Try again.')
                continue
