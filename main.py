#first we will need a table to display and play tic tac toe on..
################################################
def table(i):
    print( i[0],"|",i[1] ,"|",i[2])
    print("--|---|--")
    print( i[3],"|",i[4] ,"|",i[5])
    print("--|---|--")
    print( i[6],"|",i[7] ,"|",i[8])
################################################
def win_checker(x,y,winr,who):
    w=[ [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6] ]
    tx = 0
    ty = 0
    for i in range(8):
        tx = 0
        ty = 0
        for j in range(3):
            if w[i][j] in x:
                tx = tx + 1
            if w[i][j] in y:
                ty = ty + 1
            if tx >= 3:
                who = "player 1"
                winr = True
                return winr, who
            if ty >= 3:
                who = "player 2"
                winr =True
                return winr, who
    return winr == False , who == "no_one"
################################################
print("welcome to tic tac toe !!!")
print("::how to play::")
print("--------------------")
print("player one gets x!!!")
print("plyer 2 gets 0!!!")
print('''only enter numbers
to place your mark !!!''')
print("--------------------")
print("1.start game!")
print("2.quit game!")
choice = int(input())
p1 = [0,0,0,0,0]
ptr1 = 0
p2 = [0,0,0,0]
ptr2 = 0
tc = 0
who = "0"
winr = False
i = ["0","1","2","3","4","5","6","7","8"]
if choice == 1:
    while tc < 9:
        table(i)
        if tc == 0 or tc % 2 == 0 :
            print("player 1 chance:")
            p1[ptr1] = int(input(""))
            i[p1[ptr1]] = "x"
            ptr1 = ptr1 + 1
            winr , who = win_checker(p1, p2, winr, who)
        else:
            print("player 2 chance:")
            p2[ptr2] = int(input(""))
            i[p2[ptr2]] = "O"
            ptr2 = ptr2 + 1
            winr , who = win_checker(p1, p2, winr, who)
        tc = tc + 1
        print(np1,np2)
        if winr == True:
            break
    table(i)
    print(p1)
    print(p2)
    print("the winner is:", who)
else:
    exit()    
