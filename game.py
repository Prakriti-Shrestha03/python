import random
import datetime
import os
import time

INVENTORY_FILE="inventory.txt"
LEADERBOARD_FILE="leaderboard.txt"

def save_to_file(filename, data, mode="a"):
    """Save data to file"""
    with open(filename,mode) as file:
        file.write(data + "\n")

def explore_location():
    """Explore a random location and find treasures"""
    locations=["Mysterious Cave","Haunted Forest","Deserted Beach","Ancient Ruins"]
    treasures=["Golden Crown","Silver Sword","Diamond Necklace","Ancient Artifact"]
    
    location=random.choice(locations)
    treasure=random.choice(treasures)
    
    print(f"Exploring {location}...")
    time.sleep(2)
    print(f"You found a {treasure}")
    
    save_to_file(INVENTORY_FILE,treasure)
    return treasure

def load_from_file(filename):
    """Load data from a file."""
    if not os.path.exists(filename):
        return []
    with open(filename,"r")as file:
        return [line.strip() for line in file]
    
def display_inventory():
    """Display the leaderboard."""
    leaderboard=load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nleaderboard:")
        for entry in leaderboard:
            print(entry)
    else:
        print("\n No entries in the leaderboard yet.")

def update_leaderboard(player_name,score):
    """Update the leaderboard"""
    save_to_file(LEADERBOARD_FILE,f"{player_name}:{score}")

def treasure_hunt():
    print("Welcome to Treasure Hunt")
    player_name=input("Enter your name:").strip()
    
    if os.path.exists(INVENTORY_FILE):
        print("\nResuming your adventure...")
    else:
        print("\nStarting a new adventure...")
        open(INVENTORY_FILE,"w").close()
    
    score=0
    
    while True:
        print("\n What would you like to do?")
        print("1. Explore a new location")
        print("2. View inventory")
        print("3. Quit and save Progress")
        choice=input("Enter your choice (1/2/3):").strip()
        
        if choice=="1":
            treasure=explore_location()
            score+=1
            print(f"You added {treasure} to your inventory")
        elif choice=="2":
            display_inventory()
        elif choice=="3":
            print(f"\nThanks for playing,{player_name}!")
            print(f"You collected {score} treasures.")
            update_leaderboard(player_name,score)
            break
        else:
            print("Invalid choice.Please try again.")
            
def display_leaderboard():
    """Display the Leaderboard"""
    leaderboard=load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nLeaderboard")
        for entry in leaderboard:
            print(entry)
    else:
        print("\nNo entries in the leaderboard yet.")

def view_leaderboard():
    print("\n==Leaderboard==")
    display_leaderboard()

def main():
    while True:
        print("\n==Treasure Hunt Menu==")
        print("1. Start/Resume game")
        print("2.View Leaderboard")
        print("3.Exit")
        choice=input("enter your choice (1/2/3)").strip()
        
        if choice=="1":
            treasure_hunt()
        elif choice=="2":
            view_leaderboard()
        elif choice=="3":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again")

if __name__=="__main__":
    main()

