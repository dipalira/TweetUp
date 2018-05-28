from rake_nltk import Rake
from nltk.corpus import stopwords
import pandas as pd

from pprint import pprint
import ast
import json
r = Rake()
def get_names():
    with open("groups_05.json", 'r') as in_file:
        data = json.load(in_file)
        #for inp in in_file.readlines():
            #k = ast.literal_eval(inp)
            #pprint(k)
            #data = json.loads(inp)
        with open("titles_list.txt", 'w') as ou_f:
            for d in data:
                for a in d:
                    ou_f.write(a["name"].encode('ascii', 'ignore') + "\n")


def rake_text():

    with open("titles_list.txt", 'r') as input_file:
        lines = ""
        text = input_file.readlines()
        for line in text:
            lines = lines + line + " "
        print (lines)
        r.extract_keywords_from_text(lines)
        meetup_words = ['<p>', '<\p>', '<br>', 'group', 'join', 'meetup', 'right', 'idea', 'join', 'community', 'make',
                        'social', 'discuss', 'local', 'chapter',
                        'people', 'country', 'topic', 'human', 'justice', 'discus', 'important', '_', 'meet', 'welcome',
                        'event', 'get', 'bring', 'day', 'join', 'go']
        states = [
            'alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida',
            'georgia', 'hawaii', 'idaho', 'illinois', 'indiana'
            , 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota',
            'mississippi', 'missouri',
            'montana', 'nebraska', 'nevada', 'new', 'hampshire', 'new', 'jersey', 'new', 'mexico', 'new', 'york', 'nyc',
            'north carolina', 'north dakota', 'ohio',
            'oklahoma', 'oregon', 'pennsylvania', 'rhode', 'island', 'south', 'carolina', 'south', 'dakota', 'tennessee',
            'texas', 'utah', 'vermont', 'virginia',
            'washington', 'dc', 'west', 'Virginia', 'wisconsin', 'wyoming', 'philadelphia', 'brooklyn', 'america', 'pittsburgh']
        rake_object = Rake(stopwords.words('english') + meetup_words + states)
        rake_object.extract_keywords_from_text(lines)
        #print rake_object.get_ranked_phrases_with_scores()
        print (rake_object.extract_keywords_from_text(lines))
        print (rake_object.frequency_dist)
        #print r.get_ranked_phrases()

import string
from nltk.stem.wordnet import WordNetLemmatizer

stop_words = stopwords.words('english')
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)


if __name__ == '__main__':
    get_names()
    rake_text()
