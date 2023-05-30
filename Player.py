from dataclasses import dataclass
from Piece import Piece
from Piece import ColorPiece
from Piece import TypePiece


@dataclass
class Player:
    username: str

    def choose_piece_to_play(board, current_player, player_white, player_black):

        """
        Return a piece which the current player would like to play
        """

        while True:
            print("Please select the piece you would like to play...\n")
            try:
                piece_coordinate_x = int(input("Enter the row's variable between 0 and 7:\n"))
                if piece_coordinate_x > 7 or piece_coordinate_x < 0:
                    print("\nPlease enter a number between 0 and 7\n")
                    continue
                piece_coordinate_y = int(input("Enter the colum's variable between 0 and 7:\n"))
                if piece_coordinate_y > 7 or piece_coordinate_y < 0:
                    print("\nPlease enter a number between 0 and 7\n")
                    continue
            except ValueError:
                print('please enter a number\n')
                continue

            if board.pieces[piece_coordinate_x][piece_coordinate_y] is not None:
                if current_player is player_white:
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

        """
        Return the location to move the chosen piece from last function
        """

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

    def is_king_still_in_check(self, board, current_player, player_white, player_black, move_to_piece, piece_to_play, move_to_play, play_from_location):

        """
        Ensure the current player play the move to get out of the check
        """
        for rows in board.pieces:
            for piece in rows:
                if piece is not None:
                    if piece.typePiece is TypePiece.KING:
                        if piece.colorPiece is ColorPiece.WHITE:
                            white_king_location = piece.location
                        else:
                            black_king_location = piece.location

        all_moves = piece.list_all_moves(board)

        if current_player is player_white:
            king_location = white_king_location
        elif current_player is player_black:
            king_location = black_king_location

        if king_location in all_moves:
            while move_to_play in all_moves:
                print("\nYour king is in check! You should play something else!\n")
                piece_to_play.location = play_from_location
                board.pieces[play_from_location[0]][play_from_location[1]] = piece_to_play
                board.pieces[move_to_play[0]][move_to_play[1]] = move_to_piece
                piece_to_play = Player.choose_piece_to_play(board, current_player, player_white, player_black)
                move_to_play = Player.choose_move_to_play(piece_to_play, board)
                board.pieces[piece_to_play.location[0]][piece_to_play.location[1]] = None
                piece_to_play.location = (move_to_play[0], move_to_play[1])
                board.pieces[move_to_play[0]][move_to_play[1]] = piece_to_play
                new_all_moves = Piece.list_all_moves(self, board)
                if move_to_play in new_all_moves:
                    continue
                else:
                    break
