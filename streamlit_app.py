import streamlit

streamlit.title('My Parents Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Banana')
streamlit.text('🥗Smoothie')
streamlit.text('🐔Eggs')   
streamlit.text('🥑Avo on Toast 🍞')  


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
