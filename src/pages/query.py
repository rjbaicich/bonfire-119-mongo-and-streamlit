from pathlib import Path
import streamlit as st
import sys
import os

filepath = os.path.join(Path(__file__).parents[1])

sys.path.insert(0, filepath)

from to_mongo import ToMongo

c = ToMongo()

answer = st.text_input('Enter a card name:', value = 'Sol Ring')
st.write(list(c.cards.find({'name:answer'})))