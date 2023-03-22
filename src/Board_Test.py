import unittest

from Piece import Board
from Piece import Piece
from Piece import TypePiece
from Piece import ColorPiece


class Boardtest(unittest.TestCase):

    def test_pawn_can_capture(self):
        board = Board(pieces = [
                [Piece(TypePiece.ROOK, ColorPiece.BLACK, (0, 0)), Piece(TypePiece.KNIGHT, ColorPiece.BLACK, (0, 1)), Piece(TypePiece.BISHOP, ColorPiece.BLACK, (0, 2)), Piece(TypePiece.QUEEN, ColorPiece.BLACK, (0, 3)), Piece(TypePiece.KING, ColorPiece.BLACK, (0, 4)), Piece(TypePiece.BISHOP, ColorPiece.BLACK, (0, 5)), Piece(TypePiece.KNIGHT, ColorPiece.BLACK, (0, 6)), Piece(TypePiece.ROOK, ColorPiece.BLACK, (0, 7))],
                [Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 0)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 1)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 2)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 3)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 4)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 5)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 6)), Piece(TypePiece.PAWN, ColorPiece.BLACK, (1, 7))],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 0)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 1)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 2)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 3)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 4)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 5)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 6)), Piece(TypePiece.PAWN, ColorPiece.WHITE, (6, 7))],
                [Piece(TypePiece.ROOK, ColorPiece.WHITE, (7, 0)), Piece(TypePiece.KNIGHT, ColorPiece.WHITE, (7, 1)), Piece(TypePiece.BISHOP, ColorPiece.WHITE, (7, 2)), Piece(TypePiece.QUEEN, ColorPiece.WHITE, (7, 3)), Piece(TypePiece.KING, ColorPiece.WHITE, (7, 4)), Piece(TypePiece.BISHOP, ColorPiece.WHITE, (7, 5)), Piece(TypePiece.KNIGHT, ColorPiece.WHITE, (7, 6)), Piece(TypePiece.ROOK, ColorPiece.WHITE, (7, 7))]
                ])



        dictionary_moves = {}
        for rows in board.pieces:
            for piece in rows:
                if piece is not None:
                        list_of_list = piece.movement(board)
                        for location in list_of_list:
                            dictionary_moves[piece.location] = location
        print(dictionary_moves)
        piece_to_kill_location = [k for k, v in dictionary_moves.items() if v == (5, 4)]
        print(piece_to_kill_location)

        #Piece.checkmate(board)


                
        print(board.pieces[1][0])
        actual_movement = board.pieces[5][1].movement(board)
        expected_movement = [(0, 0), (0, 1)]
        final = actual_movement

        print("printing actual movement...")
        return print(final)


boardtest = Boardtest()
pawnmove = boardtest.test_pawn_can_capture()