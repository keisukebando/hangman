
    
def hangman(word):
    wrong = 0
    stages=["",
            "_________        ",
            "|                ",
            "|        |       ",
            "|        0       ",
            "|       /|\      ",
            "|       / \      ",
            "|                ",
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages)-1:
        print("\n") #空白
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            clind = rletters.index(char)
            board[clind] = char
            rletters[clind] = '$' #複数文字のために更新
        else: wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You are win!")
            win = True
            break
#   if wrong == len(stages)-1:
#         print("\n".join(stages[0:wrong+1]))
#        print("You lose!")

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose!")

#hangman("cat")





import random


words = ["Dog", "Keisuke", "Bando"]
n = random.randint(0, 2)
hangman(words[n])

