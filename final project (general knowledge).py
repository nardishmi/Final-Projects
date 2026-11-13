

categories = ["History", "Science", "Music", "Food"]

questions = [["In which country is Persepolis located?","Who built the Pyramids of Giza?","Who was the first emperor of the Mongol Empire?"],["Which planet is known as the Red Planet?","What is the chemical symbol for Gold?","Which organ pumps blood in the human body?"],["Who is known as the King of Pop?","Which musical instrument has 88 keys?","Which band released Bohemian Rhapsody?"],["Kashk-e Bademjan is a traditional dish from which country?","Sushi is a traditional food from which country?","Paella is a traditional dish from which country?"]]

options = [[["Iran", "Greece", "Egypt", "Italy"],["Romans", "Egyptians", "Greeks", "Persians"],["Alexander", "Genghis Khan", "Napoleon", "Julius Caesar"]],[["Venus", "Mars", "Jupiter", "Saturn"],["Ag", "Au", "Fe", "Cu"],["Lungs", "Brain", "Heart", "Kidneys"]],[["Elvis Presley", "Michael Jackson", "Freddie Mercury", "Prince"],["Guitar", "Violin", "Piano", "Drums"],["The Beatles","Queen", "ABBA", "Pink Floyd"]],[["Turkey", "Iran", "Lebanon", "India"],["China", "Japan", "Thailand", "South Korea"],["Italy", "Mexico", "Spain", "France"]]]

answers = [[1, 2, 2],[2, 2, 3],[2, 3, 2],[2, 2, 3]]
scores = [0, 0, 0, 0]
played = [False, False, False, False]

while True:
    menu=input("1.history quiz 2.science quiz 3.music quiz 4.food quiz 5.show results 6.reset scores 7.exit :")
    while True:
        match menu:
            case "1":
                category = 0
            case "2":
                category = 1
            case "3":
                category = 2
            case "4":
                category = 3
            case "5":
                print(" results ")
                for i in range(4):
                    print(categories[i], ":", scores[i])
                print("total Score:", sum(scores), "out of 12")
            case "6":
                scores = [0, 0, 0, 0]
                played = [False, False, False, False]
                print("all scores have been reset!")
            case "7":
                print("thank you for playing!")
                break
            case _:
                print("invalid menu option!")
        if menu == "1" or menu == "2" or menu == "3" or menu == "4":
            if played[category] == False:
                print(categories[category])
                for i in range(3):
                    print("question", i + 1)
                    print(questions[category][i])
                    for j in range(4):
                        print(j + 1, options[category][i][j])
                    answer = input("your answer (1-4): ")
                    if answer.isdigit():
                        answer = int(answer)
                        if answer >= 1 and answer <= 4:
                            if answer == answers[category][i]:
                                print("correct!")
                                scores[category] += 1
                            else:
                                print("wrong!")
                                print("Correct answer:",options[category][i][answers[category][i] - 1])
                        else:
                            print("invalid answer!")
                    else:
                        print("invalid input!")
                played[category] = True
                print("your score:", scores[category], "out of 3")
            else:
                print("you already played this category!")
                
