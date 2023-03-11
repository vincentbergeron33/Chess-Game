from dataclasses import dataclass
from enum import Enum
from typing import List
from itertools import product
from typing import List, Optional


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
    

    def __post_init__(self):
        self.startingLocation = self.location

    def isAtStartingLocation(self) -> bool:
        return self.startingLocation == self.location


    def movement(self, Board) -> List[(int, int)]:
        if self.typePiece is TypePiece.PAWN:
            return self.pawnValidMovePositions(Board) + self.pawnValidCapturePositions(Board)

        elif self.typePiece is TypePiece.ROOK:
            return self.rookValidMoveAndCapturePositions(Board)
        elif self.typePiece is TypePiece.KNIGHT:
            return self.knightValidMoveAndCapturePositions(Board)
        elif self.typePiece is TypePiece.KING:
            return self.kingValidMoveAndCapturePositions(Board)

        else:
            raise NotImplementedError()


    def isWithinBoard(self, location) -> bool:
        if 0 <= location[0] >= 7 and 0 <= location[1] >= 7:
            return True
        else:
            return False

    def pawnCanMoveTwo(self, Board):
        if self.ColorPiece is ColorPiece.WHITE:
            if Board.pieces[[self.location[0]][self.location[1]] + 1] is None:
                location_to_validate = [
                    Board.pieces[self.location[0], self.location[1] + 1],
                    Board.pieces[self.location[0], self.location[1] + 2]
                    ]
            else:
                return []
        else:
            if Board.pieces[self.location[0], self.location[1] - 1] is None:
                location_to_validate = [
                    Board.pieces[self.location[0], self.location[1] - 1],
                    Board.pieces[self.location[0], self.location[1] - 2]
                    ]

            else:
                return []

        piece_pawn_can_move_two: List[Piece] = (lambda piece: Board.pieces[location_to_validate[0]][location_to_validate[1]] is None, location_to_validate)
        return piece_pawn_can_move_two

    def pawnValidMovePositions(self, Board) -> List[(int, int)]:
        if self.isAtStartingLocation():
            piece_pawn_can_move = pawnCanMoveTwo()
        elif self.colorPiece is ColorPiece.WHITE:
            location_to_validate: List[Piece] = [
                Board.pieces[self.location[0]][self.location[1] + 1]
                ]
            piece_pawn_can_move: List [Piece] = (lambda piece: piece is not None and isWithinBoard(), location_to_validate)
        else:
            location_to_validate: List[Piece] = [
                Board.pieces[self.location[0]][self.location[1] - 1]
                ]
            piece_pawn_can_move: List [Piece] = (lambda piece: piece is not None and isWithinBoard(), location_to_validate)

        position_pawn_can_move = map(lambda piece: piece.location, piece_pawn_can_move)

        return position_pawn_can_move
             

    def pawnValidCapturePositions(self, Board) -> List[(int, int)]:
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

        pieces_pawn_can_capture: List[Piece] = filter(lambda piece: piece is not None and self.colorPiece is not piece.colorPiece, pieces_to_validate)
        positions_pawn_can_capture: List[(int, int)] = map(lambda piece: piece.location, pieces_pawn_can_capture)

        return positions_pawn_can_capture

    def rookValidMoveAndCapturePositions(self, Board) -> List[(int, int)]:
        piece_to_validate_up = [[Board.pieces[self.location[0]][self.location[1] + 1]]]

        piece_up_rook: List[Piece] = []

        while piece_to_validate_up is None and isWithinBoard(piece_to_validate_up):
            piece_up_rook = piece_up_rook.append(piece_to_validate_up)
            piece_to_validate_up = Board.pieces[[piece_to_validate_up[0]][piece_to_validate_up[1] + 1]]
            if piece_to_validate_up is not None and self.colorPiece is not piece.ColorPiece:
                piece_up_rook = piece_up_rook.append(piece_to_validate_up)
                break
            elif piece_to_validate_up is not None and self.colorPiece is piece.ColorPiece:
                break
        return piece_up_rook

        piece_to_validate_down = [[Board.pieces[self.location[0]][self.location[1] - 1]]]
        piece_down_rook: List[Piece] = []

        while piece_to_validate_down is None and isWithinBoard(piece_to_validate_down):
            piece_down_rook = piece_down_rook.append(piece_to_validate_down)
            piece_to_validate_down = Board.pieces[[piece_to_validate_down[0]][piece_to_validate_down[1] - 1]]
            if piece_to_validate_down is not None and self.colorPiece is not piece.ColorPiece:
                piece_down_rook = piece_down_rook.append(piece_to_validate_down)
                break
            elif piece_to_validate_down is not None and self.colorPiece is piece.ColorPiece:
                break
        return piece_down_rook

        piece_to_validate_right = [[Board.pieces[self.location[0] + 1][self.location[1]]]]
        piece_right_rook: List[Piece] = []

        while piece_to_validate_right is None and isWithinBoard(piece_to_validate_right):
            piece_right_rook = piece_right_rook.append(piece_to_validate_right)
            piece_to_validate_right = Board.pieces[[piece_to_validate_right[0] + 1][piece_to_validate_right[1]]]
            if piece_to_validate_right is not None and self.colorPiece is not piece.ColorPiece:
                piece_right_rook = piece_right_rook.append(piece_to_validate_right)
                break
            elif piece_to_validate_right is not None and self.colorPiece is piece.ColorPiece:
                break
        return piece_right_rook

        piece_to_validate_left = [[Board.pieces[self.location[0] - 1][self.location[1]]]]
        piece_left_rook: List[Piece] = []

        while piece_to_validate_left is None and isWithinBoard(piece_to_validate_left):
            piece_left_rook = piece_left_rook.append(piece_to_validate_left)
            piece_to_validate_left = Board.pieces[[piece_to_validate_left[0] - 1][piece_to_validate_left[1]]]
            if piece_to_validate_left is not None and self.colorPiece is not piece.ColorPiece:
                piece_left_rook = piece_left_rook.append(piece_to_validate_left)
                break
            elif piece_to_validate_left is not None and self.colorPiece is piece.ColorPiece:
                break
        return piece_left_rook

        valide_move_and_capture_piece_rook = []
        valide_move_and_capture_piece_rook = valide_move_and_capture_piece_rook.append(piece_up_rook)
        valide_move_and_capture_piece_rook = valide_move_and_capture_piece_rook.append(piece_down_rook)
        valide_move_and_capture_piece_rook = valide_move_and_capture_piece_rook.append(piece_right_rook)
        valide_move_and_capture_piece_rook = valide_move_and_capture_piece_rook.append(piece_left_rook)

        valide_move_and_capture_location_rook: List[(int, int)] = map(lambda piece: piece.location, valide_move_and_capture_piece_rook)

        return valide_move_and_capture_location_rook

    def bishopValidMoveAndCapturePositions(self, Board,) -> List[(int, int)]:
        piece_to_validate_up_right = [[Board.pieces[self.location[0] + 1][self.location[1] + 1]]]

        piece_up_right_bishop: List[Piece] = []

        while piece_to_validate_up_right is None and isWithinBoard(piece_to_validate_up_right):
            piece_up_right_bishop = piece_up_right_bishop.append(piece_to_validate_up_right)
            piece_to_validate_up_right = Board.pieces[[piece_to_validate_up[0] + 1][piece_to_validate_up[1] + 1]]
            if piece_to_validate_up_right is not None and self.colorPiece is not piece.ColorPiece:
                piece_up_right_bishop = piece_up_right_bishop.append(piece_to_validate_up_right)
                break
            elif piece_to_validate_up_right is not None and self.colorPiece is piece.ColorPiece:
                break
        return piece_up_right_bishop

    def knightValidMoveAndCapturePositions(self, Board, piece) -> List[(int, int)]:
        x = self.location[0]
        y = self.location[1]
        location_to_validate = list(product([x - 1, x + 1], [y - 2, x - 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
        for location in location_to_validate:
            if isWithinBoard(location):
                if location is not piece.location:
                    valide_move_location_knight = []
                    valide_move_location_knight = valide_move_location_knight.append(location)
                    return valide_move_location_bishop
                elif location is piece.location and self.colorPiece is not piece.ColorPiece:
                    valide_capture_location_knight = []
                    valide_capture_location_knight = valide_capture_location_knight.append(location)
                    return valide_capture_location_knight
                else:
                    continue
        return valide_capture_location_knight
        
        valide_move_and_capture_location_knight = []
        valide_move_and_capture_location_knight = valide_move_and_capture_location_knight.append(valide_move_location_knight)
        valide_move_and_capture_location_knight = valide_move_and_capture_location_knight.append(valide_capture_location_knight)
        return valide_move_and_capture_location_knight

    def kingValidMoveAndCapturePositions(self, Board, piece) -> List[(int, int)]:
        x = self.location[0]
        y = self.location[1]
        location_to_validate = [
            [x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1],
             [x + 1, y + 1], [x - 1, y + 1], [x + 1, y - 1], [x - 1, y + 1]
             ]
        for location in location_to_validate:
            if isWithinBoard(location):
                if location is not piece.location:
                    valide_move_location_king = []
                    valide_move_location_kind = valide_move_location_king.append(location)
                    return valide_move_location_king
                elif location is piece.location and self.colorPiece is not piece.ColorPiece:
                    valide_capture_location_king = []
                    valide_capture_location_king = valide_capture_location_king.append(location)
                    return valide_capture_location_king
                else:
                    continue
            else:
                continue
        valide_move_and_capture_location_king = []
        valide_move_and_capture_location_king = valide_move_and_capture_location_king.append(valide_move_location_king)
        valide_move_and_capture_location_king = valide_move_and_capture_location_king.append(valide_capture_location_king)
        return valide_move_and_capture_location_king
            

    
@dataclass
class Board:
    pieces: List[List[Optional[Piece]]]

    def printPiecesOnBoard(typePiece, colorPiece):
        if TypePiece is typePiece.PAWN:
            if ColorPiece is colorPiece.WHITE:
                print('WP')
            else:
                print('BP')
        elif typePiece is typePiece.ROOK:
            if colorPiece is colorPiece.WHITE:
                Print(WR)
            else:
                print(BR)
        elif typePiece is typePiece.BISHOP:
            if colorPiece is colorPiece.WHITE:
                Print(WB)
            else:
                print(BB)
        elif TypePiece is typePiece.KNIGHT:
            if colorPiece is colorPiece.WHITE:
                Print(WK)
            else:
                print(BK)
        elif typePiece is typePiece.QUEEN:
            if colorPiece is colorPiece.WHITE:
                Print(WQ)
            else:
                print(BQ)
        elif typePiece is typePiece.KING:
            if colorPiece is colorPiece.WHITE:
                Print(WK)
            else:
                print(BK)

    def printboard(self):
        for i in range(0, len(self.pieces)):
            for j in range(0, len(self.pieces[i])):
                piece = self.pieces[i][j]
                if piece is not None:
                    printPiecesOnBoard(piece.typePiece, piece.ColorPiece)
                else:
                    print(' ')

