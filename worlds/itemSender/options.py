from dataclasses import dataclass
from Options import Range, PerGameCommonOptions, StartInventoryPool

class ItemCount(Range):
    """How Many Items/Locations you want"""
    display_name = "Words To Win"
    range_start = 1
    default = 500
    range_end = 10000

@dataclass
class ItemSenderOptions(PerGameCommonOptions):
    item_count: ItemCount
    start_inventory_from_pool: StartInventoryPool
