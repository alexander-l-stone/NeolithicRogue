import pytest
from ..gameobject import GameObject

def test_gameobject_exists():
    assert GameObject

def test_gameobject_instantiates(gameobject):
    assert isinstance(gameobject, GameObject)