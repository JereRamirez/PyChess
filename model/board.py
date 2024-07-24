from typing import Optional
from model.piece import Piece
from model.position import Position
from model.square import Square


class Board:
    def __init__(self):
        self.squares: [[Square]] = [[None for _ in range(8)] for _ in range(8)]

    def is_position_occupied(self, position: Position) -> bool:
        return position in self.squares

    def is_move_valid(self, piece: Piece, to_position: Position) -> bool:
        if not (0 <= to_position.row < 8 and 0 <= to_position.column < 8):
            return False

        is_valid_move: bool = False
        if self.get_piece(to_position).color != piece.color:
            is_valid_move = True

        # if Knight -> check if ends in checkmate
        return is_valid_move

    def get_piece(self, position: Position) -> Optional[Piece]:
        return self.squares[position.row][position.column]