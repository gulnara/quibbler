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


input_str = ""

def get_user_input():
	input = sys.argv[1]
	input_str = input
	print("Input String: " + input_str)
	return input_str

def create_dependency_tree():
	arg_list = sys.argv
	arg_list.pop(0)
	str1 = ' '.join(arg_list)
	p = subprocess.Popen("echo " + str1 + "| sudo docker run --rm -i brianlow/syntaxnet-docker", stdout=subprocess.PIPE, shell=True)
	out = p.stdout.read()
	deptree = out.splitlines()
	return deptree

#retrieve root word 
def get_root_word(dependency_tree):
	root = dependency_tree[2].split()[0]
	return root

#retrieve dependent object
def get_dependent_object(dependency_tree):
	#print "Getting dependency tree"
	for string in dependency_tree:
		if string.find("dobj") != -1:
			dobj = string.split()[1]
			return dobj

input_str = get_user_input()

dep_tree = create_dependency_tree()

print "Dependency tree:"
for d in dep_tree:
	print d

# get root
root = get_root_word(dep_tree)
print root

#get dependent object
dobj = get_dependent_object(dep_tree)
print dobj

# # small data set - Pirates of the Carribean script
# model = Word2Vec.load(os.path.join(os.path.dirname(__file__), 'models', "pirates_of_carribean_based_300f_40w_10c"))

# bigger data set - about 100,000 imdb movie reviews 
# model = Word2Vec.load(os.path.join(os.path.dirname(__file__), 'models',"imdb_reviews_based_300f_40w_10c"))

# large data set - 681,288 blog posts
model = Word2Vec.load(os.path.join(os.path.dirname(__file__), 'models',"blog_posts_300_c_40.word2vec"))

print model.most_similar(dobj)
