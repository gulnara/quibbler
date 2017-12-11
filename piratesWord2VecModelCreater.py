#!/usr/bin/python

# encoding=utf8
import os
from nltk.corpus import stopwords
import nltk.data
import logging
import numpy as np
from gensim.models import Word2Vec
from sklearn.ensemble import RandomForestClassifier
import nltk
import re
from nltk.corpus import webtext


for fileid in webtext.fileids():
	if fileid == 'pirates.txt':
		sentences = webtext.sents(fileid)
		logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
	    level=logging.INFO)

		# Set values for various parameters
		num_features = 300    # Word vector dimensionality
		min_word_count = 40   # Minimum word count
		num_workers = 4       # Number of threads to run in parallel
		context = 10          # Context window size
		downsampling = 1e-3   # Downsample setting for frequent words
		print "Training Word2Vec model..."
		model = Word2Vec(sentences, workers=num_workers, \
	            size=num_features, min_count = min_word_count, \
	            window = context, sample = downsampling, seed=1)

		model.init_sims(replace=True)
 

		model_name = "pirates_of_carribean_based_300f_40w_10c"
		model.save(model_name)
		