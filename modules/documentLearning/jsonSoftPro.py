from .jsonExtractor import *
import re
import sys
import itertools
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TweetTokenizer


from pprint import pprint


#json_data = jsonExtractor.getJson_data()

# return sectionnames within a json data
def getSectionnames(json_data):
    i=0
    for sectionsnames in json_data:

         x = sectionsnames['sections'].keys()
    else:
         i = i+1
    x = list(x)
    return x

# return namespaces within a json data
def getNamespaces(json_data):
    all = []
    i=0
    for namespaces in json_data:
         x = namespaces['title']
         all.append(x)

         i = i + 1

    tokenize = RegexpTokenizer('\w\S*(?=:)')
    s = tokenize.tokenize(str(all))
    s_clean = list(set(s))
    return s_clean

# return filename (e.g. Concept:101Worker) within the json data. Note: not used by now
def getFileName(json_data):
    all = []
    i=0
    for namespaces in json_data:
         x = namespaces['title']
         all.append(x)

         i = i + 1

    return x


