from dataclasses import dataclass
from enum import Enum
from typing import List

from src.Board import Board


class TypePiece(Enum):
    PAWN = 1
    ROOK = 2
    BISHOP = 3
    KNIGHT = 4
    QUEEN = 5
    KING = 6


class ColorPiece(Enum):
    BLACK = 1
    WHITE = 2


@dataclass
class Piece:
    typePiece: TypePiece
    colorPiece: ColorPiece
    location: (int, int)

    def movement(self, board: Board) -> List[(int, int)]:
        if self.typePiece is TypePiece.PAWN:
            return self.pawnValidMovePositions(board) + self.pawnValidCapturePositions(board)

        elif self.typePiece is TypePiece.ROOK:
            return self.rookValidMovePositions(board) + self.rookValidCapturePositions(board)

        else:
            raise NotImplemented


# Vince adding code here

    def pawnValidMovePositions(self, board: Board) -> List[(int, int)]:
        if self.colorPiece is ColorPiece.WHITE:
            location_to_validate: List[Piece] = [
            board.pieces[self.location[0]][self.location[1] + 1]
            ]
        elif:
            location_to_validate: List[Piece] = [
            board.pieces[self.location[0]][self.location[1] - 1]
            ]
        else:
            raise NotImplemented
        
        piece_pawn_can_move : List [Piece] = (lambda piece: self.location is not piece.location, location_to_validate)

        return position_pawn_can_move
        
# End of Vince's code for pawn movement. I guess the raise NotImplemented is not required? Now that we have the available
# position to move and capture, we can call the functions in the PawnValidMovePositions? We are just missing the last restriction
# which is the board


    def pawnValidCapturePositions(self, board:Board) -> List[(int, int)]:
        if self.colorPiece is ColorPiece.WHITE:
            pieces_to_validate: List[Piece] = [
                board.pieces[self.location[0] + 1][self.location[1] + 1],
                board.pieces[self.location[0] - 1][self.location[1] + 1],
            ]
        else:
            pieces_to_validate: List[Piece] = [
                board.pieces[self.location[0] + 1][self.location[1] -1],
                board.pieces[self.location[0] - 1][self.location[1] - 1],
            ]

        pieces_pawn_can_capture: List[Piece] = filter(lambda piece: self.colorPiece is not piece.colorPiece, pieces_to_validate)
        positions_pawn_can_capture: List[(int, int)] = map(lambda piece: piece.location, pieces_pawn_can_capture)

        return positions_pawn_can_capture

#Vince adding ROOK here
    def rookValidMovePositions(self, board: Board) -> List[(int, int)]:
        piece_to_validate_up = [[board.pieces[self.location[0]][self.location[1] + 1]]]

        if piece_to_validate_up is piece.location and self.ColorPiece is not piece.ColorPiece:
            location_to_capture_top = piece_to_validate_up
            return location_to_capture_top

        elif piece_to_validate_up is piece.location and self.ColorPiece is piece.ColorPiece:
            break

        else:
            while piece_to_validate_up is not piece.location and withinBoard(self.location):
                location_up_rook: Liste[Piece] = []
                location_up_rook.append(piece_to_validate_up)
                piece_to_validate_up = [piece_to_validate_up[0]][piece_to_validate_up[1] + 1]
            return location_up_rook


        piece_to_validate_down = [board.pieces[self.location[0]][self.location[1] - 1]]

        if piece_to_validate_down is piece.location and self.ColorPiece is not piece.ColorPiece:
            location_to_capture_down = piece_to_validate_down
            return location_to_capture_down

        elif piece_to_validate_down is piece.location and self.ColorPiece is piece.ColorPiece:
            break

        else:
            while piece_to_validate_down is not piece.location and withinBoard(self.location):
                location_down_rook: Liste[Piece] = []
                location_down_rook.append(piece_to_validate_down)
                piece_to_validate_down = [piece_to_validate_down[0]][piece_to_validate_down[1] - 1]
            return location_down_rook


        piece_to_validate_right = [board.pieces[self.location[0] + 1][self.location[1]]]

        if piece_to_validate_right is piece.location and self.ColorPiece is not piece.ColorPiece:
            location_to_capture_right = piece_to_validate_right
            return location_to_capture_right

        elif piece_to_validate_right is piece.location and self.ColorPiece is piece.ColorPiece:
            break

        else:
            while piece_to_validate_right is not piece.location and withinBoard(self.location):
                location_right_rook: Liste[Piece] = []
                location_right_rook.append(piece_to_validate_right)
                piece_to_validate_right = [piece_to_validate_right[0] + 1][piece_to_validate_right[1]]
            return location_right_rook


        piece_to_validate_left = [board.pieces[self.location[0] - 1][self.location[1]]]

        if piece_to_validate_left is piece.location and self.ColorPiece is not piece.ColorPiece:
            location_to_capture_left = piece_to_validate_left
            return location_to_capture_left

        elif piece_to_validate_left is piece.location and self.ColorPiece is piece.ColorPiece:
            break

        else:
            while piece_to_validate_left is not piece.location and withinBoard(self.location):
                location_left_rook: Liste[Piece] = []
                location_left_rook.append(piece_to_validate_left)
                piece_to_validate_left = [piece_to_validate_left[0] - 1][piece_to_validate_left[1]]
            return location_left_rook

    
    valide_move_and_capture_location_rook = location_up_rook + location_down_rook + location_right_rook + location_left_rook 

    return valide_move_and_capture_location_rook


