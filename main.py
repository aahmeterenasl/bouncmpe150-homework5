
board_file = input()
opponent_file = input()
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
input_handle = open(board_file,"r")
opp_handle = open(opponent_file,"r")
input_list = input_handle.readlines()
opponent_list = opp_handle.read().split("\n")
input_handle.close()
opp_handle.close()

#take side info
my_side = input_list[0].strip()[0].upper()

#create empty board
current_board = [["--" for i in range(8)] for j in range(8)]

#fill the board
letters ="abcdefgh"
for pieces in input_list[1:]:
    piece_info = pieces.split()
    piece_name = piece_info[0]
    piece_pos = piece_info[1]
    current_board[8-int(piece_pos[1])][letters.index(piece_pos[0])] = piece_name

#define print func for board to test code easily
def board_print(board):
    for i in board:
        for j in i:
            print(j,end=" ")
        print()
#board_print(current_board)

#define a function that returns new board after moving a piece
def move(board,old_piece_pos,new_piece_row,new_piece_column):
    new_board = [["--" for i1 in range(8)] for j1 in range(8)]
    for rows in range(8):
        for columns in range(8):
            new_board[rows][columns] = board[rows][columns]
    piece_row,piece_column = 8 - int(old_piece_pos[1]),letters.index(old_piece_pos[0])
    cur_piece_name = board[piece_row][piece_column]
    new_board[piece_row][piece_column],new_board[new_piece_row][new_piece_column] = "--",cur_piece_name
    return [new_board,new_piece_row,new_piece_column]

