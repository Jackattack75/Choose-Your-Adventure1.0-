# programmer: Jack Sutton
# Date: 3/15/2024
# Title: Choose Your Adventure

import random

class Character:
    def __init__(self, name, health=100, shield=50):
        self.name = name
        self.health = health
        self.shield = shield
        self.weapon = None

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        if self.weapon:
            damage = random.randint(10, 20) + self.weapon.damage
            enemy.defend(damage)
            print(f"{self.name} attacks {enemy.name} with {self.weapon.name} causing {damage} damage!")
        else:
            print(f"{self.name} has no weapon to attack {enemy.name}!")

    def defend(self, damage):
        if self.shield > 0:
            self.shield -= damage
            if self.shield < 0:
                self.health += self.shield
                self.shield = 0
        else:
            self.health -= damage

class Enemy(Character):
    def __init__(self, name, health=100, shield=0):
        super().__init__(name, health, shield)

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Story:
    def __init__(self):
        self.current_character = None
        self.current_enemy = None

    def start(self):
        print("You wake up groggily, your head pounding, to the sound of distant screams.")
        print("Rubbing your eyes, you realize you're slouched over a desk in a dimly lit classroom.")
        print("The room is empty, eerie, and silent except for the faint scratching at the door.")
        print("You push open the door to find chaos outside.")
        print("The world has been overrun by a mysterious plague, turning people into zombies.")
        print("You need to find a way out and survive.")
        name = input("Enter your character's name: ")
        self.current_character = Character(name)
        self.outside_school()

    def outside_school(self):
        print("You step outside the school into a world engulfed in chaos.")
        print("1. Head towards the city center.")
        print("2. Search for supplies in nearby buildings.")
        print("3. Hide in the school and fortify your position.")
        choice = input("What will you do? (1/2/3): ")

        if choice == "1":
            self.city_center()
        elif choice == "2":
            self.search_supplies()
        elif choice == "3":
            self.fortify_school()
        else:
            print("Invalid choice.")
            self.outside_school()

    def city_center(self):
        # This part of the story can be expanded further
        print("You decide to head towards the city center, hoping to find survivors or assistance.")
        print("As you make your way through the streets, you encounter hordes of zombies.")
        print("You must fight your way through or find another route.")

    def search_supplies(self):
        # This part of the story can be expanded further
        print("You choose to search for supplies in nearby buildings, scavenging for food, weapons, and shelter.")
        print("Be cautious, as zombies may be lurking in the shadows.")

    def fortify_school(self):
        # This part of the story can be expanded further
        print("You decide to fortify your position within the school, setting up barricades and traps.")
        print("You must defend your stronghold against incoming waves of zombies.")

# Starting the game
game = Story()
game.start()