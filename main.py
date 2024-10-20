import tkinter 

def set_tiles(row ,column):
    global curr_player

    if game_over:
        return

    if board[row][column]["text"]!="":
        return

    board[row][column]["text"]=curr_player

    if curr_player==player_x:
        curr_player=player_o
    else:
        curr_player=player_x

    check_winner()

def check_winner():
    global game_over
    
    # for horizontal
    for row in range(3):
        if (board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"] and board[row][0]["text"]!=""):
            label.config(text=f'{board[row][0]["text"]} wins.',foreground="yellow")

            for column in range(3):
                board[row][column].config(background="red",foreground="yellow")

            game_over=True
            return

    # for vertical
    for column in range(3):
        if (board[0][column]["text"]==board[1][column]["text"]==board[2][column]["text"] and board[0][column]["text"]!=""):
            label.config(text=f'{board[0][column]["text"]} wins.',foreground="yellow")

            for row in range(3):
                board[row][column].config(background="red",foreground="yellow")
            game_over=True
            return

    #for diagonal
    if (board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"] and board[0][0]["text"]!=""):
        label.config(text=f'{board[0][0]["text"]} wins.',foreground="yellow")

        board[0][0].config(background="red",foreground="yellow")
        board[1][1].config(background="red",foreground="yellow")
        board[2][2].config(background="red",foreground="yellow")
        game_over=True


    # FOR ANTI-DIAGONAL 
    if (board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"] and board[0][2]["text"]!=""):
        label.config(text=f'{board[0][2]["text"]} wins.',foreground="yellow")
        
        board[0][2].config(background="red",foreground="yellow")
        board[1][1].config(background="red",foreground="yellow")
        board[2][0].config(background="red",foreground="yellow")
        game_over=True


def new_game():
    global game_over,curr_player
    print("new game")

    game_over=False
    curr_player=player_x

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",background=another_grey,foreground="white")

    label.config(text=f"{curr_player}'s turn ")
            


#board info

board=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

player_x="X"
player_o="O"
curr_player=player_x
game_over=False

# colors
light_green="#38b240"
green="#006400"
another_grey="#565053"

# window 
root=tkinter.Tk()
root.resizable(False,False)

frame=tkinter.Frame(root)
label=tkinter.Label(frame,text=f"{curr_player}'s turn ",background="grey",foreground="white",font=("Times",15),)
label.grid(row=0,column=0,columnspan=3,sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column]=tkinter.Button(
        frame,
        text="",
        background=another_grey,
        foreground="white",
        font=("Times",20),
        width=10,
        command=lambda row=row, column=column:set_tiles(row ,column)
        )

        board[row][column].grid(row=row+1,column=column)

restart_label=tkinter.Button(
    frame,
    text="Restart",
    font=("Times",15)
    ,background="grey",
    foreground="white",
    command=lambda :new_game()
    )
restart_label.grid(row=4,column=0,columnspan=3,sticky="we")


frame.pack()
root.mainloop()

