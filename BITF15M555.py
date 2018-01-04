#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------  WELCOME TO TICTACTOE GAME BY BITF15M555 ------------------
#------------------  SUBMITTED TO PROF. TAHIR HUSSAIN FAZAL AWAN --------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def Play2turn():
    global n
    global z
    if z == 0:
        Play1check()
    if n == 9:
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        global h
        global i
 
        Play2 =  input ("Player/O Its Your Turn.. :):) Give Me an integer(1-9)")
        if Play2 == 1:
            Play2test(a)
            a = "O"
        elif Play2 == 2:
            Play2test(b)
            b = "O"
        elif Play2 == 3:
            Play2test(c)
            c = "O"
        elif Play2 == 4:
            Play2test(d)
            d = "O"
        elif Play2 == 5:
            Play2test(e)
            e = "O"
        elif Play2 == 6:
            Play2test(f)
            f = "O"
        elif Play2 == 7:
            Play2test(g)
            g = "O"
        elif Play2 == 8:
            Play2test(h)
            h = "O"
        elif Play2 == 9:
            Play2test(i)
            i = "O"
        else:
            print "Please Enter a valid Interger From 1-9"
            Play2turn()
        print a,"\t|\t",b,"\t|\t",c
        print "----------------------------------------------------"
        print d,"\t|\t",e,"\t|\t",f
        print "----------------------------------------------------"
        print g,"\t|\t",h,"\t|\t",i
        z = 0
        Play1turn()
def Play1turn():
    global n
    global z
    if z == 0:
        Play2check()
    if n == 9:
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        global h
        global i
        Play1 = input ("Player/X Its Your Turn.. :):) Give Me an integer(1-9)")
        if Play1 == 1:
            Play1test(a)
            a = "X"
        elif Play1 == 2:
            Play1test(b)
            b = "X"
        elif Play1 == 3:
            Play1test(c)
            c = "X"
        elif Play1 == 4:
            Play1test(d)
            d = "X"
        elif Play1 == 5:
            Play1test(e)
            e = "X"
        elif Play1 == 6:
            Play1test(f)
            f = "X"
        elif Play1 == 7:
            Play1test(g)
            g = "X"
        elif Play1 == 8:
            Play1test(h)
            h = "X"
        elif Play1 == 9:
            Play1test(i)
            i = "X"
        else:
            print "Please Enter a valid Interger From 1-9"
            Play1turn()
        print a,"\t|\t",b,"\t|\t",c
        print "----------------------------------------------------"
        print d,"\t|\t",e,"\t|\t",f
        print "----------------------------------------------------"
        print g,"\t|\t",h,"\t|\t",i
        z = 0
        Play2turn()
def Play1check():                                                                           
    global z
    if   a == "X" and b == "X" and c == "X":
        Play1win()
    elif b == "X" and e == "X" and h == "X":
        Play1win()
    elif d == "X" and e == "X" and f == "X":
        Play1win()
    elif a == "X" and d == "X" and g == "X":
        Play1win()
    elif g == "X" and h == "X" and i == "X":
        Play1win()
    elif c == "X" and f == "X" and i == "X":
        Play1win()
    elif a == "X" and e == "X" and i == "X":
        Play1win()
    elif c == "X" and e == "X" and g == "X":
        Play1win()
    elif a != 1 and b != 2 and c != 3 and d != 4 and e != 5 and f != 6 and g != 7 and h != 8 and i != 9:
        tie()
    else:
        z = 1
        Play2turn()
def Play2check():                                    
    global z
    if   a == "O" and b == "O" and c == "O":
        Play2win()
    elif b == "O" and e == "O" and h == "O":
        Play2win()
    elif d == "O" and e == "O" and f == "O":
        Play2win()
    elif a == "O" and d == "O" and g == "O":
        Play2win()
    elif g == "O" and h == "O" and i == "O":
        Play2win()
    elif c == "O" and f == "O" and i == "O":
        Play2win()
    elif a == "O" and e == "O" and i == "O":
        Play2win()
    elif c == "O" and e == "O" and g == "O":
        Play2win()
    elif a != 1 and b != 2 and c != 3 and d != 4 and e != 5 and f != 6 and g != 7 and h != 8 and i != 9:
        tie()
    else:
        z = 1
        Play1turn()

def Play2win():         
    global pc
    print "MuBBarakann ! Player 2 wins"
    newgame()
        
def Play1win():                                      
    global n
    if n == 9:
        print "MuBBarakann ! Player 1 wins"
        newgame()

def Play2test(num):                                    
    if num == "X" or num == "O":
        print "Can't Enter the Already taken integer"
        Play2turn()

def Play1test(num):                                         
    if num == "X" or num == "O":
        print "Can't Enter the Already taken integer"
        Play1turn()

def newgame():
    global xwins
    global owins
    global tiewins
    global n
    if n == 9:
        t = raw_input("Do you want to play once again ! '1' or '0'")
        if t == "1":
            func()
        elif t == "0":
            n = 0
            end()
        else:
            print "Enter 1 or 0 only"
            newgame()
    

def tie():                              
    print "\n----Game has been tied.. Better Luck next time-----!! :)\n"
    newgame()

def end():                                   
    global n
    n = 0
    print "!!---Allah Hafiz---!!"
    
def func():
    global z
    global t
    global w
    global pc
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global x
    global o
    global t
    global n
    TicTacToe=[1,2,3,4,5,6,7,8,9]
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    x = 0
    o = 0
    z = 1
    t = 0
    if n != 0:
        n = 9
        w = raw_input ("Player 1 or Player 2 ?? Who want the 1st Turn 'x' or 'o'") 
        print TicTacToe[0],"\t|\t",TicTacToe[1],"\t|\t",TicTacToe[2]
        print "----------------------------------------------------"
        print TicTacToe[3],"\t|\t",TicTacToe[4],"\t|\t",TicTacToe[5]
        print "----------------------------------------------------"
        print TicTacToe[6],"\t|\t",TicTacToe[7],"\t|\t",TicTacToe[8]
        if w =='o':
            Play2turn()
        elif w =='x':
            Play1turn()
        else:
            print "Na Na Na Na--- Only Enter 'x' or 'o'"
            func()
n = 9
func()
