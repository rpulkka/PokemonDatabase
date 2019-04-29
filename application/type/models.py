import enum
from sqlalchemy import Integer, Enum

class Type(enum.Enum):
    Empty = 1
    Bug = 2
    Dark = 3
    Dragon = 4
    Electric = 5
    Fairy = 6
    Fighting = 7
    Fire = 8
    Flying = 9
    Ghost = 10
    Grass = 11
    Ground = 12
    Ice = 13
    Normal = 14
    Poison = 15
    Psychic = 16
    Rock = 17
    Steel = 18
    Water = 19