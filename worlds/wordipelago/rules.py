from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule
from .logicrules import letter_scores, rule_logic

if TYPE_CHECKING:
    from . import WordipelagoWorld

def all_needed_locations_checked(state, world):
    # for loc in state.locations_checked:
    #     if loc.address == 1000 + world.options.words_to_win:
    #         return True
    # return False
    return state.has("Word Master", world.player)

alpahbet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def needed_for_words(state, player, vowels, score, guesses = 1, yellow = False):
    possible_score = 0
    vowels_items = ["Letter A", "Letter E", "Letter I", "Letter O", "Letter U", "Letter Y"]
    for key in alpahbet:
        if(state.has("Letter " + key, player)):
            possible_score += letter_scores["Letter " + key]

    return state.has_from_list_unique(vowels_items, player, vowels) and possible_score >= score and (not yellow or state.has('Yellow Letters', player)) and state.has('Guess', player, guesses)

def create_rules(world: "WordipelagoWorld"):
    multiworld = world.multiworld
    player = world.player

    multiworld.get_region("Menu", player).add_exits(['Letters'])
    multiworld.get_region("Letters", player).add_exits(
        [ "Word Best", "Green Checks", "Yellow Checks"]
    )
    
    multiworld.get_region("Green Checks", player).add_exits(
        ['Green Checks 1'],
        {"Green Checks 1": lambda state: needed_for_words(state, world.player, *(rule_logic["normal"]["green"]["1"]))}
    )
    multiworld.get_region("Green Checks 1", player).add_exits(
        ['Green Checks 2'],
        {"Green Checks 2": lambda state: needed_for_words(state, world.player, *(rule_logic["normal"]["green"]["2"]))}
    )
    multiworld.get_region("Green Checks 2", player).add_exits(
        ['Green Checks 3'],
        {"Green Checks 3": lambda state: needed_for_words(state, world.player, *(rule_logic["normal"]["green"]["3"]))}
    )
    multiworld.get_region("Green Checks 3", player).add_exits(
        ['Green Checks 4'],
        {"Green Checks 4": lambda state: needed_for_words(state, world.player, *(rule_logic["normal"]["green"]["4"]))}
    )
    multiworld.get_region("Green Checks 4", player).add_exits(
        ['Green Checks 5'],
        {"Green Checks 5": lambda state: needed_for_words(state, world.player, *(rule_logic["normal"]["green"]["5"]))}
    )
    multiworld.get_region("Green Checks 5", player).add_exits(
        ['Words']
    )

    multiworld.get_region("Yellow Checks", player).add_exits(
        ['Yellow Checks 1'],
        {"Yellow Checks 1": lambda state: needed_for_words(state, world.player, *(rule_logic["normal"]["yellow"]["1"]))}
    )
    multiworld.get_region("Yellow Checks 1", player).add_exits(
        ['Yellow Checks 2'],
        {"Yellow Checks 2": lambda state: needed_for_words(state, world.player, *(rule_logic["normal"]["yellow"]["2"]))}
    )
    multiworld.get_region("Yellow Checks 2", player).add_exits(
        ['Yellow Checks 3'],
        {"Yellow Checks 3": lambda state: needed_for_words(state, world.player, *(rule_logic["normal"]["yellow"]["3"]))}
    )
    multiworld.get_region("Yellow Checks 3", player).add_exits(
        ['Yellow Checks 4'],
        {"Yellow Checks 4": lambda state: needed_for_words(state, world.player, *(rule_logic["normal"]["yellow"]["4"]))}
    )
    multiworld.get_region("Yellow Checks 4", player).add_exits(
        ['Yellow Checks 5'],
        {"Yellow Checks 5": lambda state: needed_for_words(state, world.player, *(rule_logic["normal"]["yellow"]["5"]))}
    )
    
    letter_checks = []
    if(world.options.letter_checks >= 1):
        letter_checks = [*letter_checks, "A", "E", "I", "O", "U", "Y"]
    if(world.options.letter_checks >= 2):
        letter_checks = [*letter_checks, "B", "C", "D", "F", "G", "H", "L", "M", "N", "P", "R", "S", "T"]  
    if(world.options.letter_checks == 3):
        letter_checks = [*letter_checks, "V", "W", "X", "Z", "Q", "J", "K"]

    for key in letter_checks:
        world.get_location("Used " + key).access_rule = lambda state: state.has("Letter " + key, world.player)
        world.get_location("Used " + key).item_rule = lambda item: item.name != "Letter " + key
        rule_logic["normal"]["letters"].append("Letter " + key)

    if(world.options.yellow_checks == 1):
        # Deny yellow letters being placed behind yellow positional checks
        world.get_location("----Y").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("---Y-").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("---YY").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("--Y--").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("--Y-Y").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("--YY-").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("--YYY").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("-Y---").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("-Y--Y").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("-Y-Y-").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("-Y-YY").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("-YY--").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("-YY-Y").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("-YYY-").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("-YYYY").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("Y----").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("Y---Y").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("Y--Y-").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("Y--YY").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("Y-Y--").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("Y-Y-Y").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("Y-YY-").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("Y-YYY").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("YY---").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("YY--Y").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("YY-Y-").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("YY-YY").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("YYY--").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("YYY-Y").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("YYYY-").item_rule = lambda item: item.name != 'Yellow Letters'
        world.get_location("YYYYY").item_rule = lambda item: item.name != 'Yellow Letters'
    

    world.multiworld.completion_condition[world.player] = lambda state: all_needed_locations_checked(state, world)