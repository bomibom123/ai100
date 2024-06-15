import streamlit as st


st.title('동물 이미지 찾기🥸')

animal_name = st.text_input("동물 이름 입력")
if st.button ('찾아보기'):
  st.write(animal_name)
  url='https://edu.spartacodingclub.kr/random/?'+animal_name
  st.image(url)
