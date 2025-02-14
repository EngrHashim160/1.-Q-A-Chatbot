import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

## Langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACKING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = "Simple Q&A Chatbot with Open Source Models"
llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-R1",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

print(model.invoke)