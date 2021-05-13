from os.path import expanduser
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iterarion =st.empty()
bar =st.progress(0)

for i in range(100):
    latest_iterarion.text(f'Iterarion {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!!!'
left_colunm,right_column = st.beta_columns(2)

button = left_colunm.button('右カラムに文字を表示')
if button:
    right_column.write("ここは右カラムです")


expander1 = st.beta_expander("問い合わせ1")
expander1.write('問い合わせを書く')
expander2 = st.beta_expander("問い合わせ2")
expander2.write('問い合わせを書く')
expander3 = st.beta_expander("問い合わせ3")
expander3.write('問い合わせを書く')
#text =st.text_input('あなたの趣味を教えてください')
#'あなたの趣味:',text

#condition = st.slider('あなたの今の調子は？', 0, 100,50)
#'コンディション:', condition

#if st.checkbox('Show Image'):
#    img = Image.open('sample.png')
#    st.image(img,caption='Hideaki Nakano', use_column_width=True)
#df= pd.DataFrame(
#    np.random.rand(100,2)/[50,50]+[35.69,139.70],
#    columns=['lat','lon']
#)
#st.table(df.style.highlight_max(axis=0))

#st.map(df)
