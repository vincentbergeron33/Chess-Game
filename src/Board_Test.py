import unittest

from Piece import Board
from Piece import Piece
from Piece import TypePiece
from Piece import ColorPiece


class Boardtest(unittest.TestCase):

    def corresponding_keys(self, val, dictionary):
        keys = []
        for k, v in dictionary.items():
            if val in v:
                keys.append(k)
        return keys

    def test_pawn_can_capture(self):
        board = Board(pieces = [
                [Piece(TypePiece.ROOK, ColorPiece.BLACK, (0, 0)), Piece(TypePiece.KNIGHT, ColorPiece.WHITE, (0, 1)), Piece(TypePiece.BISHOP, ColorPiece.BLACK, (0, 2)), Piece(TypePiece.QUEEN, ColorPiece.BLACK, (0, 3)), Piece(TypePiece.KING, ColorPiece.BLACK, (0, 4)), Piece(TypePiece.BISHOP, ColorPiece.BLACK, (0, 5)), Piece(TypePiece.KNIGHT, ColorPiece.BLACK, (0, 6)), Piece(TypePiece.ROOK, ColorPiece.BLACK, (0, 7))],
                [Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 0)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 1)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 2)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 3)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 4)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 5)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 6)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 7))],
                [ Piece(TypePiece.KING, ColorPiece.WHITE, (2, 0)), None, Piece(TypePiece.PAWN, ColorPiece.WHITE, (4, 2)), None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 0)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 1)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 2)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 3)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 4)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 5)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 6)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 7))],
                [Piece(TypePiece.ROOK, ColorPiece.WHITE, (7, 0)), Piece(TypePiece.KNIGHT, ColorPiece.WHITE, (7, 1)), Piece(TypePiece.BISHOP, ColorPiece.WHITE, (7, 2)), Piece(TypePiece.QUEEN, ColorPiece.WHITE, (7, 3)), None, Piece(TypePiece.BISHOP, ColorPiece.WHITE, (7, 5)), Piece(TypePiece.KNIGHT, ColorPiece.WHITE, (7, 6)), Piece(TypePiece.ROOK, ColorPiece.WHITE, (7, 7))]
                ])

        for rows in board.pieces:
            for piece in rows:
                if piece is not None:
                    if piece.typePiece is TypePiece.KING:
                        if piece.colorPiece is ColorPiece.WHITE:
                            white_king_location = piece.location
                        else:
                            black_king_location = piece.location

        dictionary_moves = {}
        for rows in board.pieces:
            for piece in rows:
                if piece is not None:
                    dictionary_moves[piece.location] = piece.movement(board)
        all_moves = []
        for rows in board.pieces:
            for piece in rows:
                if piece is not None:
                    all_moves = all_moves + piece.movement(board)
        

        #piece_to_kill_location = self.corresponding_keys(white_king_location, dictionary_moves)
        #print(piece_to_kill_location)
        Piece.checkmate_capture(self, board)




                


boardtest = Boardtest()
pawnmove = boardtest.test_pawn_can_capture()