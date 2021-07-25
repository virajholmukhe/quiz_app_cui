from quiz import Quiz
from quizmanagement import Qmng
Qm = Qmng()
from play import Play
Pl = Play()

choice = 0

while(choice != 3):
    print('''\t\t\t -------------------
        \t\t |  1. Admin Menu  |
        \t\t -------------------
        \t\t |  2. Play Quiz   |
        \t\t -------------------
        \t\t |  3. Exit        |
        \t\t -------------------''')
    choice = int(input("Enter your choice = "))

    if (choice == 1):
        userid = input("Username : ")
        password = input("Password : ")
        if (userid == "viraj" and password == "123"):
            print("Log in Successfull")
            choice1=0
            while(choice1 !=8):
                print('''\t\t\t\t -------------------------
                    \t\t  1. Add a question
                    \t\t  2. Show all questions
                    \t\t  3. Search a question
                    \t\t  4. Edit a question
                    \t\t  5. Delete a question
                    \t\t  6. Delete File
                    \t\t  7. Instructions
                    \t\t  8. Exit to main menu
                    \t\t -------------------------''')
                choice1 = int(input("Enter your choice = "))

                if(choice1 == 1):
                    try:
                        qid = int(input("Enter a Unique ID for Question = "))
                    except ValueError :
                        print("Please Enter a valid ID for question, read instructions for more information.")
                        break
                    qst = input("Enter a Question = ")
                    opta = input("Enter Option A = ")
                    optb = input("Enter Option B = ")
                    optc = input("Enter Option C = ")
                    optd = input("Enter Option D = ")
                    qans = input("Enter Answer of the Question = ")
                    q1 = Quiz(qid,qst,opta,optb,optc,optd,qans)
                    Qm.addQuestion(q1)
                elif(choice1 == 2):
                    Qm.showQuestion()
                elif(choice1 == 3):
                    qid = int(input("Enter a Unique ID for Question = "))
                    Qm.searchQuestion(qid)    
                elif(choice1 == 4):
                    qid = int(input("Enter a Unique ID for Question = "))
                    Qm.editQuestion(qid)
                elif(choice1 == 5):
                    qid = int(input("Enter a Unique ID for Question = "))
                    Qm.deleteQuestion(qid)
                elif(choice1 == 6):
                    Qm.deleteFile()
                elif(choice1 == 7):
                    Qm.instructions()
        else:
            print("Login Failed")
    elif(choice == 2):
        Pl.readQuestions()