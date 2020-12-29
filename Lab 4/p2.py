#python_version == '3.7'

import functools 

def low_freq_word_count(x, str, n, m):
    newx = list(filter(lambda i: len(i) > n, x))
    time_of_occurance = []
    for check in newx:
        if check.count(str) < m:
            time_of_occurance.append(check.count(str))
    time_of_occurance = list(time_of_occurance)
    word_freq = functools.reduce(lambda a, b: a + b, time_of_occurance)
    return word_freq
    