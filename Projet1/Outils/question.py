from turtle import textinput as demander
import turtle
class Question():

    def __init__(self,sujet:tuple):
        print("class qestion",sujet)
        self.question=sujet[0]
        self.reponce=sujet[1]

    def demande(self):
        if demander("Question",self.question)==self.reponce:
            print(True)
            turtle.listen()
            return True
        else:
            print(False)
            turtle.listen()
            return False

    def __str__(self):
        return "Question ?"
