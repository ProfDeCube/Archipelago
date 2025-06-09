from dataclasses import dataclass
from Options import Choice, Range, Toggle, PerGameCommonOptions, StartInventoryPool

class WordChecks(Range):
    """How many words you have to get right to hit you goal"""
    display_name = "Word Checks"
    range_start = 1
    default = 10
    range_end = 50
    
class WordStreakChecks(Range):
    """How many words you have to get right in a row to hit you goal"""
    display_name = "Word Streak Checks"
    range_start = 1
    default = 10
    range_end = 50
    
class WinCondition(Choice):
    """How many words you have to get right in a row to hit you goal"""
    display_name = "Win Condition"
    default = 0
    option_words = 0
    option_streak = 1
    option_words_and_streak = 2
    
class StartingLetters(Range):
    """How many letters you start with"""
    display_name = "Starting Letters"
    range_start = 1
    default = 1
    range_end = 26

class StartingGuesses(Range):
    """How many guesses you start with"""
    display_name = "Starting Guesses"
    range_start = 1
    default = 1
    range_end = 6
    
class AdditionalGuesses(Range):
    """How many extra guesses are added to the item pool"""
    display_name = "Additional Guesses"
    range_start = 0
    default = 0
    range_end = 10

class StartingCooldown(Range):
    """How long (in seconds) the new round cooldown is at the start of the game"""
    display_name = "Starting Cooldown"
    range_start = 0
    default = 120
    range_end = 18000

class TimeRewardCount(Range):
    """The number of new round cooldown reduction rewards in the pool"""
    display_name = "Time Reward Count"
    range_start = 0
    default = 10
    range_end = 30

class TimeRewardSeconds(Range):
    """How many seconds each time reward decreases the new round cooldown by"""
    display_name = "Time Reward Seconds"
    range_start = 0
    default = 10
    range_end = 30

class YellowUnlocked(Toggle):
    """Whether you start with yellow tiles shown or not"""
    display_name = "Yellow Unlocked"

class UnusedLettersUnlocked(Toggle):
    """
    Whether you start with keyboard letters fading out when discovered not to be in the current word
    """
    display_name = "Unused Letters Unlocked"   

class LogicDifficulty(Choice):
    """
    How restrictive the logic for checks is
    easy: easy to get checks, guesses/vowels/yellow likely early
    normal: easier to get checks, but still restrictive in some ways
    hard: bare minimum required to achive checks
    """
    display_name = "Logic Difficulty"
    option_easy = 0
    option_normal = 1
    option_hard = 2
    default = 1
    
class PointShopChecks(Range):
    """How many items are present in the point shop"""
    display_name = "Point Shop Checks"
    range_start = 1
    default = 3
    range_end = 50
    
class PointShopCheckPrice(Range):
    """How much AP items cost in the point shop, 0 for random"""
    display_name = "Point Shop Check Price"
    range_start = 0
    default = 200
    range_end = 1000

class GreenChecks(Choice):
    """
    How checks work for green letters in words
    none: No checks for getting green letters
    best: Checks for 1-5 correct letters in a word
    composition: checks for every configuration of green letters
    complete: Best and composition combined
    """
    display_name = "Green Checks"
    option_none = 0
    option_best = 1
    option_composition = 2
    option_complete = 3
    default = 1

class YellowChecks(Choice):
    """
    How checks work for yellow letters in words
    none: No checks for getting yellow letters
    composition: checks for every configuration of yellow letters
    """
    display_name = "Yellow Checks"
    option_none = 0
    option_composition = 1
    default = 0

class LetterChecks(Choice):
    """
    Which letters do you want to unlock items for sucessfully using in a word
    none: No checks for using letters
    vowels: Checks for using vowels
    common: Checks for using vowels and common consonants
    all: Checks for using all letters
    """
    display_name = "Letter Checks"
    option_none = 0
    option_vowels = 1
    option_common = 2
    option_all = 3
    default = 2

