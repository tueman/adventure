import time
import random
import Weapon_Generator
import Monster_Generator

playerweapon = Weapon_Generator.Sword()
playerhealth = 20
monster = Monster_Generator.Monster()
monsterhealth = monster.health


def attack():
    global monsterhealth
    damage = playerweapon.damage
    monsterhealth -= random.randint(*damage)


def monsterattack():
    global playerhealth
    monsterdamage = monster.damagerange
    playerhealth -= random.randint(*monsterdamage)
    if playerhealth <= 0:
        print('You have died.')


print('Uh oh, a ' + monster.name + ' has attacked you! Fortunately, you have a ' + playerweapon.name + ' to defend'
      ' yourself!')
time.sleep(2)
while True:
    choice = input('Will you attack?')
    if choice in ('y', 'Y', 'ye', 'yes', 'Yes', 'attack', 'Attack'):
        attack()
        if monsterhealth <= 0:
            print('\nCongratulations! You have won!')
            break
        else:
            print('\nThe ' + str(monster.name) + ' has ' + str(monsterhealth) + ' health left!')
            monsterattack()
            if playerhealth <= 0:
                break
            else:
                print('You only have ' + str(playerhealth) + ' health left!')
    else:
        print('Oops! You didn\'t say yes! Try again.')
        continue
