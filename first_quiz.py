print("Welcome to Bruno Rocha's Python Quiz!")

name = input("Please enter your name: ")

play = input(f"{name}, do you want to play? (yes/no): ")

if play.lower() == "yes":
    print("Let's play!")
else:
    print("Maybe next time!")

score = 0