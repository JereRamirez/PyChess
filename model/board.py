from typing import Optional
from model.position import Position
from model.square import Square
from model.piece import Piece, King


class Board:
    def is_position_occupied(self, position: Position) -> bool:
        return position in self.squares

    def __init__(self):
        self.squares: [[Square]] = [[Square(Position(row, col), None) for row in range(8)] for col in range(8)]
        self.setup_board()

    def setup_board(self):
        self.set_piece(0, 4, "king", "white")
        self.set_piece(7, 5, "king", "black")

    def set_piece(self, curr_col, curr_row, piece: str, color: str):
        position = Position(curr_row, curr_col)

        if piece == "king":
            self.squares[curr_row][curr_col].set_piece(King(position, color))

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