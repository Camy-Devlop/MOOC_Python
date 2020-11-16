import turtle

class Bonbon():
    def __init__(self):
        self.nombre=12
class Chocolat():
    def __init__(self):
        self.nombre=13

def d_l():
    deplacement("gauche",position)
def d_r():
    deplacement("droite",position)
def d_u():
    deplacement("haut",position)
def d_d():
    deplacement("bas",position)

def deplacement(mouvement:str,position):
    if mouvement=="gauche":
        if position>=1:
            print(position, isinstance(l[2 ], Chocolat))
            if isinstance(l[position-1],Chocolat):
                print("c'est du chocolat")
            position-=1

    elif mouvement=="droite":

        if position<len(l):
            print(position, isinstance(l[2], Bonbon))
            if isinstance(l[2],Bonbon):
                print("c\'et du bonbon")
            position+=1

    elif mouvement=="haut":
        pass
    elif mouvement=="bas":
        pass


position=0
l=[Chocolat(), Chocolat() ,Bonbon(), Chocolat() ,Chocolat(), Chocolat(), Bonbon()]

screen =turtle.Screen()
screen.setup(300, 300)

screen.onkeypress(d_l, "Left")
screen.onkeypress(d_r, "Right")
screen.onkeypress(d_u, "Up")
screen.onkeypress(d_d, "Down")

screen.listen()
screen.mainloop()




#import sys
#sys.path.append("..")
#----------------------------------------------------
