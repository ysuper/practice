import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime

st.title('Title')  # 標題
st.write("Hello World")  # 文字
st.text("Hello World")  # 文字
st.markdown("### Hello World")  # markdown型式
st.code("Hello World")  # code型式
st.image(Image.open('all_dream.jpg'), caption='嚇不倒我的!')  # 加入圖片
st.write(pd.DataFrame({'first column': [1, 2, 3], 'second column': [10, 20, 30]}))  # 加入 pandas 資料表
st.line_chart(pd.DataFrame((np.random.rand(10, 2) * 10).astype(int), columns=['a', 'b']))  # 加入折線圖
st.area_chart(pd.DataFrame((np.random.rand(10, 2) * 10).astype(int), columns=['a', 'b']))  # 加入曲域圖
st.bar_chart(pd.DataFrame((np.random.rand(10, 2) * 10).astype(int), columns=['a', 'b']))  # 加入長條圖
if st.button('Hello'):  # 加入按鈕
    st.write('World')
st.write("I'm ", st.slider('How old are you?', 0, 130, 25), 'years old')  # 加入slider
st.write('Your birthday is:', st.date_input("When's your birthday", datetime.date(2019, 7, 6)))  # 加入日期
