import uuid
import pytest
import requests

from .utils import is_valid_uuid

from ..core.domain.interfaces.ICharacter import GenderEnum, OriginEnum, ICharacter
from ..core.use_case.i_create_character import CreateCharacter
from ..right.inmemory.InMemoryCharacterRepository import InMemoryCharacterRepository


def test_i_can_create_a_character_without_info():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result:ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.name == "John Doe"
    assert is_valid_uuid(result.id)
    assert result.gender == GenderEnum.NO_SELECTION
    assert result.origin == GenderEnum.NO_SELECTION

def test_i_can_create_a_character_with_infos():
    character = {
        "name": "naruto",
        "origin": OriginEnum.DWARF,
        "gender": GenderEnum.MALE,
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result:ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.name == character["name"]
    assert is_valid_uuid(result.id)
    assert result.gender == character["gender"]
    assert result.origin == character['origin']
