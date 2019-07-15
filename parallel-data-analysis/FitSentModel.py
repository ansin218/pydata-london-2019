#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import re
import pickle

import pandas as pd
import numpy as np

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout, Embedding, SpatialDropout1D, TimeDistributed

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle


# In[3]:


N_CLASSES = 2 # 0 (negative), 4 (positive)
MAX_FEATURES = 3000


# In[4]:


clean_pattern = re.compile('[^a-zA-z0-9\s]')


# In[5]:


df = pd.read_csv('trainingandtestdata/training.1600000.processed.noemoticon.csv',
                   header=None,
                   encoding='latin-1')


# In[6]:


df.columns = ['Polarity', 'ID', 'Date', 'Q', 'User', 'Text']
df = df[['Polarity', 'Text']]


# In[7]:


df['Text'] = df.Text.str.replace(clean_pattern, '')                     .str.replace('rt', ' ')
# In case neutral tweets are there,
# they don't exist in the current file anyway
df = df[df.Polarity != 2]
df.loc[df.Polarity == 4, 'Polarity'] = 1


# In[8]:


df = shuffle(df)


# In[9]:


try:
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
except FileNotFoundError:
    print('fitting tokenizer')
    tokenizer = Tokenizer(num_words=MAX_FEATURES, split=' ')
    tokenizer.fit_on_texts(df.Text.values)


# In[10]:


X = pad_sequences(tokenizer.texts_to_sequences(df.Text.values))
Y = to_categorical(df.Polarity.values, num_classes=2)


# In[11]:


Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.25)


# In[12]:


#with open('tokenizer.pkl', 'wb') as f:
#    pickle.dump(tokenizer, f, protocol=pickle.HIGHEST_PROTOCOL)


# ##### Specify Model

# In[13]:


HIDDEN_SZ = 128
EMBEDDING_SZ = 256
XLABELS = X.shape[1]


# In[14]:


model = Sequential()
model.add(Embedding(MAX_FEATURES, EMBEDDING_SZ, input_length=XLABELS))
model.add(SpatialDropout1D(rate=0.4))
model.add(LSTM(HIDDEN_SZ, return_sequences=True))
model.add(LSTM(HIDDEN_SZ, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(N_CLASSES, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())


# ##### Fit Model

# In[15]:


BATCH_SIZE = 32
N_EPOCHS = 20


# In[ ]:


model.fit(x=Xtrain,
          y=Ytrain,
          validation_split=0.1,
          batch_size=BATCH_SIZE,
          verbose=1,
          epochs=N_EPOCHS)


# ###### Serialize Model and Dictionary

# In[ ]:


model.save('sentmodel.h5')


# In[ ]:


#model.evaluate(x=Xtrain)

