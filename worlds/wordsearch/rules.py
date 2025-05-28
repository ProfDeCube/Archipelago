from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule
import logging
logger = logging.getLogger("WordSearch")

if TYPE_CHECKING:
    from . import WordSearchWorld

def all_needed_locations_checked(state, world):
    return state.has("Word Master", world.player)

def word_find_rules(word_number, state, player, options):
    has_enough_words = word_number < options.starting_word_count or state.has("Word", player, word_number - options.starting_word_count)
    has_enough_loops = word_number < options.starting_loop_count or state.has("Loop", player, word_number - options.starting_loop_count)
    has_previous_word = True
    if(word_number == 1):
        has_previous_word = True
    elif(word_number == 2):
        has_previous_word = state.can_reach_location("1 Word Found", player)
    else:
        has_previous_word = state.can_reach_location(str(word_number - 1) + " Words Found" , player)
    return has_enough_words and has_enough_loops and has_previous_word

def create_rules(world: "WordSearchWorld"):
    multiworld = world.multiworld
    player = world.player
    
    multiworld.get_region("Menu", player).add_exits(["Words"])
    
    world.get_location("1 Word Found").access_rule = lambda state: word_find_rules(1, state, player, world.options)

    for i in range(world.options.total_word_count - 1):
        logger.info(f"{i} : {str(i + 2)} Words Found")
        world.get_location(str(i + 2) + " Words Found").access_rule = lambda state, word=i+2: word_find_rules(word, state, player, world.options)

    multiworld.completion_condition[player] = lambda state: all_needed_locations_checked(state, world)