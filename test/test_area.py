from ..area import Area
import pytest

def test_area_exists():
    assert Area

def test_area_instantiates(area):
    assert isinstance(area, Area)