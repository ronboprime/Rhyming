import os
import json
from pronouncing import cmudict

cmu_dict = cmudict.dict()

class Phones:
    def __init__(self, debug=False):
        self.debug = debug
        self.DT = str(os.getenv('USERPROFILE'))+"\\Desktop\\"
        self.PDir = self.DT+"thingo\\"
        self.phonesFile = self.PDir+"phones.json"

    def make_phones_file(self, debug=False):
        file = self.phonesFile
        phones = self.makePhonemes()

        with open(file, "w") as r:
            json.dump(phones, r)

    def getPhones(self, debug=False):
        # """JSON dict of phonetic expressions"""
        debug = self.debug
        try:
            with open(self.phonesFile, 'r')as w:
                phones = json.load(w)
                if debug:
                    print(type(phones))
                    print(phones)
                return phones
        except FileNotFoundError:
            self.make_phones_file()
            return self.getPhones()

    def makePhonemes(self, debug=False):
        # """Generate a set of all phonemes"""
        debug= self.debug
        all_phonemes = set()
        for phoneme_list in cmu_dict.values():
            for phonemes in phoneme_list:
                all_phonemes.update(phonemes)

        P = all_phonemes
        if debug:
            print(len(list(P)))
            print(type(P))
        keys = P
        Phones = dict.fromkeys(keys)
        return Phones
