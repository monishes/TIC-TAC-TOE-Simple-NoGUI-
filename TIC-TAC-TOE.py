#!/usr/bin/env python
# coding: utf-8

# In[19]:


from IPython.display import clear_output
clear_output()


# In[20]:


print("TIC-TAC-TOE")
def display_game(board):
    print("POSITION REFERENCE TABLE :")
    print("-------------")
    print("| {} | {} | {} |".format(1,2,3))
    print("----+---+----")
    print("| {} | {} | {} |".format(4,5,6))
    print("----+---+---")
    print("| {} | {} | {} |".format(7,8,9))
    print("-------------")
    print("GAME TABLE :")
    print("-------------")
    print("| {} | {} | {} |".format(board[0],board[1],board[2]))
    print("----+---+----")
    print("| {} | {} | {} |".format(board[3],board[4],board[5]))
    print("----+---+---")
    print("| {} | {} | {} |".format(board[6],board[7],board[8]))
    print("-------------")


# In[21]:


def user_define():
    P1=''
    P2=''
    P1=input("Player 1 : Enter your Choice of Input : (X or O)")
    print(P1)
    while P1!='X' or P1!='O':
        if P1=='X':
            P2='O'
            break
        elif P1=='O':
            P2='X'
            break
        else:
            P1=input("Invalid Choice: Enter (X or O)")
    return(P1,P2)


# In[22]:


board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']


# In[23]:


display_game(board)


# In[24]:


def game_choice():
    choice=''
    choice=input("Player 1: Do you want to start :")
    while choice!='Y' or choice!='N':
        if choice=='Y':
            return(1)
        elif choice=='N':
            return(2)
        else:
            choice=input("Invalid Choice : Enter (Y or N) : ")


# In[25]:


game_choice()


# In[26]:


def check_game(board):
    if board[0]==board[1] and board[1]==board[2] and board[2]!=' ':
        return(True)
    elif board[3]==board[4] and board[4]==board[5] and board[3]!=' ':
        return(True)
    elif board[6]==board[7] and board[7]==board[8] and board[6]!=' ':
        return(True)
    elif board[0]==board[4] and board[4]==board[8] and board[4]!=' ':
        return(True)
    elif board[2]==board[4] and board[4]==board[6] and board[4]!=' ':
        return(True)
    elif board[0]==board[4] and board[4]==board[7] and board[4]!=' ':
        return(True)
    elif board[1]==board[4] and board[4]==board[7] and board[4]!=' ':
        return(True)
    elif board[2]==board[5] and board[5]==board[8] and board[2]!=' ':
        return(True)
    else:
        return(False)


# In[27]:


def game_entry(board,player):
    index=int(input("Enter the Position in to Mark (1 - 9) : "))
    val=False
    while True:
        if index>=1 and index<=9:
            if board[index-1]!=' ':
                index=int(input("Index Already Taken ! Choose Empty index from the above Game :"))
            else:
                board[index-1]=player
                val=check_game(board)
                return(val)
        else:
            index=int(input("Invalid Choice : Choose from (1 - 9) :"))


# In[28]:


def game():
    print("Welcome to the TIC-TAC-TOE Game : ")
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    P1=''
    P2=''
    P1,P2=user_define()
    ch=game_choice()
    check=False
    count=0
    if ch==1:
        while count!=9:
            print("Player 1:")
            check=game_entry(board,P1)
            count+=1
            clear_output()
            display_game(board)
            if(check==True):
                print("Player 1 has won !")
                break
            if(count!=9):
                print("Player 2:")
                check=game_entry(board,P2)
                count+=1
                clear_output()
                display_game(board)
                if(check==True):
                    print("Player 2 has won !")
                    break
        else: 
            if count==9:
                clear_output()
                display_game(board)
                print("Draw Game")
    else:
        while count!=9:
            print("Player 2:")
            check=game_entry(board,P2)
            count+=1
            clear_output()
            display_game(board)
            if(check==True):
                print("Player 2 has won !")
                break
            if(count!=9):
                print("Player 1:")
                check=game_entry(board,P1)
                count+=1
                clear_output()
                display_game(board)
                if(check==True):
                    print("Player 1 has won !")
                    break
        else:
            if count==9:
                clear_output()
                display_game(board)
                print("Draw Game")


# In[29]:


game()


# In[ ]:




