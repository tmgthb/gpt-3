!{sys.executable} -m pip install openai
import os
import sys
import openai


openai.api_key = "Insert here your Open AI API secret key"
response = openai.Completion.create(engine="davinci", prompt="I expect", max_tokens=5)

st.text(response["choices"][0]["text"])

import pandas as pd
import numpy as np
import streamlit as st
import torch
from transformers import pipeline, AutoModelForCausalLM
st.title('GPT-3')
st.text('This GPT-3 model is the Davinci-engine')
prompt_text = st.text_input(label="Add here phrase, which you want to be completed", value="Add here few words")

