from typing import Optional
from model.piece import Piece
from model.position import Position


class Square:
    def __init__(self, position: Position, piece: Optional[Piece] = None):
        self.position = position
        self.piece = piece