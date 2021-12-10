import copy
import ftfy
import gensim
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('english')
nltk.download('stopwords')
import numpy as np
import pandas as pd
import pickle
import random
from random import choice
import seaborn as sns
import tensorflow as tf
import time
import numpy as np
import pandas as pd
from datetime import datetime, date
import requests
from bs4 import BeautifulSoup
import dateutil.parser
from google.colab import drive, files
import string
import regex as re
from ftfy import fix_text
import pattern
from pattern.en import lemma, lexeme

from tqdm import tqdm
import unidecode
import re

import xgboost as xgb

from gensim.models import KeyedVectors, Word2Vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from IPython.display import SVG, clear_output
from itertools import product

import tensorflow
from tensorflow.keras import optimizers, regularizers
from tensorflow.keras.constraints import unit_norm
from tensorflow.keras.layers import Input, Flatten, LSTM, Conv1D, Dense, TimeDistributed, GlobalMaxPooling1D, Lambda
from tensorflow.keras.models import Model, load_model, Sequential

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

import transformers
from transformers import AutoModel, AutoTokenizer, AutoConfig
from transformers import BertForMaskedLM, BertModel, BertTokenizer
from transformers import Trainer, TrainingArguments
