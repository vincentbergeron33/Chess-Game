import unittest

from Piece import Board
from Piece import Piece
from Piece import TypePiece
from Piece import ColorPiece


class Boardtest(unittest.TestCase, Board, Piece):

    def test_pawn_can_capture(Board):
        Board.pieces = [
                [None, Piece(TypePiece.PAWN, ColorPiece.BLACK, (0, 1)), None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [Piece(TypePiece.PAWN, ColorPiece.BLACK, (5, 0)), Piece(TypePiece.ROOK, ColorPiece.WHITE, (5, 1)), None, None, None, None, None, Piece(TypePiece.PAWN, ColorPiece.BLACK, (5, 7))],
                [None, None, None, None, None, None, None, None],
                [Piece(TypePiece.PAWN, ColorPiece.WHITE, (7, 0)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (7, 1)), None, None, None, None, None, None],
            ]
        
        test = print(Board.pieces[1][0])
        actual_movement = Board.pieces[5][1].movement(Board)
        expected_movement = [(0, 0), (0, 1)]
        final = actual_movement

        print("printing actual movement...")
        return print(final)


pawnmove = Boardtest.test_pawn_can_capture(Board)
