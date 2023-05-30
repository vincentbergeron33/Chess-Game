from dataclasses import dataclass
from Piece import Board
from Player import Player
from typing import Tuple
from Piece import Piece
from Piece import TypePiece
from Piece import ColorPiece


@dataclass
class Game():
    board: Board
    player_white: Player
    player_black: Player
    currentPlayer: Player

    def run_game(self):

        """
        Main function to run the game and all other functions
        """
        checkmate = False
        while checkmate is False:
            game.set_player_turn()
            if Piece.checkmate(board, game.currentPlayer, players[0], players[1]):
                break

            self.board.printboard(board)
            piece_to_play = Player.choose_piece_to_play(board, game.currentPlayer, players[0], players[1])
            move_to_play = Player.choose_move_to_play(piece_to_play, board)

            move_to_piece = board.pieces[move_to_play[0]][move_to_play[1]]
            play_from_location = piece_to_play.location

            board.pieces[piece_to_play.location[0]][piece_to_play.location[1]] = None
            piece_to_play.location = (move_to_play[0], move_to_play[1])
            board.pieces[move_to_play[0]][move_to_play[1]] = piece_to_play

            Player.is_king_still_in_check(self, board, game.currentPlayer, players[0], players[1], move_to_piece, piece_to_play, move_to_play, play_from_location)

        print("End of game")

    def set_player_turn(self):

        """
        Set the current player
        """

        if game.currentPlayer is players[0]:
            game.currentPlayer = players[1]
            print(f"\nIt is {game.currentPlayer.username}'s turn")
        else:
            game.currentPlayer = players[0]
            print(f"\nIt is {game.currentPlayer.username}'s turn")


def set_up_board() -> Board:

    """
    Set the board at the begining of the game
    """
    starting_board = Board(pieces=[
        [Piece(TypePiece.ROOK, ColorPiece.BLACK, (0, 0)), Piece(TypePiece.KNIGHT, ColorPiece.BLACK, (0, 1)), Piece(TypePiece.BISHOP, ColorPiece.BLACK, (0, 2)), Piece(TypePiece.QUEEN, ColorPiece.BLACK, (0, 3)), Piece(TypePiece.KING, ColorPiece.BLACK, (0, 4)), Piece(TypePiece.BISHOP, ColorPiece.BLACK, (0, 5)), Piece(TypePiece.KNIGHT, ColorPiece.BLACK, (0, 6)), Piece(TypePiece.ROOK, ColorPiece.BLACK, (0, 7))],
        [Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 0)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 1)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 2)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 3)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 4)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 5)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 6)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 7))],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 0)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 1)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 2)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 3)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 4)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 5)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 6)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 7))],
        [Piece(TypePiece.ROOK, ColorPiece.WHITE, (7, 0)), Piece(TypePiece.KNIGHT, ColorPiece.WHITE, (7, 1)), Piece(TypePiece.BISHOP, ColorPiece.WHITE, (7, 2)), Piece(TypePiece.QUEEN, ColorPiece.WHITE, (7, 3)), Piece(TypePiece.KING, ColorPiece.WHITE, (7, 4)), Piece(TypePiece.BISHOP, ColorPiece.WHITE, (7, 5)), Piece(TypePiece.KNIGHT, ColorPiece.WHITE, (7, 6)), Piece(TypePiece.ROOK, ColorPiece.WHITE, (7, 7))]
        ])
    return starting_board


board = set_up_board()


def set_up_players() -> Tuple[Player, Player]:
    """
    Set the player name for each player
    """
    while True:
        try:
            player_white_name = input("Enter white player name:")
            if not player_white_name:
                raise ValueError('\nPlease input an username\n')
            player_black_name = input("Enter black player name:")
            if not player_black_name:
                raise ValueError('\nPlease input an username\n')
            if player_white_name and player_black_name:
                player_white = Player(player_white_name)
                player_black = Player(player_black_name)
                print(f'\nWhite player is {player_white.username} and black player is {player_black.username}')
                break
        except ValueError as e:
            print(e)
    return [player_white, player_black]


players = set_up_players()

game = Game(board, players[0], players[1], players[1])

game.run_game()
