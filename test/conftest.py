from ..character import Character
from ..area import Area
from ..gameobject import GameObject
from ..gameobject import Tile
import pytest

@pytest.fixture
def character():
    return Character('@', (200,200,200), 0, 0, 'test', visionBlock=False, moveBlock=False, bgcolor=None)

@pytest.fixture
def area():
    return Area(0,0, 50, 50, 'test', 'test', (0,0,0))

@pytest.fixture
def gameobject():
    return GameObject('#', (100,100,100), 1, 1)

@pytest.fixture
def tile():
    return Tile((50,50,50), 0, 0)