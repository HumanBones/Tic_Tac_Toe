import random

# The game board

board = [0,1,2,
         3,4,5,
         6,7,8]

def checkDraw(list):                                  #checks for draw,if no str in list
    if all(isinstance(elem, str) for elem in list):
        return True
    else:
        return False

def show():                                         #board print
    print (board[0], "|",board[1], "|", board[2])
    print ("-----------")
    print (board[3], "|",board[4], "|", board[5])
    print ("-----------")
    print (board[6], "|",board[7], "|", board[8])

def checkLine(char, spot1, spot2, spot3):          #line checker
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True

def checkAll(char):                 #Checks in line wins
    if checkLine (char, 0, 1, 2):
        return True
    if checkLine (char, 3, 4, 5):
        return True
    if checkLine (char, 6, 7, 8):
        return True
    if checkLine (char, 0, 4, 8):
        return True
    if checkLine (char, 6, 4, 2):
        return True
    if checkLine (char, 0, 3, 6):
        return True
    if checkLine (char, 1, 4, 7):
        return True
    if checkLine (char, 2, 5, 8):
        return True



show()

while True:

    if checkAll("o") == True: #checks if x is in line
        print("--O WINS--")
        show()
        #print(draw)
        break
    if checkAll("x") == True: #checks if x is in line
        print("--X WINS--")
        show()
        #print(draw)
        break

    while True:                           #checks if input is valid
        try:
            a = input("Select a spot: ")  #lets u input
            a = int(a)
            if (a <= 8):
                break
            else:
                print("Number is to big!")
                continue
        except ValueError:
            print("Invalid value!")
            continue

    if board[a] != "x" and board[a] != "o":  #checks if u can place it there
        board[a] = "x"
        draw = checkDraw(board)
        #print(draw)
        if checkAll("x") == True: #checks if x is in line
            #win = True
            print("--X WINS--")
            show()
            #print(draw)
            break
        if draw == True:
            print("Draw!")
            show()
            break
        while True:
            random.seed() #Gives a random generator
            opponent = random.randint(0,8)  #randoms a number between 0 and 8

            if board[opponent] != "o" and board[opponent] != "x": #checks if there is place
                board[opponent] = "o"
                break

            else:                           #if it is taken it rolls a new nubmer
                continue
    else:
        print ("This spot is taken")
        continue

    show()
