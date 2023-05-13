import pytest

from garlandtools.client import Client
from garlandtools.models.records.factory import partial_factory, record_factory
from garlandtools.models.records.item import Item
from garlandtools.models.type import Type


@pytest.fixture()
def partial_data() -> dict:
    return {
        "type": Type.ITEM.value,
        "obj": {
            "i": 123,
            "n": "Test Item",
            "l": 50,
            "c": 456,
            "t": 789,
            "p": 100,
        },
    }


@pytest.fixture
def record_data_item(partial_data) -> dict:
    return {
        "item": {
            "name": "Cotton Boll",
            "description": "The fibrous flower of the cotton plant. Grown in abundance in the Black Shroud for Gridania's textile industry.",  # noqa: E501
            "id": 5343,
            "patch": 1.0,
            "patchCategory": 5,
            "price": 10,
            "ilvl": 12,
            "category": 51,
            "tradeable": 1,
            "sell_price": 1,
            "rarity": 1,
            "stackSize": 999,
            "icon": 21652,
            "nodes": [21],
        },
        "partials": [partial_data],
    }


@pytest.fixture()
def client():
    return Client()


def test_partial_factory_item(partial_data: dict, client: Client):
    result = partial_factory(partial_data, client)

    assert isinstance(result, Item)
    assert result.id == 123
    assert result.name == "Test Item"
    assert result.icon == 456
    assert result.ilvl == 50
    assert result.category == 789
    assert result.price == 100


def test_partial_factory_unknown_type(client: Client):
    partial_data = {"type": "unknown", "obj": {}}

    with pytest.raises(ValueError):
        partial_factory(partial_data, client)


def test_record_factory_item(client: Client, record_data_item, partial_data):
    record_type = Type.ITEM

    result = record_factory(record_type, record_data_item, client)

    assert isinstance(result, Item)
    assert result.id == record_data_item["item"]["id"]
    assert result.name == record_data_item["item"]["name"]
    assert result.icon == record_data_item["item"]["icon"]
    assert result.ilvl == record_data_item["item"]["ilvl"]
    assert result.category == record_data_item["item"]["category"]
    assert result.price == record_data_item["item"]["price"]
    assert len(result.related_records) == 1
    assert isinstance(result.related_records[0], Item)
    assert result.related_records[0].id == partial_data["obj"]["i"]
    assert result.related_records[0].name == partial_data["obj"]["n"]
    assert result.related_records[0].icon == partial_data["obj"]["c"]
    assert result.related_records[0].ilvl == partial_data["obj"]["l"]
    assert result.related_records[0].category == partial_data["obj"]["t"]
    assert result.related_records[0].price == partial_data["obj"]["p"]
