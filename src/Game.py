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
        while checkmate is not True:
            game.set_player_turn()
            self.board.printboard(board)
            piece_to_play = Player.choose_piece_to_play(board, game, players)
            move_to_play = Player.choose_move_to_play(piece_to_play, board)
            
            board.pieces[piece_to_play.location[0]][piece_to_play.location[1]] = None
            piece_to_play.location = (move_to_play[0], move_to_play[1])
            board.pieces[move_to_play[0]][move_to_play[1]] = piece_to_play
            Piece.checkmate_capture(self, board, game.currentPlayer, game.player_black, game.player_white)

    def set_player_turn(self):
        if game.currentPlayer is players[0]:
            game.currentPlayer = players[1]
            print('\nIt is black turn')
        else:
            game.currentPlayer = players[0]
            print('\nIt is white turn')


checkmate = False


def set_up_board() -> Board:
    starting_board = Board(pieces=[
        [Piece(TypePiece.ROOK, ColorPiece.BLACK, (0, 0)), Piece(TypePiece.KNIGHT, ColorPiece.BLACK, (0, 1)), Piece(TypePiece.BISHOP, ColorPiece.BLACK, (0, 2)), Piece(TypePiece.QUEEN, ColorPiece.BLACK, (0, 3)), Piece(TypePiece.KING, ColorPiece.BLACK, (0, 4)), Piece(TypePiece.BISHOP, ColorPiece.BLACK, (0, 5)), Piece(TypePiece.KNIGHT, ColorPiece.BLACK, (0, 6)), Piece(TypePiece.ROOK, ColorPiece.BLACK, (0, 7))],
        [Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 0)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 1)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 2)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 3)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 4)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 5)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 6)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 7))],
        [None, Piece(TypePiece.KING, ColorPiece.WHITE, (2, 1)), None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 0)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 1)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 2)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 3)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 4)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 5)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 6)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 7))],
        [Piece(TypePiece.ROOK, ColorPiece.WHITE, (7, 0)), Piece(TypePiece.KNIGHT, ColorPiece.WHITE, (7, 1)), Piece(TypePiece.BISHOP, ColorPiece.WHITE, (7, 2)), Piece(TypePiece.QUEEN, ColorPiece.WHITE, (7, 3)), None, Piece(TypePiece.BISHOP, ColorPiece.WHITE, (7, 5)), Piece(TypePiece.KNIGHT, ColorPiece.WHITE, (7, 6)), Piece(TypePiece.ROOK, ColorPiece.WHITE, (7, 7))]
        ])
    return starting_board


board = set_up_board()


def set_up_players() -> Tuple[Player, Player]:
    player_white_name = input("Enter white player name:")
    player_black_name = input("Enter black player name:")
    player_white = Player(player_white_name)
    player_black = Player(player_black_name)

    return (player_white, player_black)

    
players = set_up_players()

game = Game(board, players[0], players[1], currentPlayer=players[1])

game.run_game()