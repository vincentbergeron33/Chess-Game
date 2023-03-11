from dataclasses import dataclass
from typing import List, Optional

from Piece import Piece

startingLocation: (int, int) = field(init = False)

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

