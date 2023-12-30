"""
Start by creating a virtual environment/entering in
python3 -m venv virtual-environment
source virtual-environment/bin/activate
"""
import numpy
from src.check_image import get_image, get_dimensions, add_in_dict
import pytest

@pytest.fixture
@pytest.mark.parametrize("image_path", ["/Users/akankshasingla/PycharmProjects/BenfordsLaw/input/image-1.jpg"])
def image_file(image_path):
    img = get_image(image_path)
    return img


def test_check_image_existence():
    img = image_file()
    assert type(img) is numpy.ndarray


@pytest.mark.parametrize("image_path", ["/Users/akankshasingla/PycharmProjects/BenfordsLaw/input/image-1.jpg"])
def test_wrong_image_path(image_path):
    with pytest.raises(FileExistsError):
        img = get_image(image_path)


def test_check_file_type():
    img = image_file()
    assert type(img) is not numpy.ndarray


def test_verify_no_of_channels():
    img = image_file()
    h,w,c = get_dimensions(img)
    assert c == 3


def test_add_num_to_dict():
    with pytest.raises(Exception):
        add_in_dict(2, [])
