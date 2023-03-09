from dataclasses import dataclass
from typing import List, Optional

from Piece import Piece


@dataclass
class Board:
    pieces: List[List[Optional[Piece]]]

    Grid: Grid


    def printPiecesonBoard(self, piece):
        if typePiece is typePiece.PAWN:
            if colorPiece is colorPiece.WHITE:
                Print(WP)
            else:
                print(BP)
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
        elif typePiece is typePiece.KNIGHT:
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
        else:
            print(o)

    def printboard(self, piece):
        grid = []
        for i in range (0, 7):
            for i in range (0, 7):
                for location in piece.location:
                    if grid[i][j] is location:
                        grid[i][j] = printPiecesonBoard(self, self.typePiece)
                    else:
                        grid[i][j] = ' '


