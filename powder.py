from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import colors

@dataclass
class Element(ABC):
    name: str
    color: colors.Color
    density: float = 1.0
    
    def __str__(self): return f"{self.name}"
    def __repr__(self): return self.__str__()
    
    @abstractmethod
    def update(self) -> None: ...
    
    
class Sand(Element):
    def __init__(self):
        super().__init__("Sand", colors.color_from_hex("#c2b280"), density = 0.5)
        
    def update(self): ...
    
class Void(Element):
    def __init__(self):
        super().__init__("Void", colors.BLACK)
        
    def update(self): ...
    
class Water(Element):
    def __init__(self):
        super().__init__("Water", colors.color_from_hex("#4040ff"))
        
    def update(self): ...
    

@dataclass
class Grid:
    width: int = 10
    height: int = 10
    _board: list[list[Element]] = field(default_factory = list)
    
    def __post_init__(self):
        self._board = [[Void() for x in range(self.height)] for y in range(self.width)]
        
    def __getitem__(self, row: int) -> list[Element]:
        return self._board[row]
    
    def __setitem__(self, row: int, value: list[Element]) -> None:
        self._board[row] = value 
        
    def __str__(self) -> str:
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                s += self[x][y].__str__() + " "
            s += "\n"
        return s
    
    def copy(self) -> "Grid":
        new_board = []
        for x in range(self.width):
            new_row = []
            for y in range(self.height):
                new_row.append(self[y][x])
            new_board.append(new_row)
            
        new_grid = Grid(width = self.width, height = self.height)
        new_grid._board = new_board
        return new_grid
    
    def update(self):
        for x in range(self.width):
            for y in range(self.height):
                self[y][x].update()