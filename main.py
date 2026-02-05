# main.py

from module import GameCharacter
# TASK:
# Make a prototype game using the GameCharacter class.

# -----------------------------------------
# TODO 1:
# Print a message that welcomes the user to this game.
print("Wellcome to this game player")
# TODO 2:
# Ask the user to name their character and store it in a variable.
print("What is your character's name?")
name = input("name:")

# TODO 1:
# Assign a power and a toughness value to the character.
# (Use any integers you like between 1 and 20.)
import random
power = random.randint(1, 20)
toughness = random.randint(1, 20)
player = GameCharacter(name, power, toughness)

# TODO 2:
# Create a new GameCharacter object for the player.



# TODO 3:
# Create a new GameCharacter object for an enemy.
# The enemy's name can be something like "Goblin" or "Dragon".
# Give the enemy its own power and toughness values.
enemy = GameCharacter("Dragon", 15, 16)

# TODO 4:
# Print both characters' statuses.
print("Round 1 Fight")

print(player.get_status())
print(enemy.get_status())

# TODO 5:
# Print the player's attack message.
# Then make the enemy take damage equal to the player's power.
print("It's", name,"'s turn to attack")
player.attack()
enemy.take_damage(player.power)

# TODO 6:
# Print the enemy's updated status.
print(enemy.get_status())

# TODO 7:
# Print the enemy's attack message.
# Then make the player take damage equal to the enemy's power.
print("It's", enemy.name, "'s turn to attack")
enemy.attack()
player.take_damage(enemy.power)
# TODO 8:
# Print the player's updated status.
print(player.get_status())                      
# TODO 9:
# Update the player's name property to be "Lord " + the original name
player.name = "Lord " + player.name

# TODO 10: 
# Heal the player by 100 hitpoints
player.heal(100)

# TODO 11:
# Print the player's updated status.
print(player.get_status())

# TODO 12:
# Modify the GameCharacter class so a "defeated" message is printed if health goes to 0 or less
if enemy.health <= 0:
    print(f"{enemy.name} has been defeated!")  
elif player.health <= 0:  
    print(f"{player.name} has been defeated!")
# TODO 13:
# Go back and make it so the player gets a random Power and Toughness between 1 and 20.
      
# -----------------------------------------