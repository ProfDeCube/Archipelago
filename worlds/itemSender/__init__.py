from typing import List

from BaseClasses import Region, Tutorial, ItemClassification
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from .items import ItemSenderItem, item_data_table, item_table
from .locations import ItemSenderLocation, location_data_table, get_location_table
from .options import ItemSenderOptions
from .regions import region_data_table
from .rules import create_rules



class ItemSenderWebWorld(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing ItemSender.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["ProfDeCube"]
    )

    tutorials = [setup_en]


class ItemSenderWorld(World):
    """A testing utility for easily sending items."""

    game = "ItemSender"
    web = ItemSenderWebWorld()
    options: ItemSenderOptions
    options_dataclass = ItemSenderOptions
    location_name_to_id = get_location_table()
    item_name_to_id = item_table
    starting_items = []

    def fill_slot_data(self):
            """
            make slot data, which consists of options, and some other variables.
            """
            item_sender_options = self.options.as_dict(
                "item_count",
            )
            return {
                **item_sender_options,
                "world_version": "0.1.0",
            }
            
    def create_item(self, name: str) -> ItemSenderItem:
        return ItemSenderItem(name, item_data_table[name].type, item_data_table[name].code, player=self.player)

    def create_items(self) -> None:
        self.starting_items = []
        item_pool: List[ItemSenderItem] = []
      
        for key, item in item_data_table.items():
            if item.code and item.can_create(self):
                for i in range(item.count(self)):
                    item_pool.append(self.create_item(key))
        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:

        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, ItemSenderLocation)
            if(region_name == 'Locations'):
                for i in range(self.options.item_count):
                    name = "Location " + str(i + 1)
                    region.add_locations({name: 1001 + i})

        # Change the victory location to an event and place the Victory item there.
        victory_location_name = f"Location {self.options.item_count}"
        self.get_location(victory_location_name).place_locked_item(
            ItemSenderItem("Winner", ItemClassification.progression, 10, self.player)
        )

    def set_rules(self):
        create_rules(self)

    def get_filler_item_name(self) -> str:
        return "Item"
