from dataclasses import dataclass
from Piece import Piece
from Piece import ColorPiece

@dataclass
class Player:
    username: str

    def choose_piece_to_play(board, game, players):
        while True:
            print("Please select the piece you would like to play...\n")
            try:
                piece_coordinate_x = int(input("Enter the row's variable between 0 and 7:"))
                piece_coordinate_y = int(input("Enter the colum's variable between 0 and 7:"))
            except ValueError:
                print('please enter a number')
                continue
            if board.pieces[piece_coordinate_x][piece_coordinate_y] is not None:
                if game.currentPlayer is players[0]:
                    if board.pieces[piece_coordinate_x][piece_coordinate_y].colorPiece is ColorPiece.WHITE:
                        piece_to_validate = board.pieces[piece_coordinate_x][piece_coordinate_y]
                        if piece_to_validate.movement(board):
                            print(f'You have selected {piece_to_validate.typePiece} at location ({piece_coordinate_x}, {piece_coordinate_y})')
                            break
                        else:
                            print("\nThis piece has no possible move!\n")
                            continue

                    else:
                        print("\nYou have selected the wrong color!\n")
                        continue
                else:
                    if board.pieces[piece_coordinate_x][piece_coordinate_y].colorPiece is ColorPiece.BLACK:
                        piece_to_validate = board.pieces[piece_coordinate_x][piece_coordinate_y]
                        if piece_to_validate.movement(board):
                            print(f'You have selected {piece_to_validate.typePiece} at location ({piece_coordinate_x}, {piece_coordinate_y})')
                            break
                        else:
                            print("\nThis piece has no possible move!\n")
                            continue
                    else:
                        print("\nYou have selected the wrong color!\n")
                        continue
            elif board.pieces[piece_coordinate_x][piece_coordinate_y] is None:
                print("\nYou have selected an empty square!\n")
                continue
            else:
                print("\nPlease select a coordinate within the board\n")
                continue
        return board.pieces[piece_coordinate_x][piece_coordinate_y]



    
    def choose_move_to_play(piece_to_play, board):
        print("\nPlease select the location you would like to move your piece\n")
        print("Find below the available move:")
        print(piece_to_play.movement(board))

        while True:
            try:
                piece_coordinate_x = int(input("Enter the row's variable between 0 and 7:"))
                piece_coordinate_y = int(input("Enter the colum's variable between 0 and 7:"))
            except ValueError:
                print('please enter a number')
            new_position = (piece_coordinate_x, piece_coordinate_y)
            if new_position in piece_to_play.movement(board):
                print(f"{piece_to_play.typePiece} has been moved to {new_position}")
                break
            else:
                print("Please select a valid move")
                continue
        return new_position
