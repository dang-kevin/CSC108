"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    return puzzle == view

def game_over(puzzle: str, view: str, selection: str) -> bool:
    """Return True if and only if puzzle is the same as view or the current
    selection is QUIT.
    
    >>> game_over('banana', 'banana', 'QUIT')
    True
    >>> game_over('apple', 'a^^le', 'QUIT')
    True
    >>> game_over('banana', 'banana', 'VOWEL')
    True
    >>> game_over('apple', 'a^^le', 'SOLVE')
    False
    """
    if puzzle == view:
        return True
    elif selection == QUIT:
        return True
    else:
        return False
    
def bonus_letter(puzzle: str, view: str, letter: str) -> bool:
    """Return True if and only if the letter appears in the puzzle but not in
    its view.
    
    >>> bonus_letter('apple', 'a^^le', 'p')
    True
    >>> bonus_letter('apple', 'a^^le', 'a')
    False
    >>> bonus_letter('banana', 'banana', 'n')
    False
    """
    return letter in puzzle and letter not in view       
    
    
def update_letter_view(puzzle: str, view: str, index: int, letter: str) -> str:
    """Return a single character string representing the next view of the
    character at the given index. If letter at that index of the puzzle
    matches its guess, then return letter. Otherwise, return the
    character at that index of the view.
    
    >>> update_letter_view('apple', 'a^^le', 2, 'p')
    'p'
    >>> update_letter_view('apple', 'a^^le', 2, 'b')
    '^'
    >>> update_letter_view('apple', 'a^^le', 0, 'c')
    'a'
    """
    if letter == puzzle[index]:
        return letter
    else:
        return view[index]
    
def calculate_score(score: int, occurrence: int, letter: str) -> int:
    """Return the new score by adding CONSONANT_POINTS per occurrence of the
    letter to the current score if the letter is a consonant, or by deducting
    the VOWEL_PRICE from the score if the letter is a vowel.
    
    Precondition: score >= 0
    
    >>> calculate_score(0, 1, 'b')
    1
    >>> calculate_score(3, 1, 'a')
    2
    >>> calculate_score(3, 2, 'c')
    5
    >>> calculate_score(1, 2, 'e')
    0
    """
    if letter == VOWEL:
        return score - VOWEL_PRICE
    else:
        return score + occurrence * CONSONANT_POINTS
    
def next_player(player: str, occurrences: int) -> str:
    """If and only if the number of occurrences is greater than zero, the
    current player plays again. Return the next player.
    
    Precondition: occurences >= 0
    
    >>> next_player(PLAYER_ONE, 1)
    PLAYER_ONE
    >>> next_player('PLAYER_ONE', 0)
    PLAYER_TWO
    >>> next_player('PLAYER_TWO', 0)
    PLAYER_ONE
    >>> next_player('PLAYER_TWO', 1)
    PLAYER_TWO
    """
    if occurrences > 0:
        return player
    elif occurrences == 0 and player == PLAYER_ONE:
        return PLAYER_TWO
    elif occurrences == 0 and player == PLAYER_TWO:
        return PLAYER_ONE
    