from dataclasses import dataclass
from typing import List, Optional

from src.Piece import Piece


@dataclass
class Board:
    pieces: List[List[Optional[Piece]]]