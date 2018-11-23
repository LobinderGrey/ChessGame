import os

w, h = 8,8;
winner = False

playerWhite = ['F:A7','F:B7','F:C7','F:D7','F:E7','F:F7','F:G7','F:H7','T:H8','T:A8','H:G8','H:B8','B:F8','B:C8','K:D8','Q:E8']
playerBlack = ['F:A2','F:B2','F:C2','F:D2','F:E2','F:F2','F:G2','F:H2','T:H1','T:A1','H:G1','H:B1','B:F1','B:C1','Q:D1','K:E1']

def Chesfield():
    print("a b c d e f g h ")
    counter = 0
    for counter in range(0, 8):
        index = 0
        chesfieldline = ''
        for index in range(0, 8):
            figure = checkFieldUseW(index, counter)
            if figure == None:
                figure = checkFieldUseB(index, counter)
            if figure == None:
                chesfieldline = chesfieldline + '_ '
            else:
                chesfieldline = chesfieldline + figure + ' '

        print(chesfieldline + str(counter + 1))
        print("")

def convlettonumb(letter):
    if letter == 'A' or letter == 'a':
        return 0
    if letter == 'B' or letter == 'b':
        return 1
    if letter == 'C' or letter == 'c':
        return 2
    if letter == 'D' or letter == 'd':
        return 3
    if letter == 'E' or letter == 'e':
        return 4
    if letter == 'F' or letter == 'f':
        return 5
    if letter == 'G' or letter == 'g':
        return 6
    if letter == 'H' or letter == 'h':
        return 7

def checkFieldUseW(x,y):
    for figure in playerWhite:
        numbtochar = convlettonumb(figure[2])
        if int(numbtochar) == int(x) and int(figure[3]) - 1 == int(y):
            return figure[0]
    return None

def checkFieldUseB(x,y):
    for figure in playerBlack:
        numbtochar = convlettonumb(figure[2])
        if int(numbtochar) == int(x) and int(figure[3]) - 1 == int(y):
            return figure[0]
    return None
        
def checkSelection(selection, activeplayer):
    if len(selection) == 2:
        print(selection[0])
        sy = int(convlettonumb(selection[0]))
        print(selection[1])
        print(sy)
        sx = int(selection[1])-1
        if any(selection in s for s in activeplayer):
            print('player selection')   
        else:
            print("Keine Figur gewaehlt")

def checkTarget(target, enemyplayer, activeplayer):
    if len(target) == 2:
        print(target[0])
        sy = int(convlettonumb(target[0]))
        print(target[1])
        sx = int(target[1])-1
    if any(target in s for s in enemyplayer):
        print('Enemy Player targeted')
    if any(target in s for s in activeplayer):
        print('Own figure Targeted')


def farmer(p,t):
    moveint = abs(int(p[1]) - int(t[1]))
    if moveint > 0 and moveint < 3:


def tower(p,t):
    if p[1] == t[1]:
        print(abc(int(p[1]) - int(t[1])))

    if p[0] == t[0]:
        print(abs(int(convlettonumb(p[0])) - int(convlettonumb(t[0]))))

def horse(p,t):

    print('horse')

def bishop(p,t):

    print('bishop')

def queen(p,t):

    print('queen')

def king(p,t):

    print('king')

def checkFigure(token, Sfigure, target):
    if token == 'F':
        farmer(Sfigure,target)
    if token == 'T':
        tower(Sfigure,target)
    if token == 'H':
        horse(Sfigure,target)
    if token == 'B':
        bishop(Sfigure,target)
    if token == 'Q':
        queen(Sfigure,target)
    if token == 'K':
        king(Sfigure,target)

while winner == False:
    Chesfield() 
    playerf = input('Waehle Figur Koordinate: ') 
    Sfigure = checkSelection(playerf, playerBlack) 
    target = input('Waehle  Zielkoordinate: ') 
    Starget = checkTarget(target, playerWhite, playerBlack) 
    #checkFigure(Sfigure, playerWhite, target) 
    #os.system('cls') 
    Chesfield() 
    #winner = True