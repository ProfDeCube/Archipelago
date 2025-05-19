from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import ItemSenderWorld


class ItemSenderItem(Item):
    game = "ItemSender"


class ItemSenderItemData(NamedTuple):
    count: Callable[["ItemSenderWorld"], int] = lambda world: 1
    code: Optional[int] = None
    name: Optional[str] = None
    type: ItemClassification = ItemClassification.filler
    can_create: Callable[["ItemSenderWorld"], bool] = lambda world: True


item_data_table: Dict[str, ItemSenderItemData] = {
    "Item": ItemSenderItemData(code=1,type=ItemClassification.progression, count = lambda world: world.options.item_count - 1 ),
    "Winner": ItemSenderItemData(code=10,type=ItemClassification.progression, can_create = lambda world: False),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
