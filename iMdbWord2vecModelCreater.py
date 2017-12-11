#!/usr/bin/python

# encoding=utf8
import pandas as pd
import os
from nltk.corpus import stopwords
import nltk.data
import logging
import numpy as np
from gensim.models import Word2Vec
from sklearn.ensemble import RandomForestClassifier
import sys
import subprocess
import nltk
import re
from nltk.corpus import wordnet
from nltk.corpus import stopwords

from CleanupUtility import CleanupUtility


def getCleanReviews(reviews):
    clean_reviews = []
    for review in reviews["review"]:
        clean_reviews.append( CleanupUtility.review_to_wordlist( review, remove_stopwords=True ))
    return clean_reviews


if __name__ == '__main__':

	train = pd.read_csv( os.path.join(os.path.dirname(__file__), 'data', "labeledTrainData.tsv"), header=0, 
	 delimiter="\t", quoting=3 )
	unlabeled_train = pd.read_csv( os.path.join(os.path.dirname(__file__), 'data', "unlabeledTrainData.tsv"), header=0, 
	 delimiter="\t", quoting=3 )

    # Load the punkt tokenizer
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	sentences = []  # Initialize an empty list of sentences

	print "Parsing sentences from training set"
	for review in train["review"]:
	    sentences += CleanupUtility.review_to_sentences(review, tokenizer)

	print "Parsing sentences from unlabeled set"
	for review in unlabeled_train["review"]:
	    sentences += CleanupUtility.review_to_sentences(review, tokenizer)


	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
	    level=logging.INFO)

	# Set values for various parameters
	num_features = 300    # Word vector dimensionality
	min_word_count = 40   # Minimum word count
	num_workers = 4       # Number of threads to run in parallel
	context = 10          # Context window size
	downsampling = 1e-3   # Downsample setting for frequent words

	# Initialize and train the model (this will take some time)
	print "Training Word2Vec model..."
	model = Word2Vec(sentences, workers=num_workers, \
	            size=num_features, min_count = min_word_count, \
	            window = context, sample = downsampling, seed=1)

	model.init_sims(replace=True)
 

	model_name = "imdb_reviews_based_300f_40w_10c"
	model.save(model_name)