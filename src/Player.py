from dataclasses import dataclass

@dataclass
class Player:
    username: str

    def choose_piece_to_play(self):
        while True:
            try:
                piece_coordinate_x = int(input("Enter the row's variable between 0 and 7:"))
                piece_coordinate_y = int(input("Enter the colum's variable between 0 and 7:"))
            except ValueError:
                print('please enter a number')
                continue
            if board.pieces[piece_coordinate_x][piece_coordinate_y] is not None:
                if currentPlayer is player_white:
                    if board.pieces[piece_coordinate_x][piece_coordinate_y].colorPiece is piece.ColorPiece.WHITE:
                        print(f'You have selected {board.pieces[piece_coordinate_x][piece_coordinate_y].typePiece}')
                        break
                    else:
                        print("You have selected the wrong color!")
                        continue
                else:
                        if board.pieces[piece_coordinate_x][piece_coordinate_y].colorPiece is piece.ColorPiece.BLACK:
                            print(f'You have selected {board.pieces[piece_coordinate_x][piece_coordinate_y].typePiece}')
                            break
                        else:
                            print("You have selected the wrong color!")
                            continue
            elif board.pieces[piece_coordinate_x][piece_coordinate_y] is None:
                print("You have selected an empty square!")
            else:
                print("Please select a coordinate within the board")



    
    def choose_move_to_play():
        input()