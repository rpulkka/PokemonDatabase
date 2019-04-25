import enum
from sqlalchemy import Integer, Enum

class Type(enum.Enum):
    bug = 1
    dark = 2
    dragon = 3
    electric = 4
    fairy = 5
    fighting = 6
    fire = 7
    flying = 8
    ghost = 9
    grass = 10
    ground = 11
    ice = 12
    normal = 13
    poison = 14
    psychic = 15
    rock = 16
    steel = 17
    water = 18
    none = 19