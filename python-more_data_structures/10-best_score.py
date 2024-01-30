#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxd = 0
    score = ''
    for value in a_dictionary:
        if a_dictionary[value] > maxd:
            maxd = a_dictionary[value]
            score = value
    return score
