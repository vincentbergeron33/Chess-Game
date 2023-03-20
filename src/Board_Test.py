import unittest

from Piece import Board
from Piece import Piece
from Piece import TypePiece
from Piece import ColorPiece


class Boardtest(unittest.TestCase):

    def test_pawn_can_capture(self):
        board = Board(pieces = [
                [None, Piece(TypePiece.PAWN, ColorPiece.BLACK, (0, 1)), None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [Piece(TypePiece.PAWN, ColorPiece.BLACK, (5, 0)), Piece(TypePiece.QUEEN, ColorPiece.WHITE, (5, 1)), None, None, None, None, None, Piece(TypePiece.PAWN, ColorPiece.BLACK, (5, 7))],
                [None, Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 1)), None, None, None, None, None, None],
                [Piece(TypePiece.PAWN, ColorPiece.BLACK, (7, 0)), Piece(TypePiece.KNIGHT, ColorPiece.WHITE, (7, 1)), None, None, None, None, None, None],
                ])
        
        print(board.pieces[1][0])
        actual_movement = board.pieces[5][1].movement(board)
        expected_movement = [(0, 0), (0, 1)]
        final = actual_movement

        print("printing actual movement...")
        return print(final)


boardtest = Boardtest()
pawnmove = boardtest.test_pawn_can_capture()