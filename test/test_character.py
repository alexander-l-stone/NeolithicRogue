from ..character import Character
from ..area import Area
import pytest

@pytest.fixture
def character():
    return Character('@', (200,200,200), 0, 0, 'test', visionBlock=False, moveBlock=False, bgcolor=None)

@pytest.fixture
def area():
    return Area(0,0, 50, 50, 'test', 'test', (0,0,0))

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
