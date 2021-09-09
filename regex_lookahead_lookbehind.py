import re


def count_n_repetitions(text, n=1):
    """
    Counts how often characters are followed by themselves for
    n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    """

    hits = re.findall(
        rf"""
        (.)  # Matches any character, with DOTALL even newlines
        (?=  # Start look-ahead group
            \1{{{n}}}  # match char n-times
        )    # End look-ahead group
        """,
        text,
        flags=re.DOTALL | re.VERBOSE,
    )
    return len(hits)


def count_n_reps_or_n_chars_following(text, n=1, char=""):
    """
    Counts how often characters are repeated for n times, or
    followed by char n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    char: Character which also counts if repeated n times
    """
    # Functions could be merged together, but for easy reference, we keep them spearated
    if char == "":
        return count_n_repetitions(text, n)

    # escape chars if necessary for usage in square regex brackets
    escaped_chars = re.escape(char)

    hits = re.findall(
        rf"""
        (.)  # Matches any character, with DOTALL even newlines
        (?=  # Start look-ahead group
            (?:  # Start non-capturing group -> () around or would be capturing group again
                \1{{{n}}}  # matched char followed by repetitions
                |    # OR
                [{escaped_chars}]{{{n}}}  # followed by escaped char in square brackets n times
            )    # End non capturing group
        )    # End lookahead group
        """,
        text,
        flags=re.DOTALL | re.VERBOSE,
    )

    return len(hits)


def check_surrounding_chars(text, surrounding_chars):
    """
    Count the number of times a character is surrounded by
    characters from the surrounding_chars list.

    text: UTF-8 compliant input text
    surrounding_chars: List of characters
    """
    escaped_surround_chars = re.escape("".join(surrounding_chars))
    surround_pattern = "[" + escaped_surround_chars + "]"
    hits = re.findall(
        rf"""
        (?<=  # Start look-behind group
            {surround_pattern} # include escaped surround pattern
        )     # End look-behind group
        (.)   # match all character
        (?=  # Start look-ahead group
            {surround_pattern} # include escaped surround pattern
        )     # End look-ahead group
        """,
        text,
        flags=re.DOTALL | re.VERBOSE,
    )

    return len(hits)