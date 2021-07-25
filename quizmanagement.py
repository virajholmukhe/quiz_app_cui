import os
from os import path
from quiz import Quiz
class Qmng:
    def __init__(self):
        pass
    def addQuestion(self,q):
        #it will create a text file and will append data in the file.
        with open("quizdata.txt","a") as fp:
            fp.write(str(q))
            fp.write("\n")
    def showQuestion(self):
        #it will check if file does exixts in directory or not.
        if(path.exists("quizdata.txt")):
            #to read all data from file till end.
            with open("quizdata.txt","r") as fp:
                print(fp.read())
        #if file not exists.
        else:
            print("File does not exist")
    def searchQuestion(self,qid):
        if(path.exists("quizdata.txt")):            
            with open("quizdata.txt","r") as fp:
                ##to read all data from file line by line.
                for line in fp:
                    #search qid line by line. 
                    if(str(qid) in line):
                        print("Record Found")
                        print(line)
                        break
                else:
                    print("Record not found")
        else:
            print("File does not exist")
    def editQuestion(self,qid):
        if(path.exists("quizdata.txt")):
            list = []
            found1 = False
            with open("quizdata.txt","r") as fp:
                for line in fp:
                    #read the file line by line and if qid is not in line, append to the list.
                    if(str(qid) not in line):
                        list.append(line)
                    else:
                        #split method splits string into list and it will stored in edit.
                        edit = line.split(",")
                        #it will ask if you want to change question.
                        ans = input("Do you wish to change Question ? (Y/N) = ")
                        if (ans.lower() == "y"):
                            qst = input("Enter Question = ")
                            #changed question will replace 2nd index of list i.e., qst.
                            edit[1] = qst
                        #it will ask if you want to change options.
                        ans = input("Do you wish to change options ? (Y/N) = ")
                        if (ans.lower() == "y"):
                            opta = input("Enter option A = ")
                            #changed option will replace 3rd index of list i.e., opta
                            edit[2] = opta
                            optb = input("Enter option B = ")
                            #changed option will replace 4th index of list i.e., optb
                            edit[3] = optb
                            optc = input("Enter option C = ")
                            #changed option will replace 5th index of list i.e., optc
                            edit[4] = optc
                            optd = input("Enter option D = ")
                            #changed option will replace 6th index of list i.e., optd
                            edit[5] = optd
                        #it will ask if you want to change answer.
                        ans = input("Do you wish to change Answer ? (Y/N) = ")
                        if (ans.lower() == "y"):
                            qst = input("Enter Question = ")
                            #changed answer will replace 6th index of list i.e., qns.
                            edit[6] = qst
                        #to join splitted list in , seperated values
                        edit = ",".join(edit)
                        #pointer will go to new line
                        edit+="\n"
                        #edit list will append to original list.
                        list.append(edit)
                        found1 = True
            #if found == true, i will write edited question in file.
            if(found1 == True):
                with open("quizdata.txt","w") as fp:
                    for line in list:
                        fp.write(line)
        else:
            print("File does not exist")
    def deleteQuestion(self,qid):
        if(path.exists("quizdata.txt")):
            list2 = []
            found2 = False
            with open("quizdata.txt","r") as fp:
                for line in fp:
                    #if qid is not present in line, line will append to list2.
                    if(str(qid) not in line):
                        list2.append(line)
                    else:
                        found2 = True
            #list will contain all data except qid line, so it will get overwrite file.
            if(found2 == True):
                with open("quizdata.txt","w") as fp:
                    for line in list2:
                        fp.write(line)
        else:
            print("File does not exist")
    def deleteFile(self):
        if(path.exists("quizdata.txt")):            
            os.remove("quizdata.txt")
            print("File Deleted successfully")
        else:
            print("File does not exist")
    def instructions(self):
        print('''\t\t\t\t -------------------------
            \t\t ♦ Plsease use only numbers as question ID, 
            \t\t   else it will get automatically logged out.
            \t\t ♦ If you choose to edit question, 
            \t\t   change atleast one value.
            \t\t ♦ If you choose to delete File. 
            \t\t   it will remove all data from file.
            \t\t ♦ ''')
