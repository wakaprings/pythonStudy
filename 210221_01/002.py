# http://100sen.cyber-ninja.jp/
# https://qiita.com/nyax/items/fc418416e97a12141d0a

# ユニークな数の出現回数
# df.value_counts

# pip install matplotlib
# pip install japanize_matplotlib

import streamlit as st

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)