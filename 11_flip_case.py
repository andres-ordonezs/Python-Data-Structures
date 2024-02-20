def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    response = ""
    phrase = list(phrase)

    for index in range(len(phrase)):
        if phrase[index] == to_swap.upper():
            response += phrase[index].lower()

        elif phrase[index] == to_swap.lower():
            response += phrase[index].upper()

        else:
            response += phrase[index]

    return response
