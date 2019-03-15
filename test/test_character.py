from ..character import Character
from ..area import Area
import pytest

def test_character_exists():
    assert Character

def test_character_can_instantiate(character):
    assert isinstance(character, Character)

def test_move(character, area):
    assert area
    assert character
    assert isinstance(area, Area)
    area.animalList.append(character)
    character.move(area, 1,1)
    assert character.x == 1
    assert character.y == 1
