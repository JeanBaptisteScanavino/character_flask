from uuid import uuid4
import pytest

from .utils import is_valid_uuid

def test_is_valid_uuid_true():
    test_uuid = uuid4()
    assert is_valid_uuid(test_uuid)

def test_is_valid_uuid_false():
    false_uuid = "NOP"
    assert not is_valid_uuid(false_uuid)