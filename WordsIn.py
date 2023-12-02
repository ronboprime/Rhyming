import os 
import json
from itertools import chain
from pronouncing import cmudict
from nltk.corpus import wordnet as wn

needed=False

if needed:
    lemmas_in_wordnet = set(chain(*[ss.lemma_names() for ss in wn.all_synsets()]))

cmu_dict = cmudict.dict()

class Words:
    def __init__(self,debug=False):
        self.debug=debug
        self.DT=str(os.getenv('USERPROFILE'))+"\\Desktop\\"
        self.PDir=self.DT+"thingo\\"
        self.wordsFile=self.PDir+"words.json"
   
    def getWords(self, minnel=3, limit=2500, debug=False):
        C = 0
        debug = self.debug
        try:
            with open(self.wordsFile, 'r') as w:
                words = json.load(w)
                words = {k: v for k, v in words.items() if len(k) >= minnel
                         and k.isalpha() and not k.isupper() 
                         and "_" not in k and "-" not in k and "." not in k and "'" not in k}

                if debug:
                    for k, v in words.items():
                        C += 1
                        print(k, v)
                        if C > limit:
                            C = 0
                            break
                return words
        except FileNotFoundError:
            self.make_words_file()
            return self.getWords(minnel=minnel, limit=limit, debug=debug)

    def make_words_file(self, debug=False):
        #"""generates a dictionary of enumerated words"""
        debug=self.debug
        words={}
        lemmas=sorted(lemmas_in_wordnet)
        for i, lems in enumerate(lemmas):
            if str(lems).isalpha():
                words[lems]=str(i)
        if debug:
            print(words)
            print(type(words))
        with open(self.wordsFile,"w")as f:
            json.dump(words ,f)        
            
