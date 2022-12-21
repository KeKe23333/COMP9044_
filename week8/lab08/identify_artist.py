#!/usr/bin/env python3
import glob
import math
import re
import sys

from torch import max_pool1d

def total_(lines):
    total = 0 

    for line in lines:
        words = re.findall(r'[a-zA-Z]+', line)

        total +=len(words)

    return total

def count_(lines, arg):
    times = 0
    find = r'\b' + arg + r'\b'

    for line in lines:
        sub_times = re.findall(find, line, flags=re.I)
        times+=len(sub_times)

    return times + 1

data = {}

for file in glob.glob("lyrics/*.txt"):
    fp = open(file, 'r')
    lines = fp.readlines()
    fp.close()
    total = total_(lines)
    counts = []
    for arg in sys.argv[1:]:
        counts.append(count_(lines, arg))
    res = 0
    for value in counts:
        log = math.log(value/total)
        res +=log 
    file_name = file.replace('lyrics/', '')
    file_name = file_name.replace('.txt', '')
    file_name = file_name.replace('_', ' ')
    
    data[file_name] = res


 
def get_all_words(song):
    fp = open(song, 'r')
    song_lines = fp.readlines()

    fp.close()

    all_words = []

    for line in song_lines:

        words = re.findall(r'[a-zA-Z]+', line, flags = re.I)
        all_words+=words
    return all_words



##################################################
# 1.get all word
total_words_dict = {}
lines_dict = {}

for file in glob.glob('lyrics/*.txt'):
    fp =  open(file, 'r')
    lines = fp.readlines()
    fp.close()
    file_name = file.replace('lyrics/', '')
    total = total_(lines)
    total_words_dict[file_name] = total # value
    lines_dict[file_name] = lines # list


# 2. #######################
fre_word_dict = {}

for file in glob.glob('lyrics/*.txt'):
    file_name = file.replace('lyrics/', '')
    fre_word_dict[file_name] = {}


# 3. compute the song probabliy in each lyrics
def count_probablity(all_words, file):
    res = 0
    for word in all_words:
        total = total_words_dict[file]
        file_dict = fre_word_dict[file]

        word = word.lower()

        if word not in file_dict.keys():
            lines = lines_dict[file]
            file_dict[word] = count_(lines, word)

        log = math.log(file_dict[word]/total)
        res +=log
        #update
        fre_word_dict[file] = file_dict
    return res

for song in sys.argv[1:]:

    all_words = get_all_words(song)
    max_log = -math.inf
    max_file = ''
    for file in glob.glob('lyrics/*.txt'):
        name = file.replace('lyrics/', '')
        prob = count_probablity(all_words, name)

        if prob > max_log:
            max_log = round(prob, 1)
            max_file = name 
    max_file = max_file.replace('.txt', '')
    max_file = max_file.replace('_', ' ')

    print(f'{song} most resembles the work of {max_file} (log-probability={max_log})')