class ShuffleTyping(Choice):
    """
    Whether typing on your physical keyboard mimics the layout of the game keyboard
    none: Typing and on screen keyboard are not shuffled
    onscreen: On screen keyboard is shuffled, typing remains unshuffled
    querty: Typing and on screen keyboard are shuffled as if using a querty keyboard
    azerty: Typing and on screen keyboard are shuffled as if using a azerty keyboard
    dvorak: Typing and on screen keyboard are shuffled as if using a dvorak keyboard
    """
    display_name = "Unused Letters Unlocked"
    option_none = 0
    option_onscreen = 1
    option_querty = 2
    option_azerty = 3
    option_dvorak = 4
    default = 0

class LetterBalancing(Range):
    """
    ==Not Yet Implimented==
    New letter usefulness, 0 = completely random, 5 = weighted to useful letters early
    """
    display_name = "Letter Balancing"
    range_start = 0
    default = 2
    range_end = 5

class ExtraTimeRewardPercent(Range):
    """
    What percentage of filler items will be replaced with an extra cooldown reduction
    """
    display_name = "Extra Time Reward Percent"
    range_start = 0
    range_end = 100
    default = 0
    
class ClueItemRewardPercent(Range):
    """
    What percentage of filler items will be replaced with Clue Points
    """
    display_name = "Clue Item Reward Percent"
    range_start = 0
    range_end = 100
    default = 0
    
class ClueItemPointSize(Range):
    """
    How many Clue Points are awarded with Clue Point filler items
    """
    display_name = "Clue Item Point Size"
    range_start = 0
    range_end = 1000
    default = 100
    
class ClueItemDefaultFiller(Toggle):
    """
    Whether the default filler item is point shop points, Suggestions if not
    """
    display_name = "Points as Default Filler"
   
class BadGuessTrapPercent(Range):
    """
    What percentage of filler items will be replaced with Bad Guess traps
    """
    display_name = "Bad Guess Trap Reward Percent"
    range_start = 0
    range_end = 100
    default = 0
    
class RandomGuessTrapPercent(Range):
    """
    What percentage of filler items will be replaced with Random Guess traps
    """
    display_name = "Random Guess Trap Reward Percent"
    range_start = 0
    range_end = 100
    default = 0
    
class ExtraCooldownTrapPercent(Range):
    """
    What percentage of filler items will be replaced with Extra Cooldown traps
    """
    display_name = "Extra Cooldown Trap Percent"
    range_start = 0
    range_end = 100
    default = 0
    
class ExtraCooldownTrapSize(Range):
    """
    How many second are added with the extra cooldown traps
    """
    display_name = "Extra Cooldown Trap Size"
    range_start = 0
    range_end = 300
    default = 0

@dataclass
class WordipelagoOptions(PerGameCommonOptions):
    # Game Conditions
    starting_letters: StartingLetters
    starting_guesses: StartingGuesses
    additional_guesses: AdditionalGuesses
    starting_cooldown: StartingCooldown
    yellow_unlocked: YellowUnlocked
    unused_letters_unlocked: UnusedLettersUnlocked
    shuffle_typing: ShuffleTyping
    
    logic_difficulty: LogicDifficulty
    
    # Win Conditions
    word_checks: WordChecks
    word_streak_checks: WordStreakChecks
    win_condition: WinCondition
    
    # Non Goal Checks
    point_shop_checks: PointShopChecks
    point_shop_check_price: PointShopCheckPrice
    green_checks: GreenChecks
    yellow_checks: YellowChecks
    letter_checks: LetterChecks
    
    # Items
    time_reward_count: TimeRewardCount
    time_reward_seconds: TimeRewardSeconds
    extra_time_reward_percent: ExtraTimeRewardPercent
    clue_item_reward_percent: ClueItemRewardPercent
    clue_item_point_size: ClueItemPointSize
    clue_item_default_filler: ClueItemDefaultFiller
    
    #Traps
    bad_guess_trap_percent: BadGuessTrapPercent
    random_guess_trap_percent: RandomGuessTrapPercent
    extra_cooldown_trap_percent: ExtraCooldownTrapPercent
    extra_cooldown_trap_size: ExtraCooldownTrapSize

    start_inventory_from_pool: StartInventoryPool
