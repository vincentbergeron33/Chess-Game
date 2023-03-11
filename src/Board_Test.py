import unittest

from Piece import Board
from Piece import Piece
from Piece import TypePiece
from Piece import ColorPiece


class Boardtest(unittest.TestCase, Board, Piece):

    def test_pawn_can_capture(self):
        board = Board()
        board = Board_squares.pieces[
                [None, Piece(TypePiece.PAWN, ColorPiece.WHITE, (0, 1))],
                [Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 0)), None],
            ]

        actual_movement = board[0][1].movement(board)
        expected_movement = [(1, 1), (0, 1)]

        self.assertEqual(actual_movement, expected_movement)  
        return print(actual_movement)


Boardtest.test_pawn_can_capture(1)