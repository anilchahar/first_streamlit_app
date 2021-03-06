import streamlit
import pandas as p

my_fruit_list = p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index), ['Apple', 'Lime'])
streamlit.dataframe(my_fruit_list)
