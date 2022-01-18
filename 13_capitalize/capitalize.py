def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    phrase_list = phrase.split(" ")
    phrase_list[0] = phrase_list[0].capitalize()
    return " ".join(phrase_list)
    