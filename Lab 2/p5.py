#python_version == '3.7'
import string

def count_alphabet(csentence):
    count = 0
    for x in csentence:
        if (x.isalpha() == True):
            count += 1
    return count

def vowel_capitalization(vsentence):
    vsentence = vsentence.replace('a','A')
    vsentence = vsentence.replace('e','E')
    vsentence = vsentence.replace('i','I')
    return vsentence

def concat(origin, new):
    return origin + new

def search(ssentence, target):
    check = ssentence.count(target)
    if (check == 0):
        return -1
    else:
        flag = True
        startpos = 0
        index = ssentence.find(target)
        while flag == True:            
            temp = ssentence.find(target, startpos, -1)
            if (temp >= index):
                index = temp
                startpos = temp + 1
            else:
                flag = False
        return index

def letter_count(lsentence):
    sentence = ''.join([i for i in lsentence if i.isalpha()])
    new_sentence = sentence.lower()
    all_freq = {} 
    for i in new_sentence: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    all_frequency = list(all_freq.items())
    all_frequency.sort()
    return all_frequency
