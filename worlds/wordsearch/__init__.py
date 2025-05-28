from typing import List

from BaseClasses import Region, Tutorial, ItemClassification
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from .items import WordSearchItem, item_data_table, item_table
from .locations import WordSearchLocation, location_data_table, get_location_table
from .options import WordSearchOptions
from .regions import region_data_table
from .rules import create_rules



class WordSearchWebWorld(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing WordSearch.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["ProfDeCube"]
    )

    tutorials = [setup_en]


class WordSearchWorld(World):
    """A brand new take on the world famous word guessing game."""

    game = "WordSearch"
    web = WordSearchWebWorld()
    options: WordSearchOptions
    options_dataclass = WordSearchOptions
    location_name_to_id = get_location_table()
    item_name_to_id = item_table
    starting_items = []

    def generate_early(self):
        location_count = self.options.total_word_count - 1
        item_count = 2 * self.options.total_word_count - (self.options.starting_word_count + self.options.starting_loop_count)
        if(location_count < item_count):
            raise OptionError('Not enough locations, increase total words or starting words/loops')

    def fill_slot_data(self):
            """
            make slot data, which consists of options, and some other variables.
            """
            word_search_options = self.options.as_dict(
                "grid_size",
                "total_word_count",
                "starting_word_count",
                "out_of_logic_words",
                "starting_loop_count",
                "diagonal_words",
                "backwards_words",
            )
            return {
                **word_search_options,
                "world_version": "0.1.0",
            }
            
    def create_item(self, name: str) -> WordSearchItem:
        return WordSearchItem(name, item_data_table[name].type, item_data_table[name].code, player=self.player)

    def create_items(self) -> None:
        item_pool: List[WordSearchItem] = []

        for key, item in item_data_table.items():
            if item.code and item.can_create(self):
                for i in range(item.count(self)):
                    item_pool.append(self.create_item(key))

        location_count = self.options.total_word_count - 1
        item_count = 2 * self.options.total_word_count - (self.options.starting_word_count + self.options.starting_loop_count)
        if(location_count > item_count):
            filler_items = location_count - item_count
            for i in range(filler_items):
                item_pool.append(self.create_filler())
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
            }, WordSearchLocation)
            
            if(region_name == 'Words'):
                first_check_name = "1 Word Found"
                region.add_locations({first_check_name: 101})
                for i in range(self.options.total_word_count - 1):
                    name =  str(i + 2) + " Words Found"
                    region.add_locations({name: 102 + i})

        # Change the victory location to an event and place the Victory item there.
        victory_location_name = f"{self.options.total_word_count} Words Found"
        self.get_location(victory_location_name).place_locked_item(
            WordSearchItem("Word Master", ItemClassification.progression, 1000, self.player)
        )

    def set_rules(self):
        create_rules(self)

    def get_filler_item_name(self) -> str:
        return "Filler"
