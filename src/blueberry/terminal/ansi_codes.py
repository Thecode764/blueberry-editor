"""
Here you will find ansi escape sequences which are codes used to talk to the
terminal.

Each function returns the requested escape sequence in form of a string.
"""
import re


ESCAPE_REGEX = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')


def enable_alternative_screen_buffer():
    """
    Changes the terminal screen buffer to an empty one until the alternative
    screen buffer is disabled.
    """
    return '\033[?1049h'


def disable_alternative_screen_buffer():
    """
    Restores the previous screen buffer.
    """
    return '\033[?1049l'


def show_cursor():
    """
    Shows the blinking bar (the cursor).
    """
    return '\033[?25h'


def hide_cursor():
    """
    Hides the blinking bar (the cursor).
    """
    return '\033[?25l'


def move_cursor(row: int, column: int):
    """
    Moves cursor to given position.

    Args:
        row (int): row starting from 0
        column (int): column starting from 0
    """
    return f'\033[{row + 1};{column + 1}H'
