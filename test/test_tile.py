from ..gameobject import Tile
import pytest

def test_tile_exists():
    assert Tile

def test_tile_instantiates(tile):
    assert isinstance(tile, Tile)