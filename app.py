import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

st.title('홍보 포스터 제작봇🥸')

keyword = st.text_input("키워드를 입력하세요")
if st.button ('포스터 생성'):
  with st.spinner('잠시만 기다려주세요!'):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": keyword,
            },
                    {
                "role": "system",
                "content": "입력 받은 키워드를 홍보하는 솔깃한 홍보문구를 100자 이내로 만들어줘",
            }
        ],
        model="gpt-4o",
    )
    response = client.images.generate(
      model="dall-e-3",
      prompt=f'{keyword}, 오일페인팅 풍으로 그려줘', 
      size="1024x1024",
      quality="standard",
      n=1,
    )
    

  result = chat_completion.choices[0].message.content
  image_url = response.data[0].url
  st.write(result)
  st.image(image_url)
  
  
  
  # url='https://edu.spartacodingclub.kr/random/?'+keyword
  # st.image(url)
