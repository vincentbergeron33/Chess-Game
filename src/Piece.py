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
    
    #startingLocation doesnt
    def __post_init__(self):
        self.startingLocation = self.location

    def is_at_starting_location(self) -> bool:
        return self.startingLocation == self.location

    def movement(self, Board) -> List[int]:
        if self.typePiece is TypePiece.PAWN:
            valid_move_pawn = self.pawn_valid_captures(Board) + self.pawn_valid_moves(Board)
            valid_move_pawn = list(set(valid_move_pawn))
            return valid_move_pawn
        elif self.typePiece is TypePiece.ROOK:
            return self.rook_valid_moves(Board)
        elif self.typePiece is TypePiece.BISHOP:
            return self.bishop_valid_moves(Board)
        elif self.typePiece is TypePiece.QUEEN:
            return self.bishop_valid_moves(Board) + self.rook_valid_moves(Board)
        elif self.typePiece is TypePiece.KNIGHT:
            return self.knight_valid_moves(Board)
        elif self.typePiece is TypePiece.KING:
            return self.king_valid_moves(Board)
        else:
            raise NotImplementedError()

    def is_within_board(self, location) -> bool:
        if 0 <= location[0][0] <= 7 and 0 <= location[0][1] <= 7:
            return True
        else:
            return False

    def pawn_can_move_two(self, Board):
        if self.colorPiece is ColorPiece.WHITE:
            if Board.pieces[self.location[0] - 1][self.location[1]] is None:
                piece_pawn_can_move_two = [(self.location[0] - 1, self.location[1])]
                if Board.pieces[self.location[0] - 2][self.location[1]] is None:
                    piece_pawn_can_move_two = piece_pawn_can_move_two + ([
                        (self.location[0] - 2, self.location[1])
                        ])
            else:
                return []
        else:
            if Board.pieces[self.location[0] + 1][self.location[1]] is None:
                piece_pawn_can_move_two = [(self.location[0] + 1, self.location[1])]
                if Board.pieces[self.location[0] + 2][self.location[1]] is None:
                    piece_pawn_can_move_two = piece_pawn_can_move_two + ([
                        (self.location[0] + 2, self.location[1])
                        ])
            else:
                return []

        return piece_pawn_can_move_two

    def pawn_valid_moves(self, Board) -> List[int]:
        if self.is_at_starting_location():
            position_pawn_can_move = self.pawn_can_move_two(Board)
        elif self.colorPiece is ColorPiece.WHITE:
            if Board.pieces[self.location[0] - 1][self.location[1]] is None:
                position_pawn_can_move = [(self.location[0] - 1, self.location[1])]
        else:
            if Board.pieces[self.location[0] + 1][self.location[1]] is None:
                position_pawn_can_move = [(self.location[0] + 1, self.location[1])]

        return position_pawn_can_move      

    def pawn_valid_captures(self, Board) -> List[int]:
        positions_pawn_can_capture = []
        if self.colorPiece is ColorPiece.WHITE:
            location_one = [(self.location[0] - 1,self.location[1] + 1)]
            location_two = [(self.location[0] - 1,self.location[1] - 1)]
            if self.is_within_board(location_one):
                piece_to_validate_one = Board.pieces[self.location[0] - 1][self.location[1] + 1]
                if piece_to_validate_one is not None and self.colorPiece is not piece_to_validate_one.colorPiece:
                    positions_pawn_can_capture = location_one
            if self.is_within_board(location_two):
                piece_to_validate_one = Board.pieces[self.location[0] - 1][self.location[1] - 1]
                if piece_to_validate_one is not None and self.colorPiece is not piece_to_validate_one.colorPiece:
                    positions_pawn_can_capture = positions_pawn_can_capture + location_two
        else:
            location_one = [(self.location[0] + 1,self.location[1] + 1)]
            location_two = [(self.location[0] + 1,self.location[1] - 1)]
            if self.is_within_board(location_one):
                piece_to_validate_one = Board.pieces[self.location[0] + 1][self.location[1] + 1]
                if piece_to_validate_one is not None and self.colorPiece is not piece_to_validate_one.colorPiece:
                    positions_pawn_can_capture = location_one
            if self.is_within_board(location_two):
                piece_to_validate_one = Board.pieces[self.location[0] + 1][self.location[1] - 1]
                if piece_to_validate_one is not None and self.colorPiece is not piece_to_validate_one.colorPiece:
                    positions_pawn_can_capture = positions_pawn_can_capture + location_two

        return positions_pawn_can_capture

    def rook_valid_moves(self, Board) -> List[int]:

        location_up = [(self.location[0] - 1,self.location[1])]
        location_up_rook: List[Piece] = []

        if self.is_within_board(location_up):
            piece_to_validate_up = Board.pieces[self.location[0] - 1][self.location[1]]
            if piece_to_validate_up is not None:
                if self.colorPiece is not piece_to_validate_up.colorPiece:
                    location_up_rook = location_up_rook + location_up
            else:
                while piece_to_validate_up is None and self.is_within_board(location_up):
                    location_up_rook = list(location_up_rook + location_up)
                    location_up = [(location_up[0][0] - 1, location_up[0][1])]
                    
                    if self.is_within_board(location_up) is False:
                        break

                    piece_to_validate_up = Board.pieces[location_up[0][0]][location_up[0][1]]

                    if piece_to_validate_up is not None:
                        if self.colorPiece is not piece_to_validate_up.colorPiece:
                            location_up_rook = location_up_rook + location_up
                        else:
                            break

        location_down = [(self.location[0] + 1,self.location[1])]
        location_down_rook: List[Piece] = []

        if self.is_within_board(location_down):
            piece_to_validate_down = Board.pieces[self.location[0] + 1][self.location[1]]
            if piece_to_validate_down is not None:
                if self.colorPiece is not piece_to_validate_down.colorPiece:
                    location_down_rook = location_down_rook + location_down
            else:
                while piece_to_validate_down is None and self.is_within_board(location_down):
                    location_down_rook = list(location_down_rook + location_down)
                    location_down = [(location_down[0][0] + 1, location_down[0][1])]
                    
                    if self.is_within_board(location_down) is False:
                        break

                    piece_to_validate_down = Board.pieces[location_down[0][0]][location_down[0][1]]

                    if piece_to_validate_down is not None:
                        if self.colorPiece is not piece_to_validate_down.colorPiece:
                            location_down_rook = location_down_rook + location_down
                        else:
                            break

        
        location_right = [(self.location[0],self.location[1] + 1)]
        location_right_rook: List[Piece] = []

        if self.is_within_board(location_right):
            piece_to_validate_right = Board.pieces[self.location[0]][self.location[1] + 1]
            if piece_to_validate_right is not None:
                if self.colorPiece is not piece_to_validate_right.colorPiece:
                    location_right_rook = location_right_rook + location_right
            else:
                while piece_to_validate_right is None and self.is_within_board(location_right):
                    location_right_rook = list(location_right_rook + location_right)
                    location_right = [(location_right[0][0], location_right[0][1] + 1)]
                    
                    if self.is_within_board(location_right) is False:
                        break

                    piece_to_validate_right = Board.pieces[location_right[0][0]][location_right[0][1]]

                    if piece_to_validate_right is not None:
                        if self.colorPiece is not piece_to_validate_right.colorPiece:
                            location_right_rook = location_right_rook + location_right
                        else:
                            break

        location_left = [(self.location[0],self.location[1] - 1)]
        location_left_rook: List[Piece] = []
        
        if self.is_within_board(location_left):
            piece_to_validate_left = Board.pieces[self.location[0]][self.location[1] - 1]
            if piece_to_validate_left is not None:
                if self.colorPiece is not piece_to_validate_left.colorPiece:
                    location_left_rook = location_left_rook + location_left
            else:
                while piece_to_validate_left is None and self.is_within_board(location_left):
                    location_left_rook = list(location_left_rook + location_left)
                    location_left = [(location_left[0][0], location_left[0][1] - 1)]
                    
                    if self.is_within_board(location_left) is False:
                        break

                    piece_to_validate_left = Board.pieces[location_left[0][0]][location_left[0][1]]

                    if piece_to_validate_left is not None:
                        if self.colorPiece is not piece_to_validate_left.colorPiece:
                            location_left_rook = location_left_rook + location_left
                        else:
                            break

        valide_move_and_capture_location_rook = location_up_rook + location_down_rook + location_right_rook + location_left_rook

        return valide_move_and_capture_location_rook


    def bishop_valid_moves(self, Board,) -> List[int]:

       
        location_up_right = [(self.location[0] - 1,self.location[1] + 1)]
        location_up_right_bishop: List[Piece] = []

        if self.is_within_board(location_up_right):
            piece_to_validate_up_right = Board.pieces[self.location[0] - 1][self.location[1] + 1]
            if piece_to_validate_up_right is not None:
                if self.colorPiece is not piece_to_validate_up_right.colorPiece:
                    location_up_right_bishop = location_up_right_bishop + location_up_right
            else:
                while piece_to_validate_up_right is None and self.is_within_board(location_up_right):
                    location_up_right_bishop = list(location_up_right_bishop + location_up_right)
                    location_up_right = [(location_up_right[0][0] - 1, location_up_right[0][1] + 1)]
                    if self.is_within_board(location_up_right) is False:
                        break

                    piece_to_validate_up_right = Board.pieces[location_up_right[0][0]][location_up_right[0][1]]

                    if piece_to_validate_up_right is not None:
                        if self.colorPiece is not piece_to_validate_up_right.colorPiece:
                            location_up_right_bishop = location_up_right_bishop + location_up_right
                        else:
                            break

        location_up_left = [(self.location[0] - 1,self.location[1] - 1)]
        location_up_left_bishop: List[Piece] = []

        if self.is_within_board(location_up_left):
            piece_to_validate_up_left = Board.pieces[self.location[0] - 1][self.location[1] - 1]
            if piece_to_validate_up_left is not None:
                if self.colorPiece is not piece_to_validate_up_left.colorPiece:
                    location_up_left_bishop = location_up_left_bishop + location_up_left
            else:
                while piece_to_validate_up_left is None and self.is_within_board(location_up_left):
                    location_up_left_bishop = list(location_up_left_bishop + location_up_left)
                    location_up_left = [(location_up_left[0][0] - 1, location_up_left[0][1] - 1)]
                    if self.is_within_board(location_up_left) is False:
                        break

                    piece_to_validate_up_left = Board.pieces[location_up_left[0][0]][location_up_left[0][1]]

                    if piece_to_validate_up_left is not None:
                        if self.colorPiece is not piece_to_validate_up_left.colorPiece:
                            location_up_left_bishop = location_up_left_bishop + location_up_left
                        else:
                            break


            
        location_down_left = [(self.location[0] + 1,self.location[1] - 1)]
        location_down_left_bishop: List[Piece] = []

        if self.is_within_board(location_down_left):
            piece_to_validate_down_left = Board.pieces[self.location[0] + 1][self.location[1] - 1]
            if piece_to_validate_down_left is not None:
                if self.colorPiece is not piece_to_validate_down_left.colorPiece:
                    location_down_left_bishop = location_down_left_bishop + location_down_left
            else:
                while piece_to_validate_down_left is None and self.is_within_board(location_down_left):
                    location_down_left_bishop = list(location_down_left_bishop + location_down_left)
                    location_down_left = [(location_down_left[0][0] + 1, location_down_left[0][1] - 1)]
                    if self.is_within_board(location_down_left) is False:
                        break

                    piece_to_validate_down_left = Board.pieces[location_down_left[0][0]][location_down_left[0][1]]

                    if piece_to_validate_down_left is not None:
                        if self.colorPiece is not piece_to_validate_down_left.colorPiece:
                            location_down_left_bishop = location_down_left_bishop + location_down_left
                        else:
                            break

        location_down_right = [(self.location[0] + 1,self.location[1] + 1)]
        location_down_right_bishop: List[Piece] = []

        if self.is_within_board(location_down_right):
            piece_to_validate_down_right = Board.pieces[self.location[0] + 1][self.location[1] + 1]
            if piece_to_validate_down_right is not None:
                if self.colorPiece is not piece_to_validate_down_right.colorPiece:
                    location_down_right_bishop = location_down_right_bishop + location_down_right
            else:
                while piece_to_validate_down_right is None and self.is_within_board(location_down_right):
                    location_down_right_bishop = list(location_down_right_bishop + location_down_right)
                    location_down_right = [(location_down_right[0][0] + 1, location_down_right[0][1] + 1)]
                    if self.is_within_board(location_down_right) is False:
                        break

                    piece_to_validate_down_right = Board.pieces[location_down_right[0][0]][location_down_right[0][1]]

                    if piece_to_validate_down_right is not None:
                        if self.colorPiece is not piece_to_validate_down_right.colorPiece:
                            location_down_right_bishop = location_down_right_bishop + location_down_right
                            break
                        else:
                            break


        valide_move_and_capture_location_bishop = location_up_right_bishop + location_up_left_bishop + location_down_left_bishop + location_down_right_bishop
  

        return valide_move_and_capture_location_bishop


    def knight_valid_moves(self, Board) -> List[int]:
        x = self.location[0]
        y = self.location[1]
        location_to_validate = list(product([x - 1, x + 1], [y - 2, x - 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
        valide_location_knight = []
        for location in location_to_validate:
            if self.is_within_board([location]):
                piece = Board.pieces[location[0]][location[1]]
                if piece is None:
                    valide_location_knight = valide_location_knight + [location]
                elif piece is not None and self.colorPiece is not piece.colorPiece:
                    valide_location_knight = valide_location_knight + [location]
                else:
                    continue

        return valide_location_knight

    def king_valid_moves(self, Board) -> List[int]:
        x = self.location[0]
        y = self.location[1]
        location_to_validate = [
             (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
             (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)
             ]
        valide_location_king: List[Location] = []
        for location in location_to_validate:
            if self.is_within_board([location]):
                if Board.pieces[location[0]][location[1]] is None:
                    valide_location_king = valide_location_king + [location]
                elif Board.pieces[location[0]][location[1]] is not None:
                    if self.colorPiece is not Board.pieces[location[0]][location[1]].colorPiece:
                        valide_location_king = valide_location_king + [location]

        return valide_location_king

    def checkmate(currentPlayer):
        if checkmate_capture() and checkmate_move():
            print(f'{currentPlayer} is checkmate!')
            return True
        else:
            print(f'{currentPlayer} is check!')

    def corresponding_keys(self, val, dictionary):
        keys = []
        for k, v in dictionary.items():
            if val in v:
                keys.append(k)
        return keys

    def dictionary_of_moves(self, board):
        dictionary_of_moves = {}
        for rows in board.pieces:
            for piece in rows:
                if piece is not None:
                    dictionary_of_moves[piece.location] = piece.movement(board)
        return dictionary_of_moves

    def list_all_moves(self, board):
        list_all_moves = []
        for rows in board.pieces:
            for piece in rows:
                if piece is not None:
                    list_all_moves = list_all_moves + piece.movement(board)
        return list_all_moves



    def checkmate_capture(self, board):

        for rows in board.pieces:
            for piece in rows:
                if piece is not None:
                    if piece.typePiece is TypePiece.KING:
                        if piece.colorPiece is ColorPiece.WHITE:
                            white_king_location = piece.location
                        else:
                            black_king_location = piece.location

        dictionary_moves = piece.dictionary_of_moves(board)
        all_moves = piece.list_all_moves(board)
        
        if white_king_location in all_moves or black_king_location in all_moves:
            print("King in check!")
            check = False
            while check is False:
                piece_to_kill_location = self.corresponding_keys(white_king_location, dictionary_moves)
                print(piece_to_kill_location)
                if len(piece_to_kill_location) > 1:
                    print('Capture Check confirmed!')
                else:
                    if piece_to_kill_location[0] in all_moves:
                        print("if piece to kill has started...")
                        king_defenders_locations = self.corresponding_keys(piece_to_kill_location, dictionary_moves)
                        checkmate_check = []
                        for defender in king_defenders_locations:
                            board_to_iterate = board
                            print("for loop has started...")
                            piece_defender = board.pieces[defender[0]][defender[1]]
                            board_to_iterate.pieces[defender[0]][defender[1]] = None
                            defender.location = (piece_to_kill_location[0], piece_to_kill_location[1])
                            board_to_iterate.pieces[piece_to_kill_location[0]][piece_to_kill_location[1]] = piece_defender
                            new_all_moves = []
                            for rows in board_to_iterate.pieces:
                                for piece in rows:
                                    if piece is not None:
                                        new_all_moves = piece.movement(board)
                                        print(new_all_moves)
                            
                            if white_king_location in new_all_moves:
                                checkmate_check = []
                            else:
                                checkmate_check = checkmate_check + [(0,0)]
                        
                        if checkmate_check:
                            Print("We now need to check if we can block it!")
                            check = True
                            break
                        else:
                            print("White player is in check only!")
                            check = False
        else:
            print("King not in check!")


@dataclass
class Board:
    pieces: List[List[Optional[Piece]]]

    def print_pieces_on_board(self, typePiece, colorPiece):
        if typePiece is typePiece.PAWN:
            if colorPiece is colorPiece.WHITE:
                print('WP', end='|')
            else:
                print('BP', end='|')
        elif typePiece is typePiece.ROOK:
            if colorPiece is colorPiece.WHITE:
                print('WR', end='|')
            else:
                print('BR', end='|')
        elif typePiece is typePiece.BISHOP:
            if colorPiece is colorPiece.WHITE:
                print('WB', end='|')
            else:
                print('BB', end='|')
        elif typePiece is typePiece.KNIGHT:
            if colorPiece is colorPiece.WHITE:
                print('WK', end='|')
            else:
                print('BK', end='|')
        elif typePiece is typePiece.QUEEN:
            if colorPiece is colorPiece.WHITE:
                print('WQ', end='|')
            else:
                print('BQ', end='|')
        elif typePiece is typePiece.KING:
            if colorPiece is colorPiece.WHITE:
                print('WK', end='|')
            else:
                print('BK', end='|')

    def printboard(self, board):
        for i in range(0, len(self.pieces)):
            print(f'\n{i}', end='|')
            for j in range(0, len(self.pieces[i])):     
                piece = board.pieces[i][j]
                if piece is not None:
                    self.print_pieces_on_board(piece.typePiece, piece.colorPiece)
                else:
                    print('  ', end='|')
    
        print('\n  ', end=' ')
        for i in range(8):
            print(i, end='  ')
        print('\n')

        



