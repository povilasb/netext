from dataclasses import dataclass
from typing import Tuple

from rich.segment import Segment


@dataclass
class Spacer:
    width: int

    @property
    def cell_length(self) -> int:
        return self.width

    def split_cells(self, at: int) -> Tuple["Spacer", "Spacer"]:
        at = min(max(0, at), self.width)
        return Spacer(at), Spacer(self.width - at)


@dataclass
class OffsetLine:
    segments: list[Segment | Spacer]

    x_offset: int  # Offset from left x
    y_offset: int  # Offset from top y

    def __lt__(self, value):
        if isinstance(value, OffsetLine):
            return self.x_offset < value.x_offset and self.y_offset == self.y_offset
        return False


@dataclass
class SegmentBuffer:
    segment_lines: list[OffsetLine]
    z_index: float

    @property
    def left_x(self):
        return NotImplemented

    @property
    def right_x(self):
        return NotImplemented

    @property
    def top_y(self):
        return NotImplemented

    @property
    def bottom_y(self):
        return NotImplemented

    @property
    def width(self):
        return NotImplemented

    @property
    def height(self):
        return NotImplemented

    def __lt__(self, value):
        if isinstance(value, SegmentBuffer):
            return self.left_x < value.left_x
        return False
