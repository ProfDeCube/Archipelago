from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import ItemSenderWorld

def create_rules(world: "ItemSenderWorld"):
    world.multiworld.get_region("Menu", world.player).add_exits(['Locations'])
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Winner", world.player)
