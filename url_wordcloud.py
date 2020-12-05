import streamlit as st
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


st.title("Word Cloud from the text in the URL")
raw_url = st.text_input("Enter URL Here")

if st.button("Draw Wordcloud"):
    page = urlopen(raw_url)
    soup = BeautifulSoup(page)
    words = ' '.join(map(lambda p:p.text,soup.find_all('p')))
    processed_words = ' '.join([word for word in words.split() if 'http' not in word and not word.startswith('@') and word != 'RT'])
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', height=640, width=800).generate(processed_words)
    plt.imshow(wordcloud)
    plt.xticks([])
    plt.yticks([])
    st.pyplot()