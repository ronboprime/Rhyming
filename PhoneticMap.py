import pronouncing as pn
import os 
import json
import WordsIn
import PhonesIn
import random


W=WordsIn.Words()
P=PhonesIn.Phones()

class phonometer:
   """reads the files from wordsin and phonesin"""
   def __init__(self, debug):
      self.debug=debug
      self.words=W.getWords(minnel=8,limit=5)
      self.phones=P.getPhones()
      self.DT=str(os.getenv('USERPROFILE'))+"\\Desktop\\"
      self.PDir=self.DT+"thingo\\"
      self.wordsFile=self.PDir+"words.json"
      self.phonesFile=self.PDir+"phones.json"
      self.compFile=self.PDir+"comped.json"
      self.KnownWords=self.PDir+"known_words.json"
      self.UnknownWords=self.PDir+"unknown_words.json"

   def syscheck(self):
      """just a systems check"""
      for i,phone in enumerate(self.phones):
         print(i,phone)

   def fones(self,x):
     """takes a single string, returns a dictionary of phonetic expressions that compose various pronunciations of the word. """
     result = pn.phones_for_word(x) 
     filtered_data = [item for item in result if item != []]
     return {x: filtered_data}

   def compilation(self,debug=False):
       """makes a file (dictionary) of all the phonetic expressions, pertaining to each word"""
       big = {}
       for word in self.words:
         f = self.fones(word)
         big.update(f)
       if debug:
          print(big)       
       with open(self.compFile,'w') as C:
          json.dump(big, C)

   def readJSON(self):
      """this prolly shoulda been a lambda"""
      with open(self.compFile,'r') as R:
         return json.load(R)


   def getKnownWords(self):
      """gets the known words, dictionary """
      with open(self.KnownWords,'r') as k:
       return json.load(k)

   def phonemes_in_words(self):
      """gets phonetic expressions for all words, returns a dictionary"""
      known_words=self.getKnownWords()
      for k,v in known_words.items():
         values=v
         cv= str(values).replace("['",'').replace("']",'').replace("'",'').split(" ")
         known_words[k]=set(cv)
      return known_words 


   def find_words_with_query(self,phones, query):
       """reverse lookup of phonetic expression, to word, generating a list of 5 random words, containing the expression"""
       words_with_query = []
       for word, phonemes in phones.items():
           if str(query).upper() in phonemes:
               words_with_query.append(word)
       return random.sample(words_with_query,5)

#P=phonometer(True)

#phones = P.phonemes_in_words()

#query = 'ae2'

#words_with_query = P.find_words_with_query(phones, query)

#print(words_with_query)
