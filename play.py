import os
from os import path
from quiz import Quiz
from quizmanagement import Qmng

class Play:
    
    def __init__(self):
        pass
    def readQuestions(self):
        if(path.exists("quizdata.txt")):
            with open("quizdata.txt","r") as fp:
                i = 0
                marks = 0
                for line in fp:
                    i+=1
                    list = line.split(",")
                    qst = list[1]
                    print("-----------------------------------------------------------------------------------------------------")
                    print("Question No ",i,":- ",qst)
                    opta = list[2]
                    print("-----------------------------------------------------------------------------------------------------")
                    print("Option A : ",opta)
                    optb = list[3]
                    print("Option B : ",optb)
                    optc = list[4]
                    print("Option C : ",optc)
                    optd = list[5]
                    print("Option D : ",optd)
                    print("-------------------------------------------------------------------")
                    qans = list[6]
                    qans = qans.rstrip("\n")
                    answer = input("Choose Your Answer = ")
                    answer = answer.lower()
                    if (answer == qans):
                        marks += 1
                print("===================================================================")
                print("Total Questions = ",i)
                print("Corect Answers = ",marks)
                print("1 Mark each question ")
                print("Total Marks = ",marks)
                print("===================================================================")
                
        else:
            print("Record not found")