#define movements of chess pieces and return all possible boards
def possible_movements(board,cur_piece_pos):
    possible_boards = []

    #take piece name and pos indexes
    piece_row = 8-int(cur_piece_pos[1])
    piece_column = letters.index(cur_piece_pos[0])
    cur_piece_name = board[piece_row][piece_column]

    #if there is a piece take its side
    if cur_piece_name == "--":
        return
    cur_piece_side = cur_piece_name[0]

    #movements for black pawns
    if cur_piece_name == "BP":
        #if pawn is at the other end do nothing
        if piece_row == 7:
            return possible_boards
        #if pawn's front is empty go forward by 1
        if board[piece_row+1][piece_column] == "--":
            possible_boards.append(move(board,cur_piece_pos,piece_row+1,piece_column))
        #if there is an enemy piece at pawn's front left ,eat it
        if piece_column != 7:
            if board[piece_row+1][piece_column+1][0] == "W":
                possible_boards.append(move(board, cur_piece_pos, piece_row + 1, piece_column+1))
        # if there is an enemy piece at pawn's front right ,eat it
        if piece_column != 0:
            if board[piece_row+1][piece_column-1][0] == "W":
                possible_boards.append(move(board, cur_piece_pos, piece_row + 1, piece_column-1))
        #if pawn is it's starting point,go forward by 2
        if piece_row == 1 and board[piece_row+1][piece_column] == "--" and board[piece_row+2][piece_column] == "--":
            possible_boards.append(move(board, cur_piece_pos, piece_row + 2, piece_column))

    #movements for white pawns
    elif cur_piece_name == "WP":
        # if pawn is at the other end do nothing
        if piece_row == 0:
            return possible_boards
        # if pawn's front is empty go forward by 1
        if board[piece_row-1][piece_column] == "--":
            possible_boards.append(move(board,cur_piece_pos,piece_row-1,piece_column))
        # if there is an enemy piece at pawn's front left ,eat it
        if piece_column != 7:
            if board[piece_row-1][piece_column+1][0] == "B":
                possible_boards.append(move(board, cur_piece_pos, piece_row - 1, piece_column+1))
        # if there is an enemy piece at pawn's front right ,eat it
        if piece_column != 0:
            if board[piece_row-1][piece_column-1][0] == "B":
                possible_boards.append(move(board, cur_piece_pos, piece_row - 1, piece_column-1))
        # if pawn is it's starting point,go forward by 2
        if piece_row == 6 and board[piece_row-1][piece_column] == "--" and board[piece_row-2][piece_column] == "--":
            possible_boards.append(move(board, cur_piece_pos, piece_row - 2, piece_column))

    #movements for kings
    elif cur_piece_name == "BK" or cur_piece_name == "WK":
        for K_row in [-1,0,1]:
            for K_col in [-1,0,1]:
                if K_col == 0 and K_row == 0:
                    continue
                new_row = piece_row + K_row
                new_col = piece_column + K_col
                if (new_row>=0 and new_row<8) and (new_col>=0 and new_col<8):
                    if board[new_row][new_col][0] != cur_piece_side:
                        possible_boards.append(move(board,cur_piece_pos,new_row,new_col))

    #movements for queens
    elif cur_piece_name == "BQ" or cur_piece_name == "WQ":
        new_row = piece_row + 1
        new_col = piece_column + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row += 1
                    new_col += 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row - 1
        new_col = piece_column + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row -= 1
                    new_col += 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row + 1
        new_col = piece_column - 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row += 1
                    new_col -= 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row - 1
        new_col = piece_column - 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row -= 1
                    new_col -= 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row
        new_col = piece_column + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_col += 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row - 1
        new_col = piece_column
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row -= 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row + 1
        new_col = piece_column
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row += 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row
        new_col = piece_column - 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_col -= 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break

    #movements for bishops:
    elif cur_piece_name == "BB" or cur_piece_name == "WB":
        new_row = piece_row + 1
        new_col = piece_column + 1
        while (new_row>=0 and new_row<8) and (new_col>=0 and new_col<8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row += 1
                    new_col += 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row - 1
        new_col = piece_column + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row -= 1
                    new_col += 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row + 1
        new_col = piece_column - 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row += 1
                    new_col -= 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row - 1
        new_col = piece_column - 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row -= 1
                    new_col -= 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break

    #movements for rooks
    elif cur_piece_name == "BR" or cur_piece_name == "WR":
        new_row = piece_row
        new_col = piece_column + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_col += 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row - 1
        new_col = piece_column
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row -= 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row + 1
        new_col = piece_column
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_row += 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break
        new_row = piece_row
        new_col = piece_column - 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col][0] != cur_piece_side:
                if board[new_row][new_col] == "--":
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    new_col -= 1
                else:
                    possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
                    break
            else:
                break

    #movements for knights
    elif cur_piece_name == "BN" or cur_piece_name == "WN":
        for N_row in [-2,2]:
            for N_col in [-1,1]:
                new_row = piece_row + N_row
                new_col = piece_column + N_col
                if (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
                    if board[new_row][new_col][0] != cur_piece_side:
                        possible_boards.append(move(board, cur_piece_pos, new_row, new_col))
        for N_row in [-1,1]:
            for N_col in [-2,2]:
                new_row = piece_row + N_row
                new_col = piece_column + N_col
                if (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
                    if board[new_row][new_col][0] != cur_piece_side:
                        possible_boards.append(move(board, cur_piece_pos, new_row, new_col))

    return possible_boards

#define a function to find Kings' loc
def find_king(board,color):
    n = 0
    for i in board:
        if color == "W":
            if "WK" in i:
                return n,i.index("WK")
        elif color == "B":
            if "BK" in i:
                return n, i.index("BK")
        n += 1

#define the conditions for check
def is_check(board,color):
    K_row,K_col = find_king(board,color)
    if color == "W":
        #if there is a knight that make check
        for N_row in [-2,2]:
            for N_col in [-1,1]:
                new_row = K_row + N_row
                new_col = K_col + N_col
                if (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
                    if board[new_row][new_col] == "BN":
                        return True
        for N_row in [-1,1]:
            for N_col in [-2,2]:
                new_row = K_row + N_row
                new_col = K_col + N_col
                if (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
                    if board[new_row][new_col] == "BN":
                        return True
        # if there is a pawn that make check
        new_row = K_row - 1
        for n_col in [-1,1]:
            new_col = K_col + n_col
            if (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
                if board[new_row][new_col] == "BP":
                    return True
        # if there is a queen, rook or bishop that make check
        new_row = K_row + 1
        new_col = K_col + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row += 1
                new_col += 1
            elif board[new_row][new_col] in ["BQ","BB"]:
                return True
            else:
                break
        new_row = K_row - 1
        new_col = K_col + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row -= 1
                new_col += 1
            elif board[new_row][new_col] in ["BQ", "BB"]:
                return True
            else:
                break
        new_row = K_row + 1
        new_col = K_col - 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row += 1
                new_col -= 1
            elif board[new_row][new_col] in ["BQ", "BB"]:
                return True
            else:
                break
        new_row = K_row - 1
        new_col = K_col - 1
        while (new_row >=0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row -= 1
                new_col -= 1
            elif board[new_row][new_col] in ["BQ", "BB"]:
                return True
            else:
                break
        new_row = K_row
        new_col = K_col + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_col += 1
            elif board[new_row][new_col] in ["BQ", "BR"]:
                return True
            else:
                break
        new_row = K_row
        new_col = K_col - 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_col -= 1
            elif board[new_row][new_col] in ["BQ", "BR"]:
                return True
            else:
                break
        new_row = K_row + 1
        new_col = K_col
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row += 1
            elif board[new_row][new_col] in ["BQ", "BR"]:
                return True
            else:
                break
        new_row = K_row - 1
        new_col = K_col
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row -= 1
            elif board[new_row][new_col] in ["BQ", "BR"]:
                return True
            else:
                break
    elif color == "B":
        #if there is a knight that make check
        for N_row in [-2,2]:
            for N_col in [-1,1]:
                new_row = K_row + N_row
                new_col = K_col + N_col
                if (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
                    if board[new_row][new_col] == "WN":
                        return True
        for N_row in [-1,1]:
            for N_col in [-2,2]:
                new_row = K_row + N_row
                new_col = K_col + N_col
                if (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
                    if board[new_row][new_col] == "WN":
                        return True
        # if there is a pawn that make check
        new_row = K_row + 1
        for n_col in [-1,1]:
            new_col = K_col + n_col
            if (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
                if board[new_row][new_col] == "WP":
                    return True
        # if there is a queen, rook or bishop that make check
        new_row = K_row + 1
        new_col = K_col + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row += 1
                new_col += 1
            elif board[new_row][new_col] in ["WQ","WB"]:
                return True
            else:
                break
        new_row = K_row - 1
        new_col = K_col + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row -= 1
                new_col += 1
            elif board[new_row][new_col] in ["WQ", "WB"]:
                return True
            else:
                break
        new_row = K_row + 1
        new_col = K_col - 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row += 1
                new_col -= 1
            elif board[new_row][new_col] in ["WQ", "WB"]:
                return True
            else:
                break
        new_row = K_row - 1
        new_col = K_col - 1
        while (new_row >=0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row -= 1
                new_col -= 1
            elif board[new_row][new_col] in ["WQ", "WB"]:
                return True
            else:
                break
        new_row = K_row
        new_col = K_col + 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_col += 1
            elif board[new_row][new_col] in ["WQ", "WR"]:
                return True
            else:
                break
        new_row = K_row
        new_col = K_col - 1
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_col -= 1
            elif board[new_row][new_col] in ["WQ", "WR"]:
                return True
            else:
                break
        new_row = K_row + 1
        new_col = K_col
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row += 1
            elif board[new_row][new_col] in ["WQ", "WR"]:
                return True
            else:
                break
        new_row = K_row - 1
        new_col = K_col
        while (new_row >= 0 and new_row < 8) and (new_col >= 0 and new_col < 8):
            if board[new_row][new_col] == "--":
                new_row -= 1
            elif board[new_row][new_col] in ["WQ", "WR"]:
                return True
            else:
                break

#define the conditions for checkmate:
def is_checkmate(board,side):
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j][0] == side:
                possible_list = possible_movements(board,letters[j] + str(8-i))
                for pos_board in possible_list:
                    if not is_check(pos_board[0],side):
                        return False
    return True

#define the all possible movements for one side given a board
def all_moves(board,side):
    all_move_list = []
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j][0] == side:
                possible_list = possible_movements(board,letters[j] + str(8-i))
                if possible_list == []:
                    continue
                for pos_board in possible_list:
                    if not is_check(pos_board[0], side):
                        new_row = pos_board[1]
                        new_col = pos_board[2]
                        all_move_list.append(letters[j] + str(8 - i) + " " + letters[new_col] + str(8 - new_row))
    return all_move_list

def rec_solution_func(board,side,opponents_moves,n=0):#side is either "W" or "B"
    soln_list = []
    if side== "W":
        rival = "B"
    elif side == "B":
        rival = "W"
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j][0] == side:
                possible_list = possible_movements(board,letters[j] + str(8-i))
                for pos_board in possible_list:
                    new_row = pos_board[1]
                    new_col = pos_board[2]
                    if is_check(pos_board[0], side):
                        continue

                    if is_check(pos_board[0],rival):
                        correct_move = True
                        if len(opponents_moves) > n:
                            opp_boards = []
                            real_opp_moves = opponents_moves[n].split(",")
                            for opp_move in real_opp_moves:
                                opp_move = opp_move.split()
                                opp_row = 8- int(opp_move[1][1])
                                opp_col = letters.index(opp_move[1][0])
                                opp_boards.append(move(pos_board[0],opp_move[0],opp_row,opp_col))
                                if is_check(opp_boards[-1][0],rival):
                                    correct_move = False
                            if correct_move:
                                soln = [letters[j] + str(8-i)+" "+letters[new_col] + str(8-new_row)]
                                #print(letters[j] + str(8-i),letters[new_col] + str(8-new_row))
                                return soln + rec_solution_func(opp_boards[0][0],side,opponents_moves,n+1)

                        elif len(opponents_moves) == n:
                            if is_checkmate(pos_board[0],rival):
                                #print(letters[j] + str(8 - i), letters[new_col] + str(8 - new_row))
                                return [letters[j] + str(8-i)+" "+letters[new_col] + str(8-new_row)]
                    elif len(opponents_moves) > n:
                        real_opp_moves = opponents_moves[n].split(",")
                        all_pos_opp_moves = all_moves(pos_board[0],rival)
                        is_same = True
                        for opp_move in real_opp_moves:
                            if opp_move not in all_pos_opp_moves:
                                is_same = False
                        if (len(real_opp_moves) == len(all_pos_opp_moves)) and is_same:
                            opp_move = real_opp_moves[0].split()
                            opp_row = 8 - int(opp_move[1][1])
                            opp_col = letters.index(opp_move[1][0])
                            soln = [letters[j] + str(8-i)+" "+letters[new_col] + str(8-new_row)]
                            #print(letters[j] + str(8 - i), letters[new_col] + str(8 - new_row))
                            opp_board = move(pos_board[0],opp_move[0],opp_row,opp_col)
                            if rec_solution_func(opp_board[0], side, opponents_moves, n + 1) != []:
                                return soln + rec_solution_func(opp_board[0], side, opponents_moves, n + 1)
    return soln_list


#board_print(current_board)
solution_list  =rec_solution_func(current_board,my_side,opponent_list,0)
for solution in solution_list:
    print(solution)
#print(all_moves(current_board,"B"))
#print(opponent_list)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
