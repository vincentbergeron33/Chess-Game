import unittest

from Board import Board
from Piece import Piece
from Piece import TypePiece
from Piece import ColorPiece


class Boardtest(unittest.TestCase):

    def test_pawn_can_capture(self):
        board = Board(
            [
                [None, Piece(TypePiece.PAWN, ColorPiece.WHITE, (0, 1))],
                [Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 0)), None],
            ])

        actual_movement = board[0][1].movement(board)
        expected_movement = [(1,1), (0,1)]

        assert(actual_movement)(expected_movement)       
