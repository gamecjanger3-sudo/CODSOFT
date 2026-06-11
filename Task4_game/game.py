import random

item_list = ["Rock","Paper","Scissor"]

your_choice = input("Enter your move = Rock, Paper, Scissor : ")
comp_choice = random.choice(item_list)

print(f"Your choice = {your_choice}, Computer Choice = {comp_choice}")

if your_choice == comp_choice:
    print("Both chooses same : = Match Tie")

elif your_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers the Rock = Computer Win")
    else:
        print("Rock smashes the Scissor = You Win")

elif your_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper covers the Rock = You Win")    
    else:
        print("Scissor cut the Paper = Computer Win") 
 
elif your_choice == "Scissor":
    if comp_choice == "Paper":
            print("Scissor cut the Paper = You Win")    
    else:
            print("Rock smashes the Scissor = Computer Win")                        