
#!/usr/bin/env python

import re
import nltk

import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from nltk.corpus import stopwords


class CleanupUtility(object):

    @staticmethod
    def review_to_wordlist( review, remove_stopwords=False ):
        # remove HTML
        review_text = BeautifulSoup(review, "html.parser").get_text()

        # remove non-letters
        review_text = re.sub("[^a-zA-Z]"," ", review_text)
        

        words = review_text.lower().split()
        
        # remove stop words
        if remove_stopwords:
            stops = set(stopwords.words("english"))
            words = [w for w in words if not w in stops]

        return(words)


    @staticmethod
    def review_to_sentences( review, tokenizer, remove_stopwords=False ):

        # NLTK tokenizer splits the paragraph into sentences
        raw_sentences = tokenizer.tokenize(review.decode('utf8').strip())

        sentences = []
        for raw_sentence in raw_sentences:
            if len(raw_sentence) > 0:
                # get a list of words
                sentences.append( CleanupUtility.review_to_wordlist( raw_sentence, \
                  remove_stopwords ))
        #
        # Return the list of sentences (each sentence is a list of words,
        # so this returns a list of lists
        return sentences