#! python3

import webbrowser
import os
from collections import Counter
import re
import json

with open('str.txt') as input_file:
    book=input_file.read()

words = re.split('\W+', book)

l_words = Counter(words).most_common(20000)
with open('out.txt', 'wt') as output_file:
    for word_num in l_words:
        if word_num[1] > 5 and (not word_num[0].istitle()) and len(word_num[0]) > 2:
            print(word_num[0], word_num[1], file=output_file)
