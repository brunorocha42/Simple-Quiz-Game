name = input("Please enter your name: ")

print(f"{name}, welcome to Bruno Rocha's Python Quiz!")

#play = input(name + ", do you want to play? (yes/no): ")
play = input(f"{name}, do you want to play? (yes/no): ")

if play.lower() != "yes":
    print("Maybe next time, see you later!")
    quit()



while play.lower() == "yes":

    score = 0

    #1
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #2
    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #3
    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #4
    answer = input("What does PSU stand for? ")
    if answer.lower() == "power supply unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #5
    answer = input("What does HDD stand for? ")
    if answer.lower() == "hard disk drive":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print(f"{name}, you got {score} out of 5 questions correct!")
    print(f"Final score: {score/5 * 100:.2f}%")

    play = input("Do you want to play again? (yes/no): ") 

