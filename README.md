Deep Learning Playground
========================

This project uses several Deep Learning tools to analyse text and provide substitution for a given word.

## Project Structure

- Creates 3 sample models using Google Word2Vec - an efficient implementation of the continuous bag-of-words and skip-gram architectures for computing vector representations of words.
- Accept User imput
- Syntaticly Parse the user imput using Google Parsey McParseface, an English parser that is trained on SyntaxNet models.
- Using 3 models created by Word2vec provide word substitution for parsed out words from user imput with Parsey McParseface.

## Try it yourself

If you would like to run this code and play with the amazing deep learning tools mentioned above, follow the installation steps bellow. 

## Installation

This code uses Python 2. You will also need virtualEnv and Docker.

1) Set up Python 2 - You can follow these instructions depending on your OS. https://cloud.google.com/python/setup

2) Clone this repo

3) Set up virtual env to keep your pakcages contained and not runing everywhere. 

```
pip install --upgrade virtualenv
cd your-project
virtualenv --python python2 env
```

4) Activate the virtual env

For Mac:

```
source env/bin/activate
```

For Windows:

```
.\env\Scripts\activate
```

5) Install requirements.txt

```
pip install -r requirements.txt
```

6) Install docker image for SyntaxNet

```
docker pull brianlow/syntaxnet-docker
```

7) You will need to download `nltk` text data sets, including stop -- only once.  

```
nltk.download()
```

## Creating models with Word2Vec

I have already created models for you to play with, they live in `models` folder.

But if you want to create a couple from scratch. 

run 
```
python iMdbWord2vecModelCreater.py
python iMdbWord2vecModelCreater.py
```

Just change names of those models on line 69 and 37 respectively. 

Now you can start playing!

run 

```
python main.py "Put Your sentence here"
```

## Modify models

You can plan with model params in `iMdbWord2vecModelCreater.py` and in `iMdbWord2vecModelCreater.py` . 
You can also modify `main.py` to change which words you want to substitute.


## Learn about tools used here

SyntaxNet and Parsey McParseface - https://research.googleblog.com/2016/05/announcing-syntaxnet-worlds-most.html

Word2Vec - https://code.google.com/archive/p/word2vec/

gesim - https://radimrehurek.com/gensim/install.html

nltk - http://www.nltk.org/

bag-of-words model - https://en.wikipedia.org/wiki/Bag-of-words_model





