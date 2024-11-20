import streamlit as st
import openai
from groq import Groq
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# langsmith tracking 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["LANGCHAIN_PROJECT"]="Q/A Chatbot"

#  prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are the smartest human to ever exist, please respond to the user queries in that manner"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    # openai.api_key=api_key
    Groq.api_key=api_key

    llm=ChatGroq(model=llm)
    output = StrOutputParser()
    chain=prompt|llm|output
    answer = chain.invoke({"question":question})
    return answer 

# title
st.title("Enhanced Q/A Chatbot")


# sidebar
st.sidebar.title("settings")
api_key=st.sidebar.text_input("Enter yout API Key",type="password")

# dropdown to select various models
llm = st.sidebar.selectbox("Select a model",["gemma2-9b-it","llama3-8b-8192","mixtral-8x7b-32768"])

# adjust response parameters
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

# main interface for user input
st.write("Go ahead i am smarter than you")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
elif user_input:
    st.warning("Enter the API key in the side bar")
else:
    st.write("provide the query")