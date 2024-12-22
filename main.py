import random
import lists
import tkinter as tk
import pygame

class game_state:
    #defines a class of game_state with a turn counter, warband, and missions
    def __init__(self, turn, warband, missions):
        self.turn = turn
        self.warband = warband
        self.missions = missions
    def __str__(self):
        #returns a string with the turn, warband, and missions of the game_state
        return "Turn: " + str(self.turn) + "\nWarband: " + str(self.warband) + "\nMissions: " + str(self.missions)
    def change_turn(self, turn):
        #changes the turn of the game_state
        self.turn = turn
    def change_warband(self, warband):
        #changes the warband of the game_state
        self.warband = warband
    def change_missions(self, missions):
        #changes the missions of the game_state
        self.missions = missions
    def add_mission(self, mission):
        #adds a mission to the game_state
        self.missions.append(mission)
    def remove_mission(self, mission):
        #removes a mission from the game_state
        self.missions.remove(mission)

class mission:
    #defines a class of mission with a type, serverity(difficulty), reward, and a type of foe
    def __init__(self, type, severity, reward, foe):
        self.type = type
        self.severity = severity
        self.reward = reward
        self.foe = foe
    def __str__(self):
        #returns a string with the type, severity, reward, and foe of the mission
        return "Type: " + self.type + "\nSeverity: " + self.severity + "\nReward: " + self.reward + "\nFoe: " + self.foe
    

class ChaosSpaceMarine:
    #defines a class chaos space marine with hp,equipment,name,legion,and xp
    def __init__(self, hp, equipment, name, legion, xp):
        self.hp = hp
        self.equipment = equipment
        self.name = name
        self.legion = legion
        self.xp = xp
        self.role = "Newborn"
        self.abilities = []
    def __str__(self):
        #returns a string with the name, legion, hp, xp, and equipment of the chaos space marine
        return "Name: " + self.name + "\nLegion: " + self.legion + "\nHP: " + str(self.hp) + "\nXP: " + str(self.xp) + "\nEquipment: " + str(self.equipment)
    def change_hp(self, hp):
        #changes the hp of the chaos space marine
        self.hp = hp
    def change_equipment(self, equipment):
        #changes the equipment of the chaos space marine
        self.equipment = equipment
    def change_name(self, name):
        #changes the name of the chaos space marine
        self.name = name
    def change_xp(self, xp):
        #changes the xp of the chaos space marine
        self.xp = xp
    def first_rank_up(self):
        #selects a random class for the first level up after newborn: Havoc, Raptor, Legionnaire, or Sorcerer
        rank = random.randint(1,4)
        if rank == 1:
            self.role = "Havoc"
            self.abilities.append("Heavy Weapons Specialist")
        elif rank == 2:
            self.role = "Raptor"
            self.abilities.append("Fast Attack Specialist")
        elif rank == 3:
            self.role = "Legionnaire"
            self.abilities.append("Melee Specialist")
        else:
            self.role = "Sorcerer"
            self.abilities.append("Psychic Powers")
    def rank_up(self):
        #adds an additional title and ability to the chaos space marine for each rank up after the first based on their role
        #Havoc goes to havoc champion to exalted havoc to daemonsmith
        #Raptor goes to raptor champion, exalted raptor, to warp talon
        #Legionnaire goes to legionnaire champion to exalted legionnaire to chaos lord
        #Sorcerer goes to aspiring sorcerer to exalted sorcerer to archmage
        if self.role == "Havoc":
            if self.xp >= 100:
                self.role = "Exalted Havoc"
                self.abilities.append("Tank Hunter")
            if self.xp >= 200:
                self.role = "Daemonsmith"
                self.abilities.append("Daemon Weapons")
        elif self.role == "Raptor":
            if self.xp >= 100:
                self.role = "Exalted Raptor"
                self.abilities.append("Rending Claws")
            if self.xp >= 200:
                self.role = "Warp Talon"
                self.abilities.append("Warpflame Strike")
        elif self.role == "Legionnaire":
            if self.xp >= 100:
                self.role = "Exalted Legionnaire"
                self.abilities.append("Chaos Champion")
            if self.xp >= 200:
                self.role = "Chaos Lord"
                self.abilities.append("Moments of glory")
        else:
            if self.xp >= 100:
                self.role = "Exalted Sorcerer"
                self.abilities.append("Sorcerous Might")
            if self.xp >= 200:
                self.role = "Archmage"
                self.abilities.append("Chaos Familiar")
    def name(self):
        #returns the name of the chaos space marine
        return self.name

