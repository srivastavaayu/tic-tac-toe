import time
def put_x(a,b,c):
    '''This function is built to input the position of 'X' and check whether the position is available.'''
    x=input("\tEnter the location where you want to mark X: ")
    if x<=3 and (a[x-1]!='X' and a[x-1]!='O'):
        a[x-1]='X'
        return 0
    elif (x>3 and x<=6) and (b[x-4]!='X' and b[x-4]!='O'):
        b[x-4]='X'
        return 0
    elif (x>6 and x<=9) and (c[x-7]!='X' and c[x-7]!='O'):
        c[x-7]='X'
        return 0
    elif x>0 and x<=9:
        print "\tThe position has already been marked! Please choose another position!"
        return 1
    else:
        print "\tInvalid position! Please choose another position!"
        return 1
def put_o(a,b,c):
    '''This function is built to input the position of 'O' and check whether the position is available.'''
    o=block_move(a,b,c)
    print "\tThe computer marked at position: ",o
    if o<=3 and (a[o-1]!='X' and a[o-1]!='O'):
        a[o-1]='O'
        return 0
    elif (o>3 and o<=6) and (b[o-4]!='X' and b[o-4]!='O'):
        b[o-4]='O'
        return 0
    elif (o>6 and o<=9) and (c[o-7]!='X' and c[o-7]!='O'):
        c[o-7]='O'
        return 0
def block_move(a,b,c):
    '''This function is built to block the human player from winning!'''
    time.sleep(1.5)
    if b[1]!='X' and b[1]!='O':
        return 5
    if a[0]==a[1] and (a[2]!='X' and a[2]!='O'):
        return 3
    elif b[0]==b[1] and (b[2]!='X' and b[2]!='O'):
        return 6
    elif c[0]==c[1] and (c[2]!='X' and c[2]!='O'):
        return 9
    elif a[1]==a[2] and (a[0]!='X' and a[0]!='O'):
        return 1
    elif b[1]==b[2] and (b[0]!='X' and b[0]!='O'):
        return 4
    elif c[1]==c[2] and (c[0]!='X' and c[0]!='O'):
        return 7
    elif a[0]==a[2] and (a[1]!='X' and a[1]!='O'):
        return 2
    elif b[0]==b[2] and (b[1]!='X' and b[1]!='O'):
        return 5
    elif c[0]==c[2] and (c[1]!='X' and c[1]!='O'):
        return 8
    elif a[0]==b[0] and (c[0]!='X' and c[0]!='O'):
        return 7
    elif a[1]==b[1] and (c[1]!='X' and c[1]!='O'):
        return 8
    elif a[2]==b[2] and (c[2]!='X' and c[2]!='O'):
        return 9
    elif b[0]==c[0] and (a[0]!='X' and a[0]!='O'):
        return 1
    elif b[1]==c[1] and (a[1]!='X' and a[1]!='O'):
        return 2
    elif b[2]==c[2] and (a[2]!='X' and a[2]!='O'):
        return 3
    elif a[0]==c[0] and (b[0]!='X' and b[0]!='O'):
        return 4
    elif a[1]==c[1] and (b[1]!='X' and b[1]!='O'):
        return 5
    elif a[2]==c[2] and (b[2]!='X' and b[2]!='O'):
        return 6
    elif a[0]==b[1] and (c[2]!='X' and c[2]!='O'):
        return 9
    elif a[2]==b[1] and (c[0]!='X' and c[0]!='O'):
        return 7
    elif c[2]==b[1] and (a[0]!='X' and a[0]!='O'):
        return 1
    elif c[0]==b[1] and (a[2]!='X' and a[2]!='O'):
        return 3
    elif a[0]==c[2] and (b[1]!='X' and b[1]!='O'):
        return 5
    elif a[2]==c[0] and (b[1]!='X' and b[1]!='O'):
        return 5
    else:
        for o in range(1,10):
            if o<=3 and (a[o-1]!='X' and a[o-1]!='O'):
                return o
            elif (o>3 and o<=6) and (b[o-4]!='X' and b[o-4]!='O'):
                return o
            elif (o>6 and o<=9) and (c[o-7]!='X' and c[o-7]!='O'):
                return o
def check_column(a,b,c,player_name):
    '''This function is built to check if a column is completed.'''
    for i in range(3):
        if a[i]==b[i]==c[i]:
            if a[i]=='X':
                print '\t\t\t\t\t\t',player_name,'wins!'
            else:
                print '\t\t\t\t\t\tComputer wins!'
            return 1
            break
def check_row(a,b,c,player_name):
    '''This function is built to check if a row is completed.'''
    if a[0]==a[1]==a[2]:
        if a[0]=='X':
            print '\t\t\t\t\t\t',player_name,'wins!'
        else:
            print '\t\t\t\t\t\tComputer wins!'
        return 1
    elif b[0]==b[1]==b[2]:
        if b[0]=='X':
            print '\t\t\t\t\t\t',player_name,'wins!'
        else:
            print '\t\t\t\t\t\tComputer wins!'
        return 1
    elif c[0]==c[1]==c[2]:
        if c[0]=='X':
            print '\t\t\t\t\t\t',player_name,'wins!'
        else:
            print '\t\t\t\t\t\tComputer wins!'
        return 1
def check_diagonal(a,b,c,player_name):
    '''This function is built to check if a diagonal is completed.'''
    if a[0]==b[1]==c[2]:
        if a[0]=='X':
            print '\t\t\t\t\t\t',player_name,'wins!'
        else:
            print '\t\t\t\t\t\tComputer wins!'
        return 1
    elif a[2]==b[1]==c[0]:
        if a[2]=='X':
            print '\t\t\t\t\t\t',player_name,'wins!'
        else:
            print '\t\t\t\t\tComputer wins!'
        return 1
def print_board(a,b,c):
    '''This function is built to print the tic-tac-toe board.'''
    print '\n\t\t\t\t\t\t\t  |   |'
    print '\t\t\t\t\t\t\t',a[0],'|',a[1],'|',a[2]
    print '\t\t\t\t\t\t    ','-----|---|-----'
    print '\t\t\t\t\t\t\t',b[0],'|',b[1],'|',b[2]
    print '\t\t\t\t\t\t    ','-----|---|-----'
    print '\t\t\t\t\t\t\t',c[0],'|',c[1],'|',c[2]
    print '\t\t\t\t\t\t\t  |   |\n\n'
