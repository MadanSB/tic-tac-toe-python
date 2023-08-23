def print_board(board):
    print("printing the board out ")
    print(board[0][1])

# 1. manually print every element of the board
#2. automate every element of the board
#3. stylise the board -make it look good

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
          print(" " , board[i][j] , " |", end="")
        print("\n-------------")
    
def main():

   # name = input("what is your name: ")
   # print("hello", name)

  #  playing = input("Would you like to play a game of tic tac toe(yes/no): ")
    playing = "yes"
    if playing == "no":
        print("Ok have a nice day:) ")
        quit()
    else:
        board_vert = [0,3,6]
        board_vert2 = [1,4,7]
        board_vert3 = [2,5,8]
        new_board = [board_vert,board_vert2,board_vert3]
        print(new_board)
        print(new_board[1][1])
        print_board(new_board)
        new_board2 = [['','',''],['','',''],['','','']]
        print(new_board2)
        tile_board = int(input("where would u like to place a tile on the board?: "))
        new_board2[tile_board][0] = 'x'
        print(new_board2)
        print_board(new_board2)
main()

player1 = {'key':'X'}
player2 ={'key':'O'}
print(player1.key)