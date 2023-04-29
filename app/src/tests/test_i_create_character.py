import uuid

import pytest
import requests

from ..core.domain.interfaces.ICharacter import (GenderEnum, ICharacter,
                                                 OriginEnum, WorkEnum)
from ..core.use_case.i_create_character import CreateCharacter
from ..right.inmemory.InMemoryCharacterRepository import \
    InMemoryCharacterRepository
from .utils import is_valid_uuid


def test_i_can_create_a_character_without_name():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    print(result)
    assert result.name == "John Doe"
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_with_name():
    character = {
        "name": "naruto",
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.name == character["name"]
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_without_gender():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.gender == GenderEnum.NO_SELECTION
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_with_gender():
    character = {
        "name": "naruto",
        "gender": GenderEnum.MALE,
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.gender == character["gender"]
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_without_origin():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.origin == OriginEnum.NO_SELECTION
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_with_origin():
    character = {
        "name": "naruto",
        "origin": OriginEnum.DWARF,
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.origin == character["origin"]
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_without_work():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.work == WorkEnum.NO_SELECTION
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_with_work():
    character = {
        "name": "naruto",
        "work": WorkEnum.WARRIOR,
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.work == character["work"]
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_without_level():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.level == 1
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_with_level():
    character = {
        "name": "naruto",
        "level": 4,
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.level == character["level"]
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_without_XP():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.XP == 0
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_with_XP():
    character = {
        "name": "naruto",
        "XP": 1021,
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.XP == character["XP"]
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_without_destiny_points():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.destiny_points == 0
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_with_destiny_points():
    character = {
        "name": "naruto",
        "destiny_points": 1,
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.destiny_points == character["destiny_points"]
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_without_caract():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.caract.force == 10
    assert result.caract.agility == 10
    assert result.caract.intel == 10
    assert result.caract.charisma == 10
    assert result.caract.brave == 10
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_with_caract():
    character = {
        "name": "naruto",
        "caract": {
            "force": 20,
            "intel": 13,
            "charisma": 11,
            "agility": 12,
            "brave": 15,
        },
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.caract.force == character["caract"]["force"]
    assert result.caract.agility == character["caract"]["agility"]
    assert result.caract.intel == character["caract"]["intel"]
    assert result.caract.charisma == character["caract"]["charisma"]
    assert result.caract.brave == character["caract"]["brave"]
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_without_money():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.money.gold == 0
    assert result.money.silver == 0
    assert result.money.thritil == 0
    assert result.money.berylium == 0
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_with_money():
    character = {
        "name": "naruto",
        "money": {"gold": 20, "silver": 13, "thritil": 11, "berylium": 12},
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.money.gold == character["money"]["gold"]
    assert result.money.silver == character["money"]["silver"]
    assert result.money.thritil == character["money"]["thritil"]
    assert result.money.berylium == character["money"]["berylium"]
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_without_caract_i_have_magic_resistance():
    character = {}
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.magic_resistance == 10
    assert is_valid_uuid(result.id)


def test_i_can_create_a_character_with_caract_i_have_magic_resistance():
    character = {
        "name": "naruto",
        "caract": {
            "force": 14,
            "intel": 13,
            "charisma": 11,
            "agility": 12,
            "brave": 15,
        },
    }
    dependencies = {"character_repository": InMemoryCharacterRepository}
    result: ICharacter = CreateCharacter(dependencies).create_character(character)
    assert result.magic_resistance == 14
    assert is_valid_uuid(result.id)
