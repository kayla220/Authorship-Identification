import os, sys, getopt
import nltk
import glob
import re
from collections import defaultdict

# sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pick')
word_tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

# load data
# with open('C10/C10test/ToddNissen/303895newsML.txt', mode='r', encoding='utf-8') as sentences:
#     for sentence in sentences:
#         print(sentence)

name = []
# {Author: {filename: text}}
news = defaultdict(dict)
for filename in glob.glob('C10/C10train//**/*.txt'):
    name = re.findall('[^C10/C10train\/][^\/]+', filename)
    with open(filename, mode='r', encoding='utf-8') as sentences:
        news[name[0]].update({name[1]: sentences.read()})
# feature vectors
print(news['AlexanderSmith'])






