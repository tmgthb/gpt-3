import openai
import streamlit as st
openai.api_key = st.secrets["SECRET_KEY"]
response = openai.Completion.create(engine="davinci", prompt="I expect", max_tokens=5)

st.title('GPT-3')

st.text('This GPT-3 model is the Davinci-engine')
prompt_text = st.text_input(label="Add here phrase, which you want to be completed", value="Add here few words")
st.text('Remaining phrase:')
st.text(response["choices"][0]["text"])


