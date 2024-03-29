def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [elem for elem in lst if elem == True]
    # why does that return [1]
    # return [elem for elem in lst if bool(elem) == True]