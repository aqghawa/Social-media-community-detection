#!/usr/bin/env python
# coding: utf-8

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd


df = pd.read_csv("cleaned.csv",encoding = "ISO-8859-1", index_col=0, nrows=50000)

tfidfvectorizer = TfidfVectorizer(analyzer='word' , stop_words='english')

X = tfidfvectorizer.fit_transform(df['tweet'])

kmeans = KMeans(n_clusters=50).fit(X)
kmeans.labels_

df['cluster']=kmeans.labels_


df0=df[df['cluster']==0]

df0=df0.to_csv('exp1.csv')
