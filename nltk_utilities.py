

import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
Stmr = PorterStemmer()

def tokenize(X) :
  '''X -> Sentence
  For Example : ["Hi, I am a chatbot. How can I help you?"]'''
  return nltk.word_tokenize(X)

def stem(Y):
  '''Y -> Words
  Example: ["HI", "Hello", "Good", "Fine"]'''
  return Stmr.stem(Y.lower())

def bag_of_words(tkX, Y):
  '''returns array of matching words in 0's and 1's
  tkX -> ['hi', 'Hello', 'good', 'fine']
  Y -> ['Hello', 'Hi', 'Nice', 'fine', 'Good', 'good']
  bow -> [1, 0, 0, 1, 0, 1]
  '''
  XY = []
  for Y in tkX :
    stem(Y)
  bag = np.zeros(len(Y), dtype = np.float32)
  for i1, i2 in enumerate(Y) :
    if i2 in XY :
      bag[i1] = 1

  return bag