name = input("Please enter your name: ")

print(f"{name}, welcome to Bruno Rocha's Python Quiz!")

#play = input(name + ", do you want to play? (yes/no): ")
play = input(f"{name}, do you want to play? (yes/no): ")

if play.lower() != "yes":
    print("Maybe next time, see you later!")
    quit()
else:
    print("Let's play, it will be fun!")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
        