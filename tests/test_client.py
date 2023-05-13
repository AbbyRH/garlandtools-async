import asyncio

import pytest

from garlandtools.client import Client
from garlandtools.models.records.item import Item
from garlandtools.models.type import Type


@pytest.fixture()
def client():
    return Client()


async def assert_cotton_boll(item):
    assert isinstance(item, Item)
    assert item.id == 5343
    assert item.name == "Cotton Boll"
    assert item.ilvl == 12
    assert item.icon == 21652
    assert item.category == 51
    assert item.price == 10
    assert (
        await item.description
        == "The fibrous flower of the cotton plant. Grown in abundance in the Black Shroud for Gridania's textile industry."  # noqa: E501
    )
    assert await item.stack_size == 999


def test_search(client: Client):
    async def runner():
        result = await client.search("Cotton Boll", Type.ITEM, exact=True)
        assert len(result) == 1
        item = result[0]

        await assert_cotton_boll(item)

    asyncio.run(runner())


def test_get_by_id_item(client: Client):
    async def runner():
        item = await client.get_by_id(5343, Type.ITEM)
        await assert_cotton_boll(item)
        assert (
            await item.description
            == "The fibrous flower of the cotton plant. Grown in abundance in the Black Shroud for Gridania's textile industry."  # noqa: E501
        )
        assert await item.stack_size == 999

    asyncio.run(runner())
