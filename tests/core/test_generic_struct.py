import pytest

from transfermarkt.core.generic_struct import GenericStruct


@pytest.fixture
def payload():
    return {
        "text": "test",
        "value": 90,
        "flag": True,
        "list": [1, 2, 3, 4]
    }


@pytest.fixture
def struct(payload):
    return GenericStruct(**payload)


def test_generate_struct(struct):
    # Test struct content
    assert struct.text == "test"
    assert struct.value == 90
    assert struct.flag
    assert struct.list == [1, 2, 3, 4]


def test_struct_equality(struct, payload):
    # Test non equal objects
    assert struct != "not a struct"
    assert struct != {}

    # Test equality of the same struct
    assert struct == GenericStruct(**payload)
    # Test dictionary content
    assert struct.to_dict() == payload
