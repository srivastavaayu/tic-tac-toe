import time
from tic_tac_toe_functions import *
print '\n\n\t\t\t\t\t\t       TIC-TAC-TOE'
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']
print_board(a,b,c)
ch=0
player_name=raw_input("\tEnter name of player: ")
choice=raw_input("\n\tWhom do you want to go first(C for computer, P for human player):")
print '\n'
if choice=='P' or choice=='p':
    for i in range(9):
        if i%2==0:
            while put_x(a,b,c):
                continue
            print_board(a,b,c)
            if check_column(a,b,c,player_name) or check_row(a,b,c,player_name) or check_diagonal(a,b,c,player_name):
                ch=1
                break
        if i%2!==0:
            while put_o(a,b,c):
                continue
            print_board(a,b,c)
            if check_column(a,b,c,player_name) or check_row(a,b,c,player_name) or check_diagonal(a,b,c,player_name):
                ch=1
                break
elif choice=='C' or choice=='c':
    for i in range(9):
        if i%2!==0:
            while put_x(a,b,c):
                continue
            print_board(a,b,c)
            if check_column(a,b,c,player_name) or check_row(a,b,c,player_name) or check_diagonal(a,b,c,player_name):
                ch=1
                break
        if i%2==0:
            while put_o(a,b,c):
                continue
            print_board(a,b,c)
            if check_column(a,b,c,player_name) or check_row(a,b,c,player_name) or check_diagonal(a,b,c,player_name):
                ch=1
                break
if ch==0:
    print "\t\t\t\t\t\tThe match is drawn! No winner! :-( "
print "\n\t\t\t\t\t\t  Thanks for playing!"
time.sleep(5)
