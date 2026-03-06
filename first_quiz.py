import random
from questions import perguntas

name = input("Please enter your name: ")

print(f"{name}, welcome to Bruno Rocha's Python Quiz!")

#play = input(name + ", do you want to play? (yes/no): ")
play = 0

while play not in ["1", "2"]:
    #play = input(name + ", do you want to play? (yes/no): ")
    play = input(f"{name}, do you want to play? \n1 - yes \n2 - no\n")

    if play == "2":
        print("Maybe next time, see you later!")
        quit()
    elif play == "1":
        play = "1"
    else:
        print("Invalid input. Please use 1 for yes and 2 for no.")

while play == "1":

    tipo = input("Please choose a question type: \n1 - Short Answer \n2 - True Or False\n")          
    if tipo == "1":
        tipo = "Short Answer"
    elif tipo == "2":            
        tipo = "True Or False"

    while tipo not in perguntas:
        print("Invalid type.")
        tipo = input("Choose again: \n1 - Short Answer \n2 - True Or False\n")
        if tipo == "1":
            tipo = "Short Answer"
        elif tipo == "2":            
            tipo = "True Or False"

    category = input("Please choose a category: \n1 - Hardware \n2 - General Culture \n3 - Python\n")
    if category == "1":
        category = "Hardware"
    elif category == "2":            
        category = "General Culture"
    elif category == "3":            
        category = "Python"

    while category not in perguntas[tipo]:
        print("Invalid category.")
        category = input("Choose again: \n1 - Hardware \n2 - General Culture \n3 - Python\n")
        if category == "1":
            category = "Hardware"
        elif category == "2":            
            category = "General Culture"
        elif category == "3":            
            category = "Python"

    # criar uma lista apenas com as perguntas (as chaves)
    lista_perguntas = list(perguntas[tipo][category].keys())
    
    # baralhar a ordem dessa lista
    random.shuffle(lista_perguntas)

    score = 0
    questionNumber = 0

    #percorrer a lista ja baralhada
    for question in lista_perguntas:
        # buscar a resposta certa no dicionario usando a pergunta como chave
        answer = perguntas[tipo][category][question]

        questionNumber += 1
        
        user_answer = input(question)

        if isinstance(answer, bool):
            opcoes_true = ["true", "t", "yes", "y"]
            opcoes_false = ["false", "f", "no", "n"]
            
            user_answer = user_answer.lower().strip()

            while user_answer not in opcoes_true and user_answer not in opcoes_false:
                print("invalid input. please use: true/t/yes/y or false/f/no/n")
                user_answer = input(question).lower().strip()

            user_answer = user_answer in opcoes_true
        else:
            user_answer = user_answer.strip().lower()
            answer = answer.strip().lower()

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    print(f"{name}, you got {score} out of {questionNumber} questions correct!")
    print(f"Final score: {score/questionNumber * 100:.2f}%")

    play = 0

    while play not in ["1", "2"]:
        #play = input(name + ", do you want to play? (yes/no): ")
        play = input("Do you want to play again? \n1 - yes \n2 - no\n")

        if play == "2":
            print("Thanks for playing, see you later!")
            quit()
        elif play == "1":
            play = "1"
        else:
            print("Invalid input. Please use 1 for yes and 2 for no.")

