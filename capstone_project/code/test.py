import pytest
import numpy as np
from dataio import load_data, split_data


def test_load_data():
    data = load_data()
    assert data.shape == (544, 4)


def test_split_data1():
    data = load_data()
    d1, d2 = split_data(data)
    assert d1.shape == (272, 4)


def test_split_data2():
    data = load_data()
    d1, d2 = split_data(data)
    assert d2.shape == (272, 4)
