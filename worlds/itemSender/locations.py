from typing import Callable, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from . import ItemSenderWorld


class ItemSenderLocation(Location):
    game = "ItemSender"


class ItemSenderLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["ItemSenderWorld"], bool] = lambda world: True

location_data_table = {}

def get_location_table():
    location_table = {}
    for i in range(10000):
        location_table["Location " + str(i + 1)] = 1001 + i
    return location_table