def warband_generate():
    #returns a roster of the warband with 10 chaos space marines each randomly generated using marine_generate
    warband = []
    for i in range(10):
        warband.append(marine_generate())
    return warband

def marine_generate():
    #Returns a Chaos Space Marine, with a random name and legion. 
    #newborn with 0 xp and 10 hp.
    #equipment is a list with a bolter, chainsword, and combat knife
    #legion is one of the 9 traitor legions
    #names are randomly generated from an imported list called names
    legions = ["Alpha Legion", "Black Legion", "Death Guard", "Emperor's Children", "Iron Warriors", "Night Lords", "Thousand Sons", "Word Bearers", "World Eaters"]
    name = random.choice(lists.name_list)
    legion = random.choice(legions)
    equipment = ["Bolter", "Chainsword", "Combat Knife"]
    return ChaosSpaceMarine(10, equipment, name, legion, 0)


def generate_mission():
    #generates a random mission with a random type, severity, reward, and foe
    types = ["Assassination", "Capture", "Destroy"]
    severities = ["Easy", "Medium", "Hard"]
    rewards = ["Weapon", "Armor", "Materials"]
    foes = ["Imperial Guard", "Space Marines", "Eldar", "Orks", "Tyranids", "Chaos Space Marines"]
    type = random.choice(types)
    severity = random.choice(severities)
    reward = random.choice(rewards)
    foe = random.choice(foes)
    return mission(type, severity, reward, foe)


def attack(marine):
    pass

def play_mission(marines, game_state, mission_choice):
    #missions are played in turns, the player and the enemy taking turns to attack each other. 
    #each marine gets to attack once per turn, and the enemy attacks four times total per turn
    #draw a tk inter window with the chosen marines on the left and the enemy on the right
    
    #create a window
    window = tk.Tk()
    window.title("Mission")
    window.geometry("800x600")
    #create a canvas
    canvas = tk.Canvas(window, width = 800, height = 600)
    canvas.pack()
    #draw the marines on the left as buttons
    for i in range(4):
        #create a button for each marine
        marine = tk.Button(window, text = marines[i].name, command=attack(marines[i]))
        marine.place(x = 100, y = 100 + 100 * i)
    #do only this for now



    #end thingy
    window.mainloop()




def main():
    turn = 0
    #generates a warband of 10 chaos space marines and prints their stats
    warband = warband_generate()
    missions = []
    for i in range(4):
        missions.append(generate_mission())
    game_state1 = game_state(turn, warband, missions)
    #start a loop based on the turn counter. Each day, players have the option to take a mission, pass a day or view the roster
    while turn < 10:
        print("Day " + str(game_state1.turn + 1))
        print("1. Take a mission")
        print("2. Pass a day")
        print("3. View Roster")
        choice = input("What would you like to do? ")
        if choice == "1":
            #Display the missions and allow the player to select one
            print("Here are the missions:")
            for i in range(4):
                print(str(i + 1) + ". " + str(missions[i]))
            mission_choice = input("Which mission would you like to take? ")
            mission_choice = int(mission_choice)

            #the player then selects four marines to take on the mission
            marines = []
            for i in range(4):
                print("Select a marine for mission slot " + str(i + 1))
                for marine in warband:
                    if marine not in marines:
                        print(marine)
                marine_choice = input("Which marine would you like to take? ")
                marine_choice = int(marine_choice)
                marines.append(warband[marine_choice - 1])
                marines.append(marine)
            #the player then plays the mission
            play_mission(marines,game_state1,mission_choice)
            game_state1.change_turn(turn + 1)
        elif choice == "2":
            print("You pass a day")
            game_state1.change_turn(turn + 1)
        else:
            print("You view the roster")
            for marine in warband:
                print(marine)
        print("\n")



main()