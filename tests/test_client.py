import asyncio
from typing import Dict

import pytest

from garlandtools import Client
from garlandtools.models.partials.item_partial import ItemPartial
from garlandtools.models.type import Type


@pytest.fixture()
def client():
    return Client()


def test_search(client: Client):
    async def runner() -> list[Dict]:
        return await client.search("Cotton Boll", Type.ITEM, exact=True)

    result = asyncio.run(runner())

    assert len(result) == 1

    # The search function should translate into ItemPartials for us,
    # It's just not implemented yet.
    item = ItemPartial(result[0])
    assert item.id == 5343
    assert item.name == "Cotton Boll"
    assert item.ilvl == 12
    assert item.icon == 21652
    assert item.category == 51
    assert item.price == 10
