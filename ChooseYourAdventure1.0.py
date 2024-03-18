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
        print("Welcome to the Adventure Game!")
        name = input("Enter your character's name: ")
        self.current_character = Character(name)
        self.intro()

    def intro(self):
        print(f"Hello, {self.current_character.name}! You find yourself in a mysterious forest...")
        self.choice1()

    def choice1(self):
        print("You encounter a fork in the road.")
        print("1. Take the left path.")
        print("2. Take the right path.")
        choice = input("What will you do? (1/2): ")

        if choice == "1":
            self.left_path()
        elif choice == "2":
            self.right_path()
        else:
            print("Invalid choice.")
            self.choice1()

    def left_path(self):
        print("You encounter a friendly villager who offers you a sword!")
        self.current_character.weapon = Weapon("Sword", 15)
        print("You received a Sword!")
        self.choice2()

    def right_path(self):
        print("You stumble upon a ferocious bear!")
        self.current_enemy = Enemy("Bear", health=150)
        self.battle()

    def battle(self):
        print(f"A wild {self.current_enemy.name} appears!")
        while self.current_character.is_alive() and self.current_enemy.is_alive():
            print(f"Your health: {self.current_character.health} | Enemy's health: {self.current_enemy.health}")
            print("1. Attack")
            print("2. Run")
            action = input("What will you do? (1/2): ")

            if action == "1":
                self.current_character.attack(self.current_enemy)
                if self.current_enemy.is_alive():
                    self.current_enemy.attack(self.current_character)
            elif action == "2":
                print("You ran away from the battle!")
                break
            else:
                print("Invalid choice.")

        if self.current_character.is_alive():
            print(f"You defeated the {self.current_enemy.name}!")
            print("You continue on your adventure...")
            # Continue the story here
        else:
            print("Game Over - You were defeated!")
            # Option to restart or end the game

# Starting the game
game = Story()
game.start()