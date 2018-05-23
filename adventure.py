import time
import sys


# for pause lines
def print_pause(line, pause):
    print(line)
    time.sleep(pause)


print_pause('Welcome to SuperHero Adventure!', 1)
print('Please choose your hero.')
print('Your choices are:\nFire-User\nTelekinesis\nFlying')

# to choose power
while True:
    heroes = ['Fire-User', 'Telekinesis', 'Flying']
    choice = input('Choice: ')
    if choice in heroes:
        break
    else:   # this will loop back to input if they write something different
        print('Whoops! That isn\'t a valid power. Please try again.')
        continue

print('You have chosen', choice + '.')
time.sleep(1)
print('You are a member of "Super Academy", where all the brightest heroes are brought and taught to use their powers '
      'without hurting others.')
time.sleep(1)
print('Today is your first day at the Academy, and you have learned that your power is', choice + '.')
time.sleep(1)
print('You will be tested to the fullest. Immediately you are brought on a mission: save a woman from a burning '
      'building!')
time.sleep(1)
print('You arrive at the scene. The three-story building is lit up with flames and you can hear the woman\'s '
      'screams from the second floor. What do you do?')
time.sleep(1)
print('What do you do?')
print('1 --- Run Away')   # offer choices
if choice == 'Fire-User':
    print('2 --- Enter the building, ignoring the heat of the flames.')
    print('3 --- Scale the side of the building to the second floor.')
elif choice == 'Telekinesis':
    print('2 --- Levitate yourself into the second floor window, using your power to push away the flames.')
    print('3 --- Telekinetically move a nearby fire hose to spray the second floor with water.')
elif choice == 'Flying':
    print('2 --- Fly into the second floor window.')
    print('3 --- Grab a nearby fire hose and fly up, aiming it at the second floor.')
else:
    print('If you see this message, you\'ve actually broken all physics.')

# to choose action
while True:
    action = input('Type the number of the action you want to perform: ')
    if action in ['1', '2', '3']:
        break
    else:
        print('That is not a valid choice.')
        continue

if action == '1':
    print('You have shown that you are not worthy of being a superhero.')
    sys.exit()
else:
    pass

if (choice, action) == ('Fire-User', '2'):
    print('You enter the building. As your body ignores the heat of the scorching flames, you make your way to the '
          'lady in the building. As you carry her out, the on-lookers congratulate you and you are hailed as a hero.')
elif (choice, action) in [('Fire-User', '3'), ('Telekinesis', '2'), ('Flying', '2')]:
    print('You make your way to the second floor, where you are able to retrieve the screaming woman and carry her'
          'back out of the building. As you carry her out, the on-lookers congratulate you and you are hailed as a '
          'hero.')
elif (choice, action) in [('Telekinesis', '3'), ('Flying', '3')]:
    print('You spray the second floor with the hose\'s water. The flames die down, and the nearby firemen are able to '
          'enter the building and rescue the lady. The on-lookers, as well as the firemen, call you a hero and thank '
          'you for your help.')

time.sleep(3)
print('Congratulations. You have proven yourself worthy of your powers and successfully completed your first mission.')
