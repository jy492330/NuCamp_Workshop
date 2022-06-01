"""
Nucamp
Week 1 workshop Assignment: battlegame.py
Student: Jin Jessica Yang
"""

wizard = "Wizard"
elf = "Elf"
human = "Human"
wizard_hp = 70
elf_hp = 100
human_hp = 150
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_hp = 300
dragon_damage = 50
multiline_str = ("1)   Wizard\n"
                 "2)   Elf\n"
                 "3)   Human")
print(multiline_str)
character = input("Choose your character: ")

while True:
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print(f"You have chosen the character: {character}")
        print("Health: ", my_hp)
        print("damage: ", my_damage)
        print()
        while True:
            dragon_hp = dragon_hp - my_damage
            my_hp = my_hp - dragon_damage
            print(f"The {character} damaged the Dragon!")
            print(f"The Dragon's hitpoints are now: {dragon_hp}\n")
            if dragon_hp <= 0:
                print("The Dragon has lost the battle.")
                break

            print(f'The Dragon strikes back at {character}')
            print(f"The {character}'s hitpoints are now: {my_hp}\n")
            if my_hp <= 0:
                print(f'The {character} has lost the battle.')
                break
        break

    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print(f"You have chosen the character: {character}")
        print("Health: ", my_hp)
        print("damage: ", my_damage)
        print()
        while True:
            dragon_hp = dragon_hp - my_damage
            my_hp = my_hp - dragon_damage
            print(f"The {character} damaged the Dragon!")
            print(f"The Dragon's hitpoints are now: {dragon_hp}\n")
            if dragon_hp <= 0:
                print("The Dragon has lost the battle.")
                break

            print(f'The Dragon strikes back at {character}')
            print(f"The {character}'s hitpoints are now: {my_hp}\n")
            if my_hp <= 0:
                print(f'The {character} has lost the battle.')
                break
        break

    elif character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print(f"You have chosen the character: {character}")
        print("Health: ", my_hp)
        print("damage: ", my_damage)
        print()
        while True:
            dragon_hp = dragon_hp - my_damage
            my_hp = my_hp - dragon_damage
            print(f"The {character} damaged the Dragon!")
            print(f"The Dragon's hitpoints are now: {dragon_hp}\n")
            if dragon_hp <= 0:
                print("The Dragon has lost the battle.")
                break

            print(f'The Dragon strikes back at {character}')
            print(f"The {character}'s hitpoints are now: {my_hp}\n")
            if my_hp <= 0:
                print(f'The {character} has lost the battle.')
                break
        break

    else:
        print("Unknown Character")
        print(multiline_str)
        character = input("Choose your character: ")







