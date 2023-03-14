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

    def is_at_starting_location(self) -> bool:
        return self.startingLocation == self.location

    def movement(self, Board) -> List[int]:
        if self.typePiece is TypePiece.PAWN:
            valid_capture_pawn = self.pawn_valid_captures(Board)
            valid_move_pawn = self.pawn_valid_moves(Board)
            valid_move_pawn = valid_move_pawn.append(valid_capture_pawn)
            return valid_move_pawn
        elif self.typePiece is TypePiece.ROOK:
            return self.rook_valid_moves(Board)
        elif self.typePiece is TypePiece.BISHOP:
            return self.bishop_valid_moves(Board)
        elif self.typePiece is TypePiece.QUEEN:
            return self.queen_valid_moves(Board)
        elif self.typePiece is TypePiece.KNIGHT:
            return self.knight_valid_moves(Board)
        elif self.typePiece is TypePiece.KING:
            return self.king_valid_moves(Board)
        else:
            raise NotImplementedError()

    def is_within_board(self, location) -> bool:
        if 0 <= location[0] >= 7 and 0 <= location[1] >= 7:
            return True
        else:
            return False

    def pawn_can_move_two(self, Board):
        if self.colorPiece is ColorPiece.WHITE:
            if Board.pieces[self.location[0]][self.location[1] -1] is None:
                location_to_validate = [
                    Board.pieces[self.location[0]][self.location[1] - 1],
                    Board.pieces[self.location[0]][self.location[1] - 2]
                    ]
                print("Two move return locations")
            else:
                print("Two returns nothing")
                return []
        else:
            if Board.pieces[self.location[0]][self.location[1] + 1] is None:
                location_to_validate = [
                    Board.pieces[self.location[0], self.location[1] + 1],
                    Board.pieces[self.location[0], self.location[1] + 2]
                    ]

            else:
                return []

        piece_pawn_can_move_two: List[Piece] = filter(lambda piece: piece is None, location_to_validate)
        print(piece_pawn_can_move_two)
        return piece_pawn_can_move_two

    def pawn_valid_moves(self, Board) -> List[int]:
        if self.is_at_starting_location():
            piece_pawn_can_move = self.pawn_can_move_two(Board)
            print("Move Two has started")
            print(piece_pawn_can_move)
        elif self.colorPiece is ColorPiece.WHITE:
            location_to_validate: List[Piece] = [
                Board.pieces[self.location[0]][self.location[1] - 1]
                ]
            piece_pawn_can_move: List[Piece] = (lambda piece: piece is None and location_to_validate.is_within_board(), location_to_validate)
        else:
            location_to_validate: List[Piece] = [
                Board.pieces[self.location[0]][self.location[1] + 1]
                ]
            piece_pawn_can_move: List[Piece] = (lambda piece: piece is None and location_to_validate.is_within_board(), location_to_validate)

        position_pawn_can_move = list(map(lambda piece: piece.location, piece_pawn_can_move))
        print(position_pawn_can_move)

        return position_pawn_can_move      

    def pawn_valid_captures(self, Board) -> List[int]:
        if self.colorPiece is ColorPiece.WHITE:
            pieces_to_validate: List[Piece] = [
                Board.pieces[self.location[0] - 1][self.location[1] + 1],
                Board.pieces[self.location[0] - 1][self.location[1] - 1],
            ]
            print("Capture when White!")
            print(pieces_to_validate)
        else:
            pieces_to_validate: List[Piece] = [
                Board.pieces[self.location[0] + 1][self.location[1] + 1],
                Board.pieces[self.location[0] + 1][self.location[1] - 1],
            ]

        pieces_pawn_can_capture: List[Piece] = filter(lambda piece: piece is not None and self.colorPiece is not piece.colorPiece, pieces_to_validate)
        print(pieces_pawn_can_capture)
        positions_pawn_can_capture: List[int] = list(map(lambda piece: piece.location, pieces_pawn_can_capture))
        print(positions_pawn_can_capture)

        return positions_pawn_can_capture

    def rook_valid_moves(self, Board) -> List[int]:

        piece_to_validate_up = [Board.pieces[[self.location[0]][self.location[1] + 1]]]
        piece_up_rook: List[Piece] = []

        while piece_to_validate_up is None and is_within_board(piece_to_validate_up):
            piece_up_rook = piece_up_rook.append(piece_to_validate_up)
            piece_to_validate_up = Board.pieces[[piece_to_validate_up[0]][piece_to_validate_up[1] + 1]]
            if piece_to_validate_up is not None and self.colorPiece is not Piece.ColorPiece:
                piece_up_rook = piece_up_rook.append(piece_to_validate_up)
                break
            elif piece_to_validate_up is not None and self.colorPiece is Piece.ColorPiece:
                break
            else:
                continue
        return piece_up_rook

        piece_to_validate_down = [Board.pieces[[self.location[0]][self.location[1] - 1]]]
        piece_down_rook: List[Piece] = []

        while piece_to_validate_down is None and is_within_board(piece_to_validate_down):
            piece_down_rook = piece_down_rook.append(piece_to_validate_down)
            piece_to_validate_down = Board.pieces[[piece_to_validate_down[0]][piece_to_validate_down[1] - 1]]
            if piece_to_validate_down is not None and self.colorPiece is not Piece.ColorPiece:
                piece_down_rook = piece_down_rook.append(piece_to_validate_down)
                break
            elif piece_to_validate_down is not None and self.colorPiece is Piece.ColorPiece:
                break
            else:
                continue
        return piece_down_rook

        piece_to_validate_right = [Board.pieces[[self.location[0] + 1][self.location[1]]]]
        piece_right_rook: List[Piece] = []

        while piece_to_validate_right is None and is_within_board(piece_to_validate_right):
            piece_right_rook = piece_right_rook.append(piece_to_validate_right)
            piece_to_validate_right = Board.pieces[[piece_to_validate_right[0] + 1][piece_to_validate_right[1]]]
            if piece_to_validate_right is not None and self.colorPiece is not Piece.ColorPiece:
                piece_right_rook = piece_right_rook.append(piece_to_validate_right)
                break
            elif piece_to_validate_right is not None and self.colorPiece is Piece.ColorPiece:
                break
            else:
                continue
        return piece_right_rook

        piece_to_validate_left = [Board.pieces[[self.location[0] - 1][self.location[1]]]]
        piece_left_rook: List[Piece] = []

        while piece_to_validate_left is None and is_within_board(piece_to_validate_left):
            piece_left_rook = piece_left_rook.append(piece_to_validate_left)
            piece_to_validate_left = Board.pieces[[piece_to_validate_left[0] - 1][piece_to_validate_left[1]]]
            if piece_to_validate_left is not None and self.colorPiece is not Piece.ColorPiece:
                piece_left_rook = piece_left_rook.append(piece_to_validate_left)
                break
            elif piece_to_validate_left is not None and self.colorPiece is Piece.ColorPiece:
                break
            else:
                continue
        return piece_left_rook

        valide_move_and_capture_piece_rook = []
        valide_move_and_capture_piece_rook = valide_move_and_capture_piece_rook.append(piece_up_rook)
        valide_move_and_capture_piece_rook = valide_move_and_capture_piece_rook.append(piece_down_rook)
        valide_move_and_capture_piece_rook = valide_move_and_capture_piece_rook.append(piece_right_rook)
        valide_move_and_capture_piece_rook = valide_move_and_capture_piece_rook.append(piece_left_rook)

        valide_move_and_capture_location_rook: List[(int, int)] = map(lambda piece: piece.location, valide_move_and_capture_piece_rook)

        return valide_move_and_capture_location_rook

    def bishop_valid_moves(self, Board,) -> List[int]:

        piece_to_validate_up_right = [Board.pieces[[self.location[0] + 1][self.location[1] + 1]]]
        piece_up_right_bishop: List[Piece] = []

        while piece_to_validate_up_right is None and is_within_board(piece_to_validate_up_right):
            piece_up_right_bishop = piece_up_right_bishop.append(piece_to_validate_up_right)
            piece_to_validate_up_right = Board.pieces[[piece_to_validate_up_right[0] + 1][piece_to_validate_up_right[1] + 1]]
            if piece_to_validate_up_right is not None and self.colorPiece is not Piece.ColorPiece:
                piece_up_right_bishop = piece_up_right_bishop.append(piece_to_validate_up_right)
                break
            elif piece_to_validate_up_right is not None and self.colorPiece is Piece.ColorPiece:
                break
            else:
                continue
        return piece_up_right_bishop

        piece_to_validate_up_left = [Board.pieces[[self.location[0] - 1][self.location[1] + 1]]]
        piece_up_left_bishop: List[Piece] = []

        while piece_to_validate_up_left is None and is_within_board(piece_to_validate_up_left):
            piece_up_left_bishop = piece_up_left_bishop.append(piece_to_validate_up_left)
            piece_to_validate_up_left = Board.pieces[[piece_to_validate_up_left[0] - 1][piece_to_validate_up_left[1] + 1]]
            if piece_to_validate_up_left is not None and self.colorPiece is not Piece.ColorPiece:
                piece_up_left_bishop = piece_up_left_bishop.append(piece_to_validate_up_left)
                break
            elif piece_to_validate_up_left is not None and self.colorPiece is Piece.ColorPiece:
                break
            else:
                continue
        return piece_up_left_bishop

        piece_to_validate_down_left = [Board.pieces[[self.location[0] - 1][self.location[1] - 1]]]
        piece_down_left_bishop: List[Piece] = []

        while piece_to_validate_down_left is None and is_within_board(piece_to_validate_down_left):
            piece_down_left_bishop = piece_down_left_bishop.append(piece_to_validate_down_left)
            piece_to_validate_down_left = Board.pieces[[piece_to_validate_down_left[0] - 1][piece_to_validate_down_left[1] - 1]]
            if piece_to_validate_down_left is not None and self.colorPiece is not Piece.ColorPiece:
                piece_down_left_bishop = piece_down_left_bishop.append(piece_to_validate_down_left)
                break
            elif piece_to_validate_down_left is not None and self.colorPiece is Piece.ColorPiece:
                break
            else:
                continue

        return piece_down_left_bishop

        piece_to_validate_down_right = [Board.pieces[[self.location[0] + 1][self.location[1] - 1]]]
        piece_down_right_bishop: List[Piece] = []

        while piece_to_validate_down_right is None and is_within_board(piece_to_validate_down_right):
            piece_down_right_bishop = piece_down_right_bishop.append(piece_to_validate_down_right)
            piece_to_validate_down_right = Board.pieces[[piece_to_validate_down_right[0] - 1][piece_to_validate_down_right[1] - 1]]
            if piece_to_validate_down_right is not None and self.colorPiece is not Piece.ColorPiece:
                piece_down_right_bishop = piece_down_right_bishop.append(piece_to_validate_down_right)
                break
            elif piece_to_validate_down_right is not None and self.colorPiece is Piece.ColorPiece:
                break
            else:
                continue
        return piece_down_right_bishop

        valide_move_and_capture_piece_bishop: List[Piece] = []
        valide_move_and_capture_piece_bishop = valide_move_and_capture_piece_bishop.append(piece_up_right_bishop)
        valide_move_and_capture_piece_bishop = valide_move_and_capture_piece_bishop.append(piece_up_left_bishop)
        valide_move_and_capture_piece_bishop = valide_move_and_capture_piece_bishop.append(piece_down_left_bishop)
        valide_move_and_capture_piece_bishop = valide_move_and_capture_piece_bishop.append(piece_down_right_bishop)

        valide_move_and_capture_location_bishop: List[(int, int)] = map(lambda piece: piece.location, valide_move_and_capture_piece_bishop)

        return valide_move_and_capture_location_bishop

    def queen_valid_moves(self, Board) -> List[int]:
        valid_moves_queen = bishop_valid_moves(Board)
        valid_moves_queen = valid_moves_queen.append(rook_valid_moves(Board))
        return valid_moves_queen

    def knight_valid_moves(self, Board) -> List[int]:
        x = [self.location[0]]
        y = [self.location[1]]
        pieces_to_validate = Board.pieces[list(product([x - 1, x + 1], [y - 2, x - 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))]
        valide_move_piece_knight = []
        valide_capture_piece_knight = []
        for piece in pieces_to_validate:
            if is_within_board(piece):
                if piece is None:
                    valide_move_piece_knight = valide_move_piece_knight.append(piece)
                elif piece is not None and self.colorPiece is not piece.ColorPiece:
                    valide_capture_piece_knight = valide_capture_piece_knight.append(piece)
                else:
                    continue
        
        valide_move_and_capture_piece_knight: List[Piece] = []
        valide_move_and_capture_piece_knight = valide_move_and_capture_piece_knight.append(valide_move_piece_knight)
        valide_move_and_capture_piece_knight = valide_move_and_capture_piece_knight.append(valide_capture_piece_knight)

        valide_move_and_capture_location_knight: List[int, int] = map(lambda piece: piece.location, valide_move_and_capture_piece_knight)
        return valide_move_and_capture_location_knight

    def king_valid_moves(self, Board, piece) -> List[int]:
        x = self.location[0]
        y = self.location[1]
        piece_to_validate = Board.pieces[
            [x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1],
             [x + 1, y + 1], [x - 1, y + 1], [x + 1, y - 1], [x - 1, y + 1]
             ]
        valide_move_piece_king: List[Piece] = []
        for piece in piece_to_validate:
            if is_within_board(piece):
                if piece is None:
                    valide_move_piece_king = valide_move_piece_king.append(piece)
                elif piece is not None and self.colorPiece is not piece.ColorPiece:
                    valide_move_piece_king = valide_move_piece_king.append(piece)
                else:
                    continue
            else:
                continue
        valide_moves_location_king = map(lambda piece: piece.location, valide_move_piece_king)
        return valide_moves_location_king
            

@dataclass
class Board:
    pieces: List[List[Optional[Piece]]]

    def printPiecesOnBoard(typePiece, colorPiece):
        if TypePiece is typePiece.PAWN:
            if ColorPiece is colorPiece.WHITE:
                print('WP')
            else:
                print('BP')
        elif TypePiece is typePiece.ROOK:
            if ColorPiece is colorPiece.WHITE:
                Print('WR')
            else:
                print('BR')
        elif TypePiece is typePiece.BISHOP:
            if ColorPiece is colorPiece.WHITE:
                Print('WB')
            else:
                print('BB')
        elif TypePiece is typePiece.KNIGHT:
            if ColorPiece is colorPiece.WHITE:
                Print('WK')
            else:
                print('BK')
        elif TypePiece is typePiece.QUEEN:
            if DolorPiece is colorPiece.WHITE:
                Print('WQ')
            else:
                print('BQ')
        elif TypePiece is typePiece.KING:
            if ColorPiece is colorPiece.WHITE:
                Print('WK')
            else:
                print('BK')

    def printboard(self):
        for i in range(0, len(self.pieces)):
            for j in range(0, len(self.pieces[i])):
                piece = self.pieces[i][j]
                if piece is not None:
                    printPiecesOnBoard(piece.typePiece, piece.ColorPiece)
                else:
                    print(' ')

