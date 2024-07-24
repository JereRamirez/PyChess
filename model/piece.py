from typing import List, Tuple

from model.position import Position
from model.board import Board


class Piece:
    def __init__(self, position: Position, color: str):
        self.position = position
        self.color = color

    def get_valid_moves(self, board: Board):
        raise NotImplementedError

    def move(self, to_position: Position, board: Board):
        if to_position in self.get_valid_moves(board):
            self.position = to_position
        else:
            raise ValueError(f'Position {to_position} is not valid')


class King(Piece):
    def __init__(self, position: Position, color: str):
        super().__init__(position, color)

    def get_valid_moves(self, board: Board) -> List[Position]:
        directions: List[Tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        valid_moves: list[Position] = []

        for direction in directions:
            new_row: int = self.position.row + direction[0]
            new_column: int = self.position.column + direction[1]

            if new_row == self.position.row and new_column == self.position.column:
                continue

            is_valid_move: bool = board.is_move_valid(self, Position(new_row, new_column))
            if is_valid_move:
                valid_moves.append(Position(new_row, new_column))

        return valid_moves
